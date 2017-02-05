# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# See the 'license' file in the base of the package for license information.

# stager - the perfect Gentoo installer
# Copyright 2016-2017, Matthew Marchese
# MIT

#!/usr/bin/env python3

"""stager - the perfect Gentoo installer

Usage:
  stager [ --quiet | --verbose ] [<host>] [<port>]
  stager (-h | --help)
  stager --version

Options:
  -c <file>, --config-file <file>   pass a configuration file (json)
  -l <file>, --logfile <file>       change log location (defaults to /tmp/stager/log.log)
  -h --help                         show this screen.
  -D --debug                        enable debug logging.
  -q --quiet                        be silent: no data to stdout.
  -v --verbose                      be chatty: moar data to stdout
  -V --version                      show version and exit.

"""

from docopt import docopt

import sys

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# todo: set a consistent way to version
__author__ = 'Matthew Marchese'
__contributors__ = ''  # People who have helped go here
__email__ = 'maffblaster@gentoo.org'
__description__ = 'The perfect Gentoo installer'
__url__ = 'https://wiki.gentoo.org/wiki/Project:Installer'
__source__ = 'https://github.com/gentoo/stager'
__copyright__ = '2016-2017'
__version__ = '0.1.0'  # Bump on version release

# Python 3 validator
if sys.version_info <= (3, 0):
    print(__name__ + " requires Python 3.0 and up. Exiting...\n")
    sys.exit(1)

app = Flask(__name__)

@app.route('/')
def welcome():
    print("hello world: meet stager: the perfect Gentoo installer")

@app.route('/auth', methods=['GET', 'POST'])
def login():
    print('auth page')
    error = None
    if request.method == 'POST':
        if request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid authorization key'
        else:
            session['logged_in'] = True
            flash('Session has been authenticated!')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    arguments = docopt(__doc__, version=__version__)
    print(arguments)
