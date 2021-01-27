#!/usr/bin/env python3

import sys,os
import curses
import curses.ascii
#from curses.textpad import Textbox, rectangle
import datetime

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

arrNum 		= arrNumBig
isBig 		= True
isHelp 		= False
isDateAff 	= True
colorClockNum = 2
colorDateNum = 1
MAX_COLORS = 7

MIN_WIDTH = 18
MIN_HEIGHT = 5

MIN_BIG_WIDTH = 45
MIN_BIG_HEIGHT = 45

lastKey = ""

def draw_number(num, posx, posy, stdscr):
	try:
		for row in arrNum[num]:
			stdscr.move(posy, posx)
			stdscr.addstr(row)
			posy = posy + 1
	except:
		print("fuch")
		endcurse(stdscr, True)
		exit()

def init(stdscr):
	# Clear and refresh the screen for a blank canvas
	stdscr.clear()
	#curses.init_color(0, 123, 0, 43)
	#curses.init_color(0, 0, 0, 0)
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
	# Start colors in curses
	curses.start_color()
	#curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(6, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)

	curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_BLACK)



# Cell do as // but ceil instead of floor, ok for integers
def ceil(n, d):
    return (n + d - 1) // d

# 
def rect(win, _px, _py, _w, _h):
    #Draw a rectangle at X , Y with WITH AND HEIGHT 
    
	win.vline(_py+1, _px, curses.ACS_VLINE, _h - 1)
	win.hline(_py, _px+1, curses.ACS_HLINE, _w - 1)
	win.hline(_py + _h, _px+1, curses.ACS_HLINE, _w - 1)
	win.vline(_py+1, _px + _w, curses.ACS_VLINE, _h - 1)
	win.addch(_py, _px, curses.ACS_ULCORNER)
	win.addch(_py, _px + _w, curses.ACS_URCORNER)
	win.addch(_py + _h, _px + _w, curses.ACS_LRCORNER)
	win.addch(_py + _h, _px, curses.ACS_LLCORNER)



    # win.vline(_py+1, ulx, curses.ACS_VLINE, _w)#lry - uly - 1)
    # win.hline(uly, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)
    # win.hline(lry, ulx+1, curses.ACS_HLINE, lrx - ulx - 1)
    # win.vline(uly+1, lrx, curses.ACS_VLINE, lry - uly - 1)
    # win.addch(uly, ulx, curses.ACS_ULCORNER)
    # win.addch(uly, lrx, curses.ACS_URCORNER)
    # win.addch(lry, lrx, curses.ACS_LRCORNER)
    # win.addch(lry, ulx, curses.ACS_LLCORNER)

def endcurse(stdscr, bError):
	curses.nocbreak()
	stdscr.keypad(False)
	curses.echo()
	curses.endwin()
	if bError:
		print("Application exited")
		sys.stdout.write("Need minimum of [" + str(MIN_HEIGHT) + "x" + str(MIN_WIDTH) + "] for ASCII render")
		exit()

