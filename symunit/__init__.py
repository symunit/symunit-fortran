"""
SymUnit
========

    SymUnit is a Python package for automatically generating unit tests.

    https://symunit.github.com/

Using
-----

    Just write in Python

    T.B.D.
"""
#    Copyright (C) 2016 by
#    Youngsung Kim <grnydawn@gmail.com>
#    All rights reserved.
#
# Add platform dependent shared library path to sys.path
#

#from __future__ import absolute_import, print_function
#from __future__ import absolute_import, print_function

import sys
if sys.version_info[:2] < (2, 7):
    MSG = "Python 2.7 or later is required for SymUnit (%d.%d detected)."
    raise ImportError(MSG % sys.version_info[:2])
del sys

import sys

# Release data
from symunit import release

__author__ = '%s <%s>' % release.AUTHORS['Youngsung']
__license__ = release.LICENSE

__date__ = release.DATE
__version__ = release.VERSION

__bibtex__ = """Not published yet."""

# These are import orderwise
from .exception import *
from .external import *
from .utils import *
from .classes import *

