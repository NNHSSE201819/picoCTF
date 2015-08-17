"""
User Testing Module
"""

import pytest
import bcrypt
import api

from api.common import safe_fail, WebException, InternalException
from common import clear_collections, ensure_empty_collections
from common import base_team, base_user, new_team_user
from conftest import setup_db, teardown_db

dict_filter = lambda dict, items: {k:v for k,v in dict.items() if k in items}

class TestNewStyleUsers(object):
    """
    API Tests for the new supported registration.
    """

    def setup_class(self):
        setup_db()

        # Get the settings to ensure they are given the defaults.
        api.config.get_settings()
        api.config.change_settings({"max_team_size": 3})

    def teardown_class(self):
        teardown_db()

    @ensure_empty_collections("users", "teams")
    @clear_collections("users", "teams")
    def test_simple_user_creation(self):
        """
        Tests the newer and simplified user creation.
        """

        user = dict_filter(base_user.copy(), ["username", "firstname", "lastname", "email"])
        user["password"] = "test"
        uid = api.user.create_simple_user_request(user)

        team = api.user.get_team(uid=uid)

        assert team["team_name"] == user["username"], "Team name does not match username."
        assert team["size"] == 1, "Individual team size is incorrect."


class TestUsers(object):
    """
    API Tests for user.py
    """

    def setup_class(self):
        setup_db()

        # Get the settings to ensure they are given the defaults.
        api.config.get_settings()
        api.config.change_settings({"max_team_size": 2})

    def teardown_class(self):
        teardown_db()

    @ensure_empty_collections("users", "teams")
    @clear_collections("users", "teams")
    def test_create_batch_users(self):
        """
        Tests user creation.

        Covers:
            user.create_user
            user.get_all_users
            user.get_user
        """

        tid = api.team.create_team(base_team.copy())

        uids = []
        for i in range(api.config.get_settings()["max_team_size"]):
            name = "fred" + str(i)
            uids.append(api.user.create_user(
                name, name, name,  name + "@gmail.com", name, tid
            ))

        with pytest.raises(InternalException):
            name = "fred" + str(api.config.get_settings()["max_team_size"])
            api.user.create_user(name, name, name, name+"@gmail.com", name, tid)

        for i, uid in enumerate(uids):
            name = "fred" + str(i)

            user_from_uid = api.user.get_user(uid=uid)
            user_from_name = api.user.get_user(name=name)

            assert user_from_uid == user_from_name, "User lookup from uid and name are not the same."

    @ensure_empty_collections("users", "teams")
    @clear_collections("users", "teams")
    def test_create_user_request_email_validation(self):
        """
        Tests the email validation during user registration.

        Covers:
            partially: user.create_user_request
        """

        team = base_team.copy()
        api.team.create_team(team)

        invalid_email_user = base_user.copy()
        invalid_email_user["email"] = "not_an_email"

        with pytest.raises(Exception):
            api.user.create_user_request(invalid_email_user)
            assert False, "Was able to register a user with something that doesn't look like an email."

        invalid_email_user["email"] = "hax$@test.c"

        with pytest.raises(WebException):
            api.user.create_user_request(invalid_email_user)
            assert False, "Was able to register a user with invalid characters"

        valid_email_user = base_user.copy()
        assert api.user.create_user_request(valid_email_user), "Was not able to register a valid email."

    @ensure_empty_collections("users", "teams")
    @clear_collections("users", "teams")
    def test_get_team(self):
        """
        Tests retrieving the team from a given uid.

        Covers:
            team.create_team
            user.create_user_request
            user.get_team
        """

        team = base_team.copy()
        tid = api.team.create_team(team)
        uid = api.user.create_user_request(base_user.copy())

        result_team = api.user.get_team(uid=uid)
        assert tid == result_team['tid'], "Unable to pair uid and tid."


    @ensure_empty_collections("users", "teams")
    @clear_collections("users", "teams")
    def test_create_user_request_new_team(self):
        """
        Tests the registration of users creating new teams.

        Covers:
            partially: user.create_user_request
            team.get_team_uids
        """

        uid = api.user.create_user_request(new_team_user)
        assert uid == api.user.get_user(name=new_team_user["username"])["uid"], "Good user created unsuccessfully."

        team = api.team.get_team(name=new_team_user["team-name-new"])
        assert team, "Team was not created."

        team_uids = api.team.get_team_uids(team["tid"])
        assert uid in team_uids, "User was not successfully placed into the new team."

        sheep_user = new_team_user.copy()
        sheep_user["username"] = "something_different"

        with pytest.raises(WebException):
            api.user.create_user_request(sheep_user)
            assert False, "Was able to create a new team... twice"

        sheep_user = new_team_user.copy()
        sheep_user["team-name-new"] = "noneixstent_team"

        with pytest.raises(WebException):
            api.user.create_user_request(sheep_user)
            assert False, "Was able to create two users with the same username."

    @ensure_empty_collections("users", "teams")
    @clear_collections("users", "teams")
    def test_create_user_request_existing_team(self):
        """
        Tests the registration of users on existing teams.

        Covers:
            partially: user.create_user_request
            team.get_team_uids
            team.create_team
        """

        tid = api.team.create_team(base_team.copy())
        assert tid, "Team was not created."

        uid = api.user.create_user_request(base_user.copy())
        assert uid == api.user.get_user(name=base_user["username"])["uid"], "Good user created unsuccessfully."

        with pytest.raises(WebException):
            api.user.create_user_request(base_user.copy())
            assert False, "Was able to register and join the team twice."

        with pytest.raises(WebException):
            invalid_team_user = base_user.copy()
            invalid_team_user["username"] = "asdf"
            invalid_team_user["team-name-existing"] = "Totally Invalid"
            api.user.create_user_request(invalid_team_user)
            assert False, "Was able to join a team that doesn't exist."

        with pytest.raises(WebException):
            invalid_team_user = base_user.copy()
            invalid_team_user["username"] = "asdf"
            invalid_team_user["team-password-existing"] = "Not correct"
            api.user.create_user_request(invalid_team_user)
            assert False, "Was able to join a team with an invalid password."

        team_uids = api.team.get_team_uids(tid)

        assert len(team_uids) == 1, "Invalid teams were created though the tests passed."
        assert uid in team_uids, "User was not successfully placed into the existing team."

    @ensure_empty_collections("users", "teams")
    @clear_collections("users", "teams")
    def test_change_password_user(self):
        """
        Tests password change functionality.

        Covers:
            user.update_password
            user.hash_password
        """

        tid = api.team.create_team(base_team.copy())
        uid = api.user.create_user("fred", "fred", "fred", "fred@gmail.com", "HASH", tid)

        old_hash = api.user.get_user(uid=uid)["password_hash"]
        assert old_hash == "HASH", "Was unable to confirm password was stored correctly."

        api.user.update_password_request({"new-password":"HACK", "new-password-confirmation":"HACK"}, uid)

        new_hash = api.user.get_user(uid=uid)["password_hash"]

        assert bcrypt.hashpw("HACK", new_hash) == new_hash, \
            "Password does not match hashed plaintext after changing it."

        with pytest.raises(WebException):
            api.user.update_password_request({"new-password": "", "new-password-confirmation":""}, uid)
            assert False, "Should not be able to update password to nothing."