def showHelp(stdscr, _title, _footer, _data, _nbLines, _x, _y, _color):
	baseY = _y
	baseX = _x

	numColumns = 1
	numLines = 0
	totalWidth = 0
	maxLenCol = 1
	bGuessNumLines = True
	ind = 0

	# Find width now if centering needed
	for vv in _data:
		# Line size for columns
		if bGuessNumLines:
			numLines += 1
		numLines = _nbLines
		lineLen = 1 + len(vv[0]) + 1 + len(vv[1]) + 1
		if lineLen > maxLenCol:
			maxLenCol = lineLen
		ind = _data.index(vv)
		#ind += 1
		# Test sortie
		if ind == (len(_data) - 1):
			totalWidth = totalWidth + maxLenCol + 1
			break
		if ind > 0 and ((ind + 1) % numLines) == 0:
			totalWidth = totalWidth + maxLenCol + 1
			maxLenCol = 1

	# Centering calculations
	height, width = stdscr.getmaxyx()
	if _x == -1:
		_x = int((width // 2) - (totalWidth // 2))	
		baseX = _x
	if _y == -1:
		_y = int((height // 2) - ceil(numLines, 2))	
		baseY = _y

	# Background
	for yy in range(numLines):
		for xx in range(totalWidth - 1):
			stdscr.addch(_y + yy + 1, _x + xx + 1, '⠀', curses.color_pair(8))# + curses.A_REVERSE)

	numColumns = 1
	numLines = 0
	#totalWidth = 0
	maxLenCol = 1
	bGuessNumLines = True
	ind = 0
	_y = baseY + 1
	for vv in _data:
		# Line size for columns
		if bGuessNumLines:
			numLines += 1
		numLines = _nbLines
		lineLen = 1 + len(vv[0]) + 1 + len(vv[1]) + 1
		if lineLen > maxLenCol:
			maxLenCol = lineLen

		stdscr.addstr(_y, _x + 2, vv[0], curses.color_pair(_color) + curses.A_BOLD) #curses.A_REVERSE
		stdscr.addstr(_y, _x + 4, vv[1])
		ind = _data.index(vv)
		#ind += 1

		# Test exit
		if ind == (len(_data) - 1):
			#totalWidth = totalWidth + maxLenCol + 1
			break

		if ind > 0 and ((ind + 1) % numLines) == 0:
			if ind <= len(_data) - 2:
				for i in range(numLines):
					stdscr.addstr(_y - i, _x + maxLenCol + 1, "|", curses.color_pair(_color) + curses.A_BOLD)
			_x = _x + maxLenCol + 1
			_y = baseY + 1
			#totalWidth = totalWidth + maxLenCol + 1
			maxLenCol = 1
			bGuessNumLines = False
		else:
			_y += 1 

	# Draw frame
	stdscr.attron(curses.color_pair(_color))
	rect(stdscr, baseX, baseY, totalWidth, numLines + 1)
	#rectangle2(stdscr, baseY, baseX, numLines + baseY + 1, 1 + totalWidth + baseX)
	stdscr.attroff(curses.color_pair(_color))
	# Title
	stdscr.addstr( baseY, baseX + 2, " " + _title + " ", curses.color_pair(_color) + curses.A_BOLD) #curses.A_REVERSE
	# Footer
	stdscr.addstr(baseY + numLines + 1, baseX + totalWidth - len(_footer) - 2, " " + _footer + " ", curses.color_pair(6) + curses.A_BOLD)

def draw_main(stdscr):
	
	global isBig
	global isHelp
	global isDateAff
	global colorClockNum
	global colorSecsNum
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
		stdscr.addstr(0, 0, " " + str(width) + " x " + str(height))

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
				stdscr.addstr(start_y + 4, int(width // 2) - 6, "⠀" + datefullSmall + "⠀", curses.A_REVERSE + curses.color_pair(colorDateNum))	
	
		# boxh = curses.newwin(6, 33, 2, 3)
		# boxh.box();
		# #rectangle(stdscr, 41,0, 1+5+1, 1+30+1)
		# boxh.addstr(1, 1, "DU IH D")
		# boxh.refresh()
		# stdscr.refresh()

		#Draw Help
		if isHelp:
			showHelp(stdscr, "H E L P", "@darokin ♥", helpMenu, ceil(len(helpMenu), 2), -1, -1, colorClockNum)

		#box = Textbox(editwin)
		# Let the user edit until Ctrl-G is struck.
		#box.edit()
		# Get resulting contents
		#message = box.gather()

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

	# Ending
	endcurse(stdscr, False)

def main():
	rows, columns = os.popen('stty size', 'r').read().split()
	if int(rows) < MIN_HEIGHT or int(columns) < MIN_WIDTH:
		#print("You must have at least " + str(MIN_HEIGHT) + " rows and " + str(MIN_WIDTH) + " columns to have the graphic clock")
		#print("You seems to have " + rows + " rows and " + columns + " columns in your terminal")
		print("Need minimum of [" + str(MIN_HEIGHT) + "x" + str(MIN_WIDTH) + "] for ASCII render, your term indicates a [" + rows + "x" + columns + "] resolution ")
		df = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
		print("Time : " + df)
		exit()
	curses.wrapper(draw_main)

if __name__ == "__main__":
	main()
