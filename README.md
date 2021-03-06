### :warning: Please use **pip3** or **python3** instead of pip and python
<p></p>

# darshell-clock

![Python application](https://github.com/darokin/darshell-clock/workflows/Python%20application/badge.svg)
[![Build Status](https://travis-ci.com/darokin/darshell-clock.svg?branch=master)](https://travis-ci.com/darokin/darshell-clock)
![GitHub last commit](https://img.shields.io/github/last-commit/darokin/darshell-clock)
![Github last version](https://img.shields.io/github/v/release/darokin/darshell-clock?include_prereleases)
[![PyPI version shields.io](https://img.shields.io/pypi/v/darshellclock.svg)](https://pypi.python.org/pypi/darshellclock/)
[![PyPI download month](https://img.shields.io/pypi/dm/darshellclock.svg)](https://pypi.python.org/pypi/darshellclock/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**darshellclock** is a *MINIMALIST* console application to display time and date with nice ASCII digits in your terminal. Uses *curses*

Here is a demo but mostly you would use this in a small persistant terminal. (More on "why this project?" in the side notes at the end)

<p align="center"><img src="http://darokin.info/github/imgs/darshellclock_01.gif" alt="darshellclock demo"/></p>

## Features

Suitable for quite small terminal sizes.
Useful for having a clock sitting around if you use a tiling window manager or tmux for example.

 - Nice 'blocky' ASCII digits :purple_heart:
 - Localised date format :airplane:
 - 2 sizes of digits, smaller digits for smaller term
 - Autoresizing and centering
 - Color selection of the time or the date
 - Possibility to hide the date and/or the seconds
 - Autoclosing (if wanted, see arguments in 'Usage and keys')
 - All the parameters are saved upon exit :+1:
 

## Usage and keys

The usual arguments are here + a 'stop' argument for the autoclosing functionnality
```
-h --help        Show help
-v --version     Show version number
-i --info        Show info [ASCII ♥]
-s --stop STOP   Quit the application after <STOP> seconds
```
While in the app, use these keys to change the configuration :

| Key  | Purpose          
|------|--------------------
| <kbd>h</kbd> | Show or hide help |
| <kbd>q</kbd> | Quit              |
| <kbd>z</kbd> | Change time color |
| <kbd>x</kbd> | Change date color |
| <kbd>d</kbd> | Show or hide date |
| <kbd>s</kbd> | Show or hide secs |
<p></p>

## Installing and starting

Use Python 3.x

:warning: Please use **pip3** or **python3** instead of pip and python

Install using **pip3**:
```bash
$ pip3 install darshellclock 	# installing
$ darshellclock			# lauching
```
Or if you want to do it manually you can clone or downlad and extract the project:

```bash
$ git clone https://github.com/darokin/darshell-clock.git
$ cd darshell-clock 
$ python3 darshellclock           # to launch/test ; or you can install it :
$ python3 setup.py install --user # to install
$ darshellclock                   # to launch installed version
```


## Side notes

:information_desk_person: This program was mainly made to try out a whole life cycle of a simple python app and to grasp new skills around github/CI/python package distribution/etc.
The [discussion section](https://github.com/darokin/darshell-clock/discussions) is open if needed.

If you encounter any problem or have any suggestions, please [open an issue](https://github.com/darokin/darshell-clock/issues/new) or [send a pull request](https://github.com/darokin/darshell-clock/pulls).

