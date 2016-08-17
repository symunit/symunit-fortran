# Makefile for simple-fortran example

SYMUNIT := ../../bin/symunit
TARGET_SRCFILE := ./src/interpolate.F90


# user provides minimum test direction
# then, the tool analyze the direction and source code
# output: the tool provides a skeleton of further directions
# that user need to provide
analyze:
	@${SYMUNIT} read ${TARGET_SRCFILE}


# at this stage, it is assumed that all required directives are provided
# using the directives, the tool generates test cases that include executable test kernels
generate:

# all test kernels are executed and test result is collected
# test result is produced and saved
test:
