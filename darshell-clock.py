#!/usr/bin/env python3

import sys, os
#import os.path
#from os import path
import curses
#import curses.ascii
import datetime

import help
#from utils import ceil

arrNumBig = [
		['████████', '██⠀⠀⠀⠀██', '██⠀⠀⠀⠀██', '██⠀⠀⠀⠀██', '████████'],
		['██', '██', '██', '██', '██'],
		['████████', '⠀⠀⠀⠀⠀⠀██', '████████', '██      ', '████████'],
		['████████', '⠀⠀⠀⠀⠀⠀██', '████████', '⠀⠀⠀⠀⠀⠀██', '████████'],
		['██⠀⠀⠀⠀██', '██⠀⠀⠀⠀██', '████████', '⠀⠀⠀⠀⠀⠀██', '⠀⠀⠀⠀⠀⠀██'],
		['████████', '██⠀⠀⠀⠀', '████████', '⠀⠀⠀⠀⠀⠀██', '████████'],
		['████████', '██⠀⠀⠀⠀', '████████', '██⠀⠀⠀⠀██', '████████'],
		['████████', '⠀⠀⠀⠀⠀⠀██', '⠀⠀⠀⠀⠀⠀██', '⠀⠀⠀⠀⠀⠀██', '⠀⠀⠀⠀⠀⠀██'],
		['████████', '██⠀⠀⠀⠀██', '████████', '██⠀⠀⠀⠀██', '████████'],
		['████████', '██⠀⠀⠀⠀██', '████████', '⠀⠀⠀⠀⠀⠀██', '████████'],
		['⠀⠀⠀', '███', '⠀⠀⠀', '███', '⠀⠀⠀']
	]

arrNumSmall = [
		['▄▄▄▄', '█⠀⠀█', '█▄▄█'], 
		['▄', '█', '█'],
		['▄▄▄▄', '▄▄▄█', '█▄▄▄'],
		['▄▄▄▄', '⠀▄▄█', '▄▄▄█'],
		['▄⠀⠀▄', '█▄▄█', '⠀⠀⠀█'],
		['▄▄▄▄', '█▄▄▄', '▄▄▄█'],
		['▄▄▄▄', '█▄▄▄', '█▄▄█'],
		['▄▄▄▄', '⠀⠀⠀█', '⠀⠀⠀█'],
		['▄▄▄▄', '█▄▄█', '█▄▄█'],
		['▄▄▄▄', '█▄▄█', '▄▄▄█'],
		['⠀', '■', '▀']
	]

helpMenu = (
	("H", "Show/Hise help"), 
	("S", "Show/Hide date"),
	("Q", "Quit"),
	("C", "Date color"),
	("T", "Time color")
)

# helpMenu = (
# 	("H", "kjep"), 
# 	("S", " date"),
# 	("Q", "Quit"),
# 	("C", "Date r"),
# 	("T", "Time or"),
# 	("f", "Shgg sdfsad fsdHigp"), 
# 	("d", "Shate"),
# 	("g", "Qgit"),
# 	("s", "Dateaor"),
# 	("g", "Tlojh")
# )

arrNum 		= arrNumBig
isBig 		= True
isHelp 		= False
isDateAff 	= True
colorClockNum = 2
colorDateNum = 1
MAX_COLORS = 0 # set after color init

# TODO mettre a 18 en mini mais faire que help tienne dedans
MIN_WIDTH = 18-2#36#18
MIN_HEIGHT = 7

MIN_BIG_WIDTH = 45
MIN_BIG_HEIGHT = 45

CONF_FILEPATH = "./darclock.cfg"

lastKey = ""

def draw_number(num, posx, posy, stdscr):
	try:
		for row in arrNum[num]:
			stdscr.move(posy, posx)
			stdscr.addstr(row)
			posy = posy + 1
	except:
		endcurse(stdscr, True)
		exit()

def init(stdscr):
	# Clear and refresh the screen for a blank canvas
	stdscr.clear()
	#curses.init_color(0, 123, 0, 43)
	# TODO bg color in conf file 
	stdscr.refresh()

	# Turn of echo ok keypress / nodelay getch / no cursor etc.
	curses.noecho()
	curses.cbreak()
	stdscr.nodelay(1)
	stdscr.keypad(1) 
	curses.curs_set(False)
	stdscr.border(2)

def intColors():
	global MAX_COLORS

	# Start colors in curses
	curses.start_color()
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
	MAX_COLORS = 7
	curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_BLACK) # for black bg on box


# Clean ending of curses + handling of error message
def endcurse(stdscr, bError):
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
	if bError:
		print("Application exited")
		sys.stdout.write("Need minimum of [" + str(MIN_HEIGHT) + "x" + str(MIN_WIDTH) + "] for ASCII render")
		exit()


