import datetime
import argparse

from .utils import get_terminal_size
from .globals import (
	MIN_HEIGHT, MIN_WIDTH, 
	startTime, stopSeconds
)
from .clock import start


class CapitalisedHelpFormatter(argparse.HelpFormatter):
	def add_usage(self, usage, actions, groups, prefix=None):
		if prefix is None:
			prefix = 'Usage: '
		return super(CapitalisedHelpFormatter, self).add_usage(
			usage, actions, groups, prefix)


def init():
	global startTime, stopSeconds
	
	# Argument parsing
	parser = argparse.ArgumentParser(description="In the app, use Q to quit and H to see how to change colors and settings.", add_help=False, formatter_class=CapitalisedHelpFormatter)
	parser._positionals.title = 'Positional arguments'
	parser._optionals.title = 'Optional arguments'
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help="Show program's version number.")
	parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='No specific arguments, hit "H in while in the app.')
	parser.add_argument("-s", "--stop", type=int, help="Auto close in n seconds")
	parser.add_argument("-i", "--info", action="store_true")
	args = parser.parse_args()

	# _VersionAction(option_strings=['-v', '--version'], dest='version', nargs=0, const=None, default='==SUPPRESS==', type=None, choices=None, help="Show program's version number and exit.", metavar=None)
	# _HelpAction(option_strings=['-h', '--help'], dest='help', nargs=0, const=None, default='==SUPPRESS==', type=None, choices=None, help='Q to QUIT / H for HELP box in app', metavar=None)

	if args.info:
		print("Display .nfo file. Not yet available sorry.")
		# open .nfo file
		# nfofile = open("darshellclock.nfo", 'r')
		# nfofile.readlines()
		# nfofile.close()
		# for nfoline in nfofile:
		# print(nfoline)
		exit()

	if args.stop > 0:
		stopSeconds = args.stop
		startTime = datetime.datetime.now().second

	rows, columns = get_terminal_size()
	if int(rows) < MIN_HEIGHT or int(columns) < MIN_WIDTH:
		print("Need minimum of [" + str(MIN_HEIGHT) + "x" + str(MIN_WIDTH) + "] for ASCII render, your term indicates a [" + str(rows) + "x" + str(columns) + "] resolution ")
		df = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
		print("Time : " + df)
		exit()

	# All is good, launching clock
	start()
