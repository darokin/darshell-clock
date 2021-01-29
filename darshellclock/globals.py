# List of main constants

# TODO mettre a 18 en mini mais faire que help tienne dedans
MIN_WIDTH = 18-2#36#18
MIN_HEIGHT = 7

MIN_BIG_WIDTH = 45
MIN_BIG_HEIGHT = 10

# TODO voir pour stocker ailleurs..
CONF_FILEPATH = "./darclock.cfg"

# Not a constant, set after color init
MAX_COLORS = 0 

# ASCII digits, from 0 to 9 plus a : sign at the end for the hour/minute separator
# BIG ASCII DIGITS
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

# SMALL ASCII DIGITS
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

# Help menu
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