def draw_main(stdscr):
	
	global isBig
	global isHelp
	global isDateAff
	global colorClockNum
	global colorDateNum
	global lastKey
	global arrNum
	
	init(stdscr)
	intColors()
	
	while True:
		# Initialization
		stdscr.clear()
		height, width = stdscr.getmaxyx()

		# Handling sizing depending on term size
		if width < 45 or height < 10:
			isBig = False

		# Quitting if size would make ncurse crash
		if height < MIN_HEIGHT or width < MIN_WIDTH:
			endcurse(stdscr, True)

		# Debug
		#stdscr.addstr(0, 0, " " + str(width) + " x " + str(height))

		# Get hours and minutes
		now = datetime.datetime.now()
		datefull = now.strftime('%d / %m / %Y')
		datefullSmall = now.strftime('%d/%m/%Y')
		hoursmin = now.strftime('%H%M%S')
		
		# Select size of block BIG or SMALL
		arrNum = arrNumBig if isBig else arrNumSmall

		# Calculate size of blocks with spacing
		blockwidth = 0
		for i in range(len(hoursmin) - 2):
			blockwidth += len(arrNum[int(hoursmin[i])][0])
			blockwidth = blockwidth + 2 if isBig else blockwidth + 1	
		# Remove extra spacing and Add size of : 
		blockwidth = blockwidth - 2 + 5 if isBig else blockwidth - 1

		# Centering calculations
		start_x = int((width // 2) - (blockwidth // 2))
		#start_y = int((height // 2) - 2.5) # 5 bloch high / 2
		if isDateAff:
			if isBig:
				start_y = int((height // 2) - 3)
			else:
				start_y = int((height // 2) - 2)
		else:
			if isBig:
				start_y = int((height // 2) - 2)
			else:
				start_y = int((height // 2) - 1)
		# ok whatever, must have use ceiled somewhere instead of //
		if height % 2 == 0 and isBig == False:
			start_y -= 1
			

		# Draw TIME
		stdscr.attron(curses.color_pair(colorClockNum))
		stdscr.attron(curses.A_BOLD)
		for i in range(len(hoursmin)-2):
			v = int(hoursmin[i])
			draw_number(v, start_x, start_y, stdscr)
			start_x += len(arrNum[v][0])
			start_x = start_x + 2 if isBig else start_x + 1
			if i == 1:
				draw_number(10, start_x, start_y, stdscr)
				start_x += len(arrNum[10][0])
				start_x = start_x + 2 if isBig else start_x + 1
		stdscr.attroff(curses.color_pair(colorClockNum))
		stdscr.attroff(curses.A_BOLD)	

		# Draw SECONDS
		#if isBig:
		#	stdscr.addstr(start_y + 6, start_x - 7, "  " + hoursmin[-2] + " " + hoursmin[-1], curses.color_pair(colorClockNum))
		
		#Draw DATE
		stdscr.attroff(curses.A_BOLD)
		if isDateAff:
			if isBig:
				stdscr.addstr(start_y + 6, start_x - blockwidth - 2, "⠀⠀" + datefull + "⠀⠀", curses.A_REVERSE + curses.color_pair(colorDateNum))
			else:
				stdscr.addstr(start_y + 4, start_x - len(datefullSmall) - 3, "⠀" + datefullSmall + "⠀", curses.A_REVERSE + curses.color_pair(colorDateNum))	
				# stdscr.addstr(start_y + 4, int(width // 2) - 6, "⠀" + datefullSmall + "⠀", curses.A_REVERSE + curses.color_pair(colorDateNum))	

		#Draw Help
		if isHelp:
			help.showHelp(stdscr, helpMenu, -1, -1, "H E L P", "%C%@darokin ♥", (2 if width > 40 else 1), 0, colorClockNum)

		# Refresh / Input / Timeout
		stdscr.refresh()
		key = stdscr.getch()
		stdscr.timeout(1000)	

		if key == ord("t") or key == ord("t"): #key == curses.KEY_UP:
			colorClockNum -= 1
			if colorClockNum == 0:
				colorClockNum = MAX_COLORS
		elif key == ord("d") or key == ord("D"): #curses.KEY_LEFT:
			colorDateNum -= 1
			if colorDateNum == 0:
				colorDateNum = MAX_COLORS
		elif key == ord('s') or key == ord("S"):
			isDateAff = not isDateAff
		#elif key == ord('s'):
		#	isBig = not isBig
		elif key == ord('h'):
			isHelp = not isHelp
		#elif key == ord('e'):
		#	lastKey = "e"
		#elif key == ord('r') and lastKey == "e":
		#	os.system("shutdown now")
		elif key == ord('q') or key == ord("Q"):
			break
		else:
			lastKey = ""

	# Loop ended properly we save the conf
	with open(CONF_FILEPATH, 'w') as writer:
		writer.write(("1" if isDateAff else "0") + ";" + str(colorClockNum) + ";" + str(colorDateNum))

	# Ending
	endcurse(stdscr, False)

def main():
	global isDateAff
	global colorClockNum
	global colorDateNum

	# Test resolution si mini ok
	rows, columns = os.popen('stty size', 'r').read().split()
	if int(rows) < MIN_HEIGHT or int(columns) < MIN_WIDTH:
		print("Need minimum of [" + str(MIN_HEIGHT) + "x" + str(MIN_WIDTH) + "] for ASCII render, your term indicates a [" + rows + "x" + columns + "] resolution ")
		df = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
		print("Time : " + df)
		exit()
	
	# Read la config si il y en a une 
	if os.path.exists(CONF_FILEPATH): 
		with open(CONF_FILEPATH, 'r') as reader:
			strconf = reader.read()
		tabconf = strconf.split(";")
		isDateAff 		= (int(tabconf[0]) == 1) #True
		colorClockNum 	= int(tabconf[1])
		colorDateNum 	= int(tabconf[2])

	curses.wrapper(draw_main)

if __name__ == "__main__":
	main()
