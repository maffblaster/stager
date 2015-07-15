#! /usr/bin/env python3

# Stage7 - The perfect Gentoo installer
# Copyright (C) 2015, Matthew Marchese
# License coming...

# Todo: check for python2 and python3.

# Define global variables
__author__ = 'matthew marchese'
__copyright__ = '2015'  # Enter a span of years
__credits__ = 'people who have helped.'

__license__ = 'coming soon...'
__version__ = '0.0.01'
__status__= 'pre-alpha'

__maintainer__ = 'matthew marchese'
__email__ = 'maffblaster@gentoo.org'

__url__ = 'https://wiki.gentoo.org/wiki/Project:Installer'
__source__ = 'https://github.com/gentoo/stager'

# 0 verbosity: normal output to stdout
# 1 verbosity: be chatty (extra output) (--verbose)
# -1 verbosity: no normal output to stdout (--quiet)
verbosity = 0

import argparse

# Imports all stage7 modules in the modules directory
# import modules

# todo Usage: stager --[global-options] subcommand [--subcommand-options <subcommand-arguments>]

parser = argparse.ArgumentParser(prog='stager', add_help=True, formatter_class=argparse.RawDescriptionHelpFormatter, description='stager: the perfect Gentoo installer.',
                                 epilog='\nsubcommands can be shorted:\n\'stager backup -h\' can be reduced to \'stager b -h\'\n\nversion ' + __version__ + ' ' + __status__ + '\n'
                                 'copyright (c) ' + __copyright__ + ', ' + __author__ + '\n' + __url__ + '\n' + __source__)
# They are global options, not arguments
for grp in parser._action_groups:
    if grp.title == 'optional arguments':
        grp.title = 'global-options'

parser.add_argument('-V', '--version', action='version', help='print version information and exit.', version=__version__)
parser.add_argument('-v', '--verbose', action='store_true', default=False, help='be chatty: more data to stdout.')
parser.add_argument('-q', '--quiet', action='store_true', default=False, help='be silent: no data to stdout.')

subparser = parser.add_subparsers(title='subcommands', description='invoke a subcommand for stager to execute.', metavar='subcommand', help='use \'stager subcommand --help\' for detailed options.')

# Create a parser for the install command
parser_install = subparser.add_parser('install', aliases={'i'}, help='install a new system from a profile.')
parser_install.add_argument('-l', '--logfile', dest='logfile', metavar='<logfile.log>', action='store', type=str, default='/tmp/install.log', help='path to the log file (defaults to /tmp/install.log).')
parser_install.add_argument('-p', '--profile', dest='profile', metavar='<profile.ini>', action='store', type=str, help='path the profile.ini file.')

# Create a parser for the backup command
parser_backup = subparser.add_parser('backup', aliases={'b'}, help='create a complete backup of the system.')
parser_backup.add_argument('-c', '--compression-type', dest='compression-type', metavar='<type>', choices=['gz', 'bz2', 'xz', 'lzma'], type=str, help='select a compression type.')
parser_backup.add_argument('-d', '--destination', dest='destination', metavar='<destination>', action='store', type=str, help='path to the backup destination.')
parser_backup.add_argument('-e', '--exclude', dest='exclude', metavar='<file>', action='append', type=str, help='exclude the following files/directories.')
parser_backup.add_argument('--exclude-list', dest='exclude-list', metavar='<exclude.txt>', action='store', type=str, help='path to a new line separated text file containing a list of files/directories to exclude.')
parser_backup.add_argument('-l', '--logfile', dest='logfile', metavar='<logfile.log>', action='store', type=str, default='/tmp/backup.log', help='path to the log file (defaults to /tmp/backup.log).')
parser_backup.add_argument('-n', '--no-compress', dest='no-compress', metavar='<type>', type=str, help='do not compress files with the these extensions.')

# Create a parser for the recovery command
parser_recover = subparser.add_parser('recover', aliases={'r'}, help='recover a system from a stage4 tarball.')
parser_recover.add_argument('-d', '--destination', dest='destination', metavar='<dir>', action='store', type=str, help='path to the recovery destination.')
parser_recover.add_argument('-l', '--logfile', dest='logfile', metavar='<logfile.log>', action='store', type=str, default='/tmp/recover.log', help='path to the log file (defaults to /tmp/recover.log).')
parser_recover.add_argument('-p', '--profile', dest='profile', metavar='<profile.ini>', action='store', type=str, help='path the profile.ini file.')
parser_recover.add_argument('-s', '--source', dest='source', metavar='<dir>', action='store', type=str, help='source of the tarball.')

# Create a parser for the serve command
parser_serve = subparser.add_parser('serve', aliases={'s'}, help='start the http ui.')
parser_serve.add_argument('-l', '--logfile', dest='logfile', metavar='<logfile.log>', action='store', default='/tmp/http-ui.log', type=str, help='path to the log file (defaults to /tmp/http-ui.log)')
parser_serve.add_argument('-P', '--password', dest='password', metavar='<password>', action='store', type=str, help='sets a password for the http interface.')
parser_serve.add_argument('-p', '--profile', dest='profile', metavar='<profile.ini>', action='store', type=str, help='populates the http UI with profile.ini data.')
parser_serve.add_argument('--port', dest='port', metavar='<port>', action='store', default=80, type=int, help='sets the port for the http interface (defaults to 80).')
parser_serve.add_argument('--url', dest='url', metavar='<url>', action='store', default='http://localhost/stager', type=str, help='sets the url for the http interface (defaults to http://localhost/stager).')

args = parser.parse_args()

parser.parse_args(' '.split())

#todo option/argument santity tests
