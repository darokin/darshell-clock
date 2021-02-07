import curses

from .utils import ceil


# Draw a rectangle at X , Y with WITH AND HEIGHT
# ... ncurses as it but i can stend invert x,y and having lower right pos instead of width and height
def rect(win, _px, _py, _w, _h):
	win.vline(_py+1, _px, curses.ACS_VLINE, _h - 1)
	win.hline(_py, _px+1, curses.ACS_HLINE, _w - 1)
	win.hline(_py + _h, _px+1, curses.ACS_HLINE, _w - 1)
	win.vline(_py+1, _px + _w, curses.ACS_VLINE, _h - 1)
	win.addch(_py, _px, curses.ACS_ULCORNER)
	win.addch(_py, _px + _w, curses.ACS_URCORNER)
	win.addch(_py + _h, _px + _w, curses.ACS_LRCORNER)
	win.addch(_py + _h, _px, curses.ACS_LLCORNER)


# Draw the help box
def showHelp(stdscr, _data, _x, _y, _title, _footer, _nbCols, _color):
	baseY = _y
	baseX = _x

	# TODO add X and Y spacing parameters
	# TODO BG color !
	# TODO en faire une classe ...
	# TODO faire des surcharges d'appels, params obsolètes etc

	totalWidth = 0
	maxLenCol = 1
	ind = 0

	if _nbCols > 0:
		_nbLines = ceil(len(_data), _nbCols)
	elif _nbLines == 0:
		_nbLines = len(_data)

	maxLenColsArr = []
	# Find width now if centering needed
	for ind, vv in enumerate(_data):
		# Deducting max width of the column
		lineLen = 1 + len(vv[0]) + 1 + len(vv[1]) + 1
		if lineLen > maxLenCol:
			maxLenCol = lineLen
		if ind > 0 and (((ind + 1) % _nbLines) == 0 or ind == (len(_data) - 1)):
			totalWidth = totalWidth + maxLenCol + 1
			maxLenColsArr.append(maxLenCol)
			maxLenCol = 1

	# Centering calculations
	height, width = stdscr.getmaxyx()
	if _x == -1:
		_x = int((width // 2) - (totalWidth // 2))
		baseX = _x
	if _y == -1:
		_y = int((height // 2) - ceil(_nbLines, 2))
		baseY = _y

	# TODO test si on déborde...et replace pour pas planter

	# Background
	for yy in range(_nbLines):
		for xx in range(totalWidth - 1):
			stdscr.addch(_y + yy + 1, _x + xx + 1, '█', curses.color_pair(8) + curses.A_REVERSE)

	maxLenColInd = 0
	_y = baseY + 1
	for ind, vv in enumerate(_data):
		# Show help info
		stdscr.addstr(_y, _x + 2, vv[0], curses.color_pair(_color) + curses.A_BOLD)
		stdscr.addstr(_y, _x + 4, vv[1])

		# Test exit
		if ind == (len(_data) - 1):
			break

		# End of line
		if ind > 0 and (((ind + 1) % _nbLines) == 0):
			maxLenCol = maxLenColsArr[maxLenColInd]
			if ind <= len(_data) - 2:
				for i in range(_nbLines):
					stdscr.addch(_y - i, _x + maxLenCol + 1, curses.ACS_VLINE, curses.color_pair(_color) + curses.A_BOLD)
			_x = _x + maxLenCol + 1
			_y = baseY + 1
			# _y = _y - (_nbLines - 1)
			maxLenColInd += 1
		else:
			_y += 1

	# Handling title positionning
	# defaut upper left title
	titleX = baseX + 2
	if _title[:3] == "%C%":
		_title = _title[3:]
		titleX = baseX + (totalWidth // 2) - (len(_title) // 2)  # ceil(len(_title), 2)
		if totalWidth % 2 == 0 or len(_title) % 2 != 0:
			titleX = titleX - 1
	elif _title[:3] == "%R%":
		_title = _title[3:]
		titleX = baseX + totalWidth - len(_title) - 2
	elif _title[:3] == "%L%":
		_title = _title[3:]

	# Handling footer positionning
	# default bottom right
	if _footer[:3] == "%C%":
		_footer = _footer[3:]
		footerX = baseX + (totalWidth // 2) - (len(_footer) // 2)  # ceil(len(_footer), 2)
		if totalWidth % 2 == 0 or len(_footer) % 2 != 0:
			footerX = footerX - 1
	elif _footer[:3] == "%L%":
		_footer = _footer[3:]
		footerX = baseX + 2
	elif _footer[:3] == "%R%":
		_footer = _footer[3:]
		footerX = baseX + totalWidth - len(_footer) - 2
	else:
		footerX = baseX + totalWidth - len(_footer) - 2

	# Draw frame
	stdscr.attron(curses.color_pair(_color))
	rect(stdscr, baseX, baseY, totalWidth, _nbLines + 1)
	# rect(stdscr, _x - totalWidth + maxLenColsArr[maxLenColInd] + 1, _y - , totalWidth, _nbLines + 1)
	stdscr.attroff(curses.color_pair(_color))
	# Title
	stdscr.addstr(baseY, titleX, " " + _title + " ", curses.color_pair(_color) + curses.A_BOLD)
	# Footer
	stdscr.addstr(baseY + _nbLines + 1, footerX, " " + _footer + " ", curses.color_pair(6) + curses.A_BOLD)
