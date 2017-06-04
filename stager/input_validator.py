# Copyright (C) 2015  Matthew Marchese
# This module will parse and validate code from various UIs.

# License coming...

__name__ = 'input_validator'

import fileinput

# 0 verbosity: normal output to stdout
# 1 verbosity: be chatty (extra output) (--verbose)
# -1 verbosity: no normal output to stdout (--quiet)
verbosity = 0

# Verbosity is -1 when --quiet is called.

class CLIParser():

    def set_verbosity(v):
        if v.quiet == True:
            verbosity = -1
        else:
           verbosity = v.verbosity


    def get_verbosity(v):
        return verbosity