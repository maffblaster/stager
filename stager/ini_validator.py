# Copyright (C) 2015  Matthew Marchese
# This module will parse and validate code from profile.ini files.
# License coming...

#todo Create functions that handle the parsing of the profile.ini file

__name__ = 'ini_validator'

import configparser

class INIParser():

    # Create configparser objects
    profile = configparser.ConfigParser()