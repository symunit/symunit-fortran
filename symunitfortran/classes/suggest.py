"""Read a source file

"""

import argparse

class Suggest(object):
    def __init__(self, cmd, argv):

        self.mycmd = cmd
        self.mycfg = config.cmdconfig[cmd]

        parser = argparse.ArgumentParser(
            description='Suggests SymUnit directives')
        #parser.add_argument('repository')
        #args = parser.parse_args(sys.argv[2:])
        #print 'Running git fetch, repository=%s' % args.repository

