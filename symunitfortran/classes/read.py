"""Read a Fortran source file

"""

import argparse
import config
import danatacppwrapper as dcw

class Read(object):
    """Read a Fortran source file
    """

    def __init__(self, cmd, argv):
        """Perform read command

        """
        self.mycmd = cmd
        self.mycfg = config.cmdconfig[cmd]

        parser = argparse.ArgumentParser(description='Reads a source file')
        #parser.add_argument('-D', dest='macros', action='append', help='preprocessing macros')
        #parser.add_argument('-I', dest='includes', action='append', help='preprocessing include paths')
        #parser.add_argument('inputfile', help='Input source file')
        args, cppargs = parser.parse_known_args(argv)

        # Preprocess input Fortran source file
        G = dcw.read(cppargs)
        for n, a in G.node.items():
            print(a['linenum'], str(n))

        # parse fortran
        G = self.parse_fortran(G)

        # parse symunit-fortran directives
        G = self.parse_suf_directives(G)

        return G

    def parse_fortran(self, prep):
        """Parse Fortran source file

        """
        pass

    def parse_suf_directives(self, fort):
        """Parse SymUnit-Fortran directives

        """

        pass

