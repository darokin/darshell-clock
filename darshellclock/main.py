import datetime
import argparse

from .utils import get_terminal_size
from .cfg import (
	MIN_HEIGHT, MIN_WIDTH
)
from .clock import start

nfoData = r"""
             ___________________
  ┌─────____/   \___   \        \─────────────┐
  │    /   /    /   \   \    \__/ - darokin - │
  │----\_______/\_______/\___/----------------│
  │                                           │
  │ darshellclock v1.1.1                 2021 │
  │ Minimalist terminal digital clock         │
  │                                           │
  │ https://github.com/darokin/darshell-clock │
  └───────────────────────────────────────────┘
"""


class CapitalisedHelpFormatter(argparse.HelpFormatter):
	def add_usage(self, usage, actions, groups, prefix=None):
		if prefix is None:
			prefix = 'Usage: '
		return super(CapitalisedHelpFormatter, self).add_usage(
			usage, actions, groups, prefix)


def init():
	_stopSeconds = 0

	# Argument parsing
	parser = argparse.ArgumentParser(description="In the app, use Q to quit and H to see how to change colors and settings.", add_help=False, formatter_class=CapitalisedHelpFormatter)
	parser._positionals.title = 'Positional arguments'
	parser._optionals.title = 'Optional arguments'
	parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0', help="Show program's version number.")
	parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='No specific arguments, hit "H in while in the app.')
	parser.add_argument("-s", "--stop", type=int, default=0, help="Auto close in <STOP> seconds")
	parser.add_argument("-i", "--info", action="store_true")
	args = parser.parse_args()

	if args.info:
		print(nfoData)
		exit()

	if args.stop > 0:
		_stopSeconds = args.stop

	rows, columns = get_terminal_size()
	if int(rows) < MIN_HEIGHT or int(columns) < MIN_WIDTH:
		print("Need minimum of [" + str(MIN_HEIGHT) + "x" + str(MIN_WIDTH) + "] for ASCII render, your term indicates a [" + str(rows) + "x" + str(columns) + "] resolution ")
		df = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
		print("Time : " + df)
		exit()

	# All is good, launching clock
	start(_stopSeconds)
