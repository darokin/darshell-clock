# darshell-clock

```
ASCII why not
```                                              

![Python application](https://github.com/darokin/darshell-clock/workflows/Python%20application/badge.svg)
[![Build Status](https://travis-ci.com/darokin/darshell-clock.svg?branch=master)](https://travis-ci.com/darokin/darshell-clock)
![GitHub last commit](https://img.shields.io/github/last-commit/darokin/darshell-clock)
![Github last version](https://img.shields.io/github/v/release/darokin/darshell-clock?include_prereleases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**darshellclock** is a *MINIMALIST* console application to displasy time and date with nice ASCII digits in your terminal.

Uses ncurses

Displaying a gif while waiting to make a proper one to showcase the app
<p align="center"><img src="http://darokin.info/imgs/darshellclock.gif" alt="darshellclock demo"/></p>
(this is done in Processing btw)

## Features

Suitable for quite small terminal sizes.
Useful for having a clock sitting around if you use a tiling window manager or tmux for example.

 - Nice square ASCII digits
 - 2 sizes of digits, smaller digits for smaller term
 - Color changing of the time or the date
 - Possibility to hide the date and or the seconds
 - Autoresizing and centering
 - Localise date format
 - All the parameters are saved upon exit
 

## Usage and keys

No specific parameters except the obvious optional arguments
```
-h --help        Show help
-v --version     Show version number
-i --info         Show info
```
While in the app, use these keys to change the configuration :

| Key  | Purpose          
|------|--------------------
| h    | Show or hide help |
| q    | Quit              |
| t    | Change time color |
| d    | Change date color |
| s    | Show or hide date |

 
## Installing and starting

> ```diff
> + Please report issues if you try to install and run into problems!
> ```

Make sure you are running at least Python 3.6.0

Install using pip:
# NOT DEPLOYED YET
```bash
 pip3 install darshellclock 	#installing
 darshellclock					#lauching
```
Or if you want to do it manually you can clone or downlad and extract the project.

You then

```bash
$ git clone https://github.com/darokin/darshell-clock.git
$ cd darshell-clock 
$ python3 darshellclock           # to launch/test
$ python3 setup.py install --user # to install
```
<<<<<<< HEAD
=======
To start the application:
```bash
$ darshellclock
$ python -m main.py
```

### TODO

- [x] Test localisation
- [ ] Test multiplatform
- [ ] Add an argument to auto close after a few second
- [ ] Not too many more functionnality
- [ ] Maybe some dirty stuff to clean up...
- look at the problem of installing forcing to put --user, otherwise...

```
darokin@darokin-AERO-15XV8:~/code/python3/darshell-clock_test$ python3 setup.py install
running install
error: can't create or remove files in install directory

The following error occurred while trying to add or remove files in the
installation directory:

    [Errno 13] Permission denied: '/usr/local/lib/python3.6/dist-packages/test-easy-install-7506.write-test'

The installation directory you specified (via --install-dir, --prefix, or
the distutils default setting) was:

    /usr/local/lib/python3.6/dist-packages/

Perhaps your account does not have write access to this directory?  If the
installation directory is a system-owned directory, you may need to sign in
as the administrator or "root" account.  If you do not have administrative
access to this machine, you may wish to choose a different installation
directory, preferably one that is listed in your PYTHONPATH environment
variable.

For information on other options, you may wish to consult the
documentation at:

  https://setuptools.readthedocs.io/en/latest/easy_install.html

Please make the appropriate changes for your system and try again.
```

>>>>>>> b18902c106c8d4c4b8cde8eaf47081b079f2051d
If you encounter any problem or have any suggestions, please [open an issue](https://github.com/darokin/darshell-clock/issues/new) or [send a pull request](https://github.com/darokin/darshell-clock/pulls).

