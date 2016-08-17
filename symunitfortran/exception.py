# -*- coding: utf-8 -*-
"""
**********
Exceptions
**********

Base exceptions and errors for Danata.

"""
__author__ = """Youngsung Kim (grnydawn@gmail.com)"""
#    Copyright (C) 2016 by
#    Youngsung Kim <grnydawn@gmail.com>
#    All rights reserved.
#

# Exception handling

# the root of all Exceptions
class SymUnitException(Exception):
    """Base class for exceptions in SymUnit."""

class SymUnitError(SymUnitException):
    """Exception for a serious error in SymUnit"""
