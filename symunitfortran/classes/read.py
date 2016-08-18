"""Read a Fortran source file

"""

import argparse
import config

class Read(object):
    """Read a Fortran source file
    """

    def __init__(self, cmd, argv):
        """Parse command line arguments

        """
        self.mycmd = cmd
        self.mycfg = config.cmdconfig[cmd]

        parser = argparse.ArgumentParser(description='Reads a source file')
        #parser.add_argument('--amend', action='store_true')
        parser.add_argument('inputfile', help='Input source file')
        args = parser.parse_args(argv)

        print ('Input source file = %s' % args.inputfile)
