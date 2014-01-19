#!usr/bin/env python3.3
"""FitLab

Usage:
	fitlab.py (login | logout) <username>
	fitlab.py (-h | --help)
	fitlab.py --version
	fitlab.py csv (sleep | activity | calories) [-hvo FILE]

Options:
	-h --help 			show this help file
	--version 			show version
	-v --verbose		show more text during execution
	-o --output FILE 	specify output file [default: ./fitbit.csv]

"""

from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='FitLab 0.1')
    print(arguments)