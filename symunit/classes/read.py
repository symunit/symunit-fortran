"""Read a source file

"""

import argparse

class SURead(object):
    def __init__(self, argv):
        parser = argparse.ArgumentParser(description='Reads a source file')
        #parser.add_argument('--amend', action='store_true')
        parser.add_argument('inputfile', help='Input source file')
        args = parser.parse_args(argv)
        print ('Input source file = %s' % args.inputfile)
