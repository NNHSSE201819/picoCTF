# District 203 picoCTF Specific

## Project Overview:
The goal of the CTF (Capture the Flag) is to be a self-contained district 203 specific competition for the use of Cybersecurity class(es). Upon successful deployment all users will be able to access the CTF website, register or login into a personal account, and earn points by solving problems related to cybersecurity. The website should keep track of individual users’ progress across multiple sessions. Those with administrative accounts will be able to add, package, deploy, and enable/disable problems. They can also create classrooms and oversee the progress of other users. Detailed explanation for functions of all options available on the website can be found in the folder “SE1819-resources” under “Button Reference” . 

## Basic Structure:
-- Ansible is the provisioning system that facilitates the deployment for testing and development and eventually cloud usage if it was      the CTF was to be made public on the web through Amazon Web Services. 
-- Vagrant deploys the site.Vagrant launches the virtualboxes, starting the servers and making the website accessible to users
-- Virtualbox actually runs the site.
-- The web server exists in a virtual machine (computer in a physical computer) and connects to another virtual machine, the shell  server. 
-- The shell server allows users to test problem solutions without leaving the site. 
The shell server also allows administrators (with a special login) to add problems to the web server for users to solve.


## Admin, setting up the server for self or student use

Prerequisites:
-- VirtualBox found here: https://www.virtualbox.org/wiki/Downloads
-- Vagrant found here: https://www.vagrantup.com/downloads.html
-- Repository clone from Github
when cloning a repository with a fresh install of GitHub Desktop,
replace the portion of the local path that starts: 
\\sd203.org\dfs-root$\HS\NNHS\Student\
with: C:\Users\
for example, the final local path for me could be: C:\Users\gcschmit\GitHub\objects-gcschmit

### Platform Specifications:
64-bit for dual Vagrant and Virtualbox compatibility
32 bit will be supported by Virtualbox until July 2020
Don’t use Raspberry Pi

1.Open up your computer’s terminal
2. Navigate to the location of the picoCTF folder on your computer (using the terminal)
  a. Option 1. Use cd and the path name of the picoCTF folder
  b. Option 2. Open github desktop, open up the picoCTF repository, select the repository option on the top menu bar, select the option that says “open in terminal”
3. In the terminal type the command “vagrant up” hit enter
  a. It should now be “provisioning”, running through all the files and preparing them 
  b. This step takes some time to complete, be patient
  c. Vagrant is running when the terminal gives a new line for a command to be entered
4. Open your preferred browser (we used Chrome) and open a new tab
5. Enter in the port address for the web site: http://192.168.2.2/
6. The site can now be navigated freely, in the folder “SE1819-resources” the file “Button Reference” has information on what the options on the website do.

Note: At this point in time the server is running and only accessible off of localhost, for use on multiple different devices look to the steps for a student.


## Student, user to access server and solve problem

Prerequisites:
-- Access to terminal
-- Access to multiple browsers
-- The computer running the server must be on the same network as the computer that wants to access the server
Follow the steps detailed in the file “Connecting to the CTF Server-Linux Mac” found in the folder “SE1819-resources” to set up a tunnel and access the website. 
Note, you will have to sign in using the computer login information of the computer that is running the server. 


## Writing Problems:
1. Follow the instructions here (https://github.com/picoCTF/picoCTF/wiki/Adding-Your-Own-Content) on the specifications required for a -problem and how to write the problem.json file and the challenge.py file.
2. The problem.json file specifies name, category, description, score, hints, author, and organization of each problem. Refer to any of the problems we wrote or example problems for an example of the problem.json file. More info: https://github.com/picoCTF/picoCTF/wiki/Problem.json
3. The challenge.py file specifies the static flag, flag file, and source code. Refer to any of the problems we wrote or example problems for an example of the challenge.py file.More info: https://github.com/picoCTF/picoCTF/wiki/Challenge.py
4. To create a static flag, reference the challenge.py file in picoCTF/problems/SE2019Problems/Cipher1/
5. To create a random flag, reference the vuln.c file in picoCTF/problems/SE2019Problems/RandoTest/. (there are further instructions for random flags later in the README)
6. To link a file in the problem description, refer to the the problem.json file in picoCTF/problems/SE2019Problems/RandoTest/. The file is embedded in the description line.

## How to add a problem to picoCTF:
1.Go to shell 
  a. Can do this on the website, the embedded shell OR use the terminal
Login: vagrant
Password: vagrant
Cd ..
Cd .. 
Cd picoCTF/problems/[subfolder]/[optional sub-sub folder]/
Essentially need to navigate to location/containing folder of the file, 
Sudo shell_manager package [file name]
Sudo dpkg -i nnhs-[file name, numbers].deb
Use “ls” command to find full debian file name
Sudo shell_manger deploy [ProblemName]
 NOW, navigate from the shell or terminal (where ever you were entering the commands) and got to the Management page on the website (this requires you to be signed into the admin account). 
Go to the “Shell Server” management sub page
Press the “Update” button towards the bottom of the screen
Press the “Load Deployment” button to the right of the “Update” option
NOW, navigate to the Manage Problems page
Enable Desired Problem(s)
Celebrate

## Random Flag:
Wherever you want the flag to be, insert {{flag}} (if you want it to be a string, put it in quotes)
It should automatically be replaced
The flag.txt file (containing only {{flag}}) should be automatically generated and given protected file status

## Software Engineering 2018-2019 Student Created Problems:

We have added all the problems we wrote ourselves to a folder in the problems folder called “SE2019Problems”. There is also an “examples” folder with the sample problems from picoCTF.

### List of Problems
Name: Color Pentagon
How to Solve: This problem has a static flag which is encoded in the pattern of the pentagons. Inside this pattern is a message in morse code. The only thing you need to pay attention to is the shape within the pentagon, the colors or orientation do not mean anything. One of the three “centers” (empty, pentagon, circle) represents a space between words, another represents a dot, and the last symbol represents a dash. 

Name: Hidden Map
How to Solve: This problem has a static flag which is hidden somewhere in the image. Download the image and open it in a photo editing application like Photoshop, this is what was used when creating and testing the image. In Photoshop go to the images tab and explore different options under Adjustments. Be sure to look at the small details after adjusting, it may not initially seem like there is a clear black and white way to solve the problem but maybe by adjusting a predominant color value the flag will appear. 

Name: Cipher 1
How to Solve: Caesar Cipher, shift original message left 5 letters to get key “welcome to cybersecurity”. This is a very basic problem and shouldn’t be worth too many points.

Name: RandoTest
RANDOM flag problem. The source file “vuln.c” contains “{{flag}}” which is replaced with a random string which can be correctly submitted as the flag.

Name: ColorSquare
Static flag problem. From left to right, top to bottom, the red value of the RGB value of each square refers to the ASCII code of each character in the flag. For example, the 3rd square has an RGB value of 65, 66, 50. Thus, the 3rd character is “A” because the ASCII of “A” is 65.


# picoCTF

The picoCTF platform is the infrastructure which is used to run
[picoCTF](https://picoctf.com/).

The platform is designed to be easily adapted to other CTF or programming
competitions. Additional documentation can be found on the
[wiki](https://github.com/picoCTF/picoCTF/wiki).

## Quick Start

The following steps will use [Vagrant](https://www.vagrantup.com/) to get you
quickly up and running with the picoCTF platform by deploying the code base to
two local virtual machines.

1. `git clone -c core.autocrlf=false https://github.com/picoCTF/picoCTF.git`  
   (see [this
   link](https://github.com/picoCTF/picoCTF/issues/68#issuecomment-346736808)
   for an explanation of this command line)
2. `cd picoCTF`
3. `vagrant up`
4. Navigate to http://192.168.2.2/
5. Register an account (this user will be the site administrator)

If you want to change CTF Placeholder, edit
picoCTF-web/web/_includes/header.html

There are now quick ways to change the memory, number of CPUs and IP addresses and run multiple instances.

After you do the git clone, rename picoCTF to picoCTF_XXX (fill in XXX with something unique for each)
Start by running a command like the below. 
J is the number of CPUs
M is the amount of memory in GB
SIP is shell IP address (default is 192.168.2.2)
WIP is web IP address (default is 192.68.2.3)

J=2 M=6 SIP=192.168.2.53 WIP=192.168.2.52 vagrant up shell && SIP=192.168.2.53 WIP=192.168.2.52 vagrant up web


## Project Overview

This project is broken down into a few discrete components that compose to build
a robust and full featured CTF platform. Specifically the project is consists of
the following:

1. [picoCTF-web](./picoCTF-web). This is the website and all APIs.
2. [picoCTF-shell](./picoCTF-shell). This is where users go to solve challenges.
3. [problems](./problems). This is the CTF problems source code.
4. [ansible](./ansible). This is used for configuring machines.
5. [terraform](./terraform). This is used for deployment.
5. [vagrant examples](./vagrant). This hosts various vagrant VM examples.

### Walkthrough

Once you bring everything up, the main flow between components is:

![Architecture](docs/architecture.png)

Here is a walkthrough:
1. The user connects to the "Web Server". This is an nginx server.
   - The nginx server serves up content in [picoCTF-web/web](picoCTF-web/web).
   - The nginx server only serves up static HTML files.
   - Most HTML files contain javascript, which is rendered browser-side for
     speed.
   - The browser rendering in turn makes requests to a REST-ful like API `/api/`
     to nginx. Requests to `/api` are forwarded to an API server (running on the
     same host for development).
   - There is a special interface called `/admin`, which is used by the admin to
     connect to new shell servers.
2. The users `/api` request is forwarded to the API server.
   - The API server is a python flask server with code under
     [picoCTF-web/api](picoCTF-web/api)
   - There is an API for adding users, checking passwords, etc.
   - There is an API for serving up challenges, checking flags, etc.
   - The API keeps track of user score and membership to teams.
3. A user can `ssh` to the shell server.
   - The shell server is loaded with problems, with examples in
     [problems](problems/).
   - The web server connects to the shell server and retrieves a JSON file
     containing problem instance location, point value, etc.
   - The web server authenticates users using password data stored and via the
     API.

Some important terminology:
+ A _problem_ is a logical CTF problem. (Sometimes called a _challenge_)
  + Solving a problem gives a user points.
  + A problem can be _locked_ or _unlocked_ for a user.
  + Super important: problems *do not* have flags. They are purely logical.
+ A _problem instance_, or _instance_ for short, is a generated version of a
  challenge to be solved by a user.
  + A single problem can have instances `inst_1`, `inst_2`, ..., `inst_n`. Each
    instance has its own flag `flag_1`, `flag_2`, ..., `flag_n`
  + Users are assigned specific problem instances, and they are expected to
    submit only their flag. For example, if user Foo has instance `inst_1`, only
    `flag_1` is a valid flag (aa separate instance flag `flag_2` is not valid)
  + Instances were invented to help combat flag sharing. If player Foo has been
    assigned `inst_1` but submits `flag_2`, then whomever has `inst_2` shared
    their flag. There may be legitimate reasons for flag sharing, but in many
    competitions it is indicative of cheating.
  + Instances are generated from _template_. Think of it like templating in a
    web framework. For example, a buffer overflow problem may template the
    specific buffer size so a solution for `inst_i` will not work for `inst_j`.

### picoCTF-web

The competitor facing web site, the API for running a CTF, and the management
functionality for CTF organizers. The development [Vagrantfile](./Vagrantfile))
deploys picoCTF-web to a virtual machine (web) at http://192.168.2.2/. If you
want to modify the look and feel of the website, this is the place to start.

### picoCTF-shell-manager

The tools to create, package, and deploy challenges for use with the picoCTF
platform. This supports the deployment of auto-generated challenge instances and
provides competitors shell access to aid in challenge solving. The development
[Vagrantfile](./Vagrantfile) deploys the shell-server as a second virtual
machine (shell) at http://192.168.2.3/. If you want to modify challenge
deployment primitives, this is the place to start.

### picoCTF Compatible Problems

Example challenges that are compatible with the picoCTF platform. These
challenges can be easily shared, deployed, or adapted for use in a CTF. The
development [Vagrantfile](./Vagrantfile) installs these examples to the shell
server and loads them into the web interface. If you want to see how to create
challenges or leverage the hacksport library, this is the place to start.

### Ansible for Automated System Administration

The tool we use to install, configure, deploy, and administer the picoCTF
platform is [Ansible](https://www.ansible.com/). This allows us to create
flexible, parameterized, automated playbooks and roles that apply across
development, staging, and production environments. If you want to modify way the
platform is configured, this is the place to start.

### Terraform for automated AWS deployment

The tool we use to codify our infrastructure as code is
[Terraform](https://www.terraform.io/). This allows a simple process for
creating, destroying, and managing a public deployment of the platform. If you
want to run a live competition on AWS, this is the place to start.

## Running Your Own Competition

If you are looking to run your own CTF competition, you should:
1. Make sure you understand how to deploy the infrastructure via terraform and
   ansible.
2. You can reskin the look and feel of the site by editing the
   [picoCTF-web/web](picoCTF-web/web) javascript and HTML code.
3. To enable password reset emails, log in using the site administrator 
   account and configure Email under Management > Configuration. 
4. You should start writing your own problems, loading them into the shell
   server, and syncing the web server problem set with the shell server via the
   `/admin` URL endpoint.

Do not underestimate the importance of spending significant time in problem
development. Our internal system is:
1. We form a working group for the contest.
2. We often vet problem ideas with the group before implementation.
3. Implement and deploy. Hardcode nothing (or as little as possible).
4. *THE KEY STEP:* Play test! Often the initial problem will have an
   intellectual leap built-in that's obvious to the creator but to no one
   else. Play testing makes sure the problem is coherent, self-contained, and
   fun.

## Want your own contest, but are not a developer?

[ForAllSecure](https://forallsecure.com) offers professionally-run original
hacking contests as a service.

## Giving Back and Development

The picoCTF platform is always under development.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for setting up a git workflow and some
  standards.
- We are especially interested any improvements on continuous integration and
  automated testing.

If you are interested in research in CTFs (e.g., improving skill acquisition,
decreasing time to mastery, etc.), please feel free to email David Brumley.

NOTE: We have not maintained backward compatibilties with
[picoCTF-Platform-2](https://github.com/picoCTF/picoCTF-platform-2). Please read
the documentation on the wiki for [forks of
picoCTF-Platform-2](https://github.com/picoCTF/picoCTF/wiki/Repository-linage#forks-of-picoctf-platform-2).

## Credits

picoCTF was started by David Brumley with his CMU professor hat in 2013. The
intention has always been to give back to the CTF community.

The original heavy lifting was done by his graduate students, and special thanks
is due to Peter Chapman (picoCTF 2013 technical lead) and Jonathan Burket
(picoCTF 2014 technical lead) for their immense efforts not only developing
code, but for organizing art work, problem development, and so on.

In 2015-2016 significant effort was done by
[ForAllSecure](https://forallsecure.com) at the companies expense. This includes
adding concepts like the shell server, and rewriting significant portions of the
web server.

Both CMU and ForAllSecure have agreed to release all code under the [MIT
LICENSE](./LICENSE) . We do encourage attribution as that helps us secure
funding and interest to run picoctf year after year, but it is not
necessary. Also, if you do end up running a contest, do feel free to drop David
Brumley a line.

- Bug Reports: [GitHub Issues](https://github.com/picoCTF/picoCTF/issues)
- Contributors (in no particular order): David Brumley, Tim Becker, Chris Ganas,
  Roy Ragsdale, Peter Chapman, Jonathan Burket, Collin Petty, Tyler Nighswander,
  Garrett Barboza
