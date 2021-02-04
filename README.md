# darshell-clock

![Python application](https://github.com/darokin/darshell-clock/workflows/Python%20application/badge.svg)
[![Build Status](https://travis-ci.com/darokin/darshell-clock.svg?branch=master)](https://travis-ci.com/darokin/darshell-clock)
![GitHub last commit](https://img.shields.io/github/last-commit/darokin/darshell-clock)
![Github last version](https://img.shields.io/github/v/release/darokin/darshell-clock?include_prereleases)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**darshellclock** is a *MINIMALIST* console application to display time and date with nice ASCII digits in your terminal.

Uses ncurses

Here is a demo but mostly you would use this in a small persistant terminal.

<p align="center"><img src="http://darokin.info/imgs/darshellclock.gif" alt="darshellclock demo"/></p>

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

Use Python 3.x

Install using pip:
```bash
 pip install darshellclock 	#installing
 darshellclock			#lauching
```
Or if you want to do it manually you can clone or downlad and extract the project:

```bash
$ git clone https://github.com/darokin/darshell-clock.git
$ cd darshell-clock 
$ python3 darshellclock           # to launch/test ; or you can install it :
$ python3 setup.py install --user # to install
```
To start the application:
```bash
$ darshellclock				# from anywhere if installed
$ python -m darshellclock	# from the main project folder
```

If you encounter any problem or have any suggestions, please [open an issue](https://github.com/darokin/darshell-clock/issues/new) or [send a pull request](https://github.com/darokin/darshell-clock/pulls).

