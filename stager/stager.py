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
# todo: set a consistent way to version
__author__ = 'Matthew Marchese'
__contributors__ = 'Brad Magyar'  # People who have helped go here
__email__ = 'maffblaster@gentoo.org'
__description__ = 'The perfect Gentoo installer'
__url__ = 'https://wiki.gentoo.org/wiki/Project:Installer'
__source__ = 'https://github.com/gentoo/stager'
__copyright__ = '2016-2017'
__version__ = '0.1.0'  # Bump on version release

from docopt import docopt

import sys
import system_information as sysinf
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

# Instatiate object containing system info
inf = sysinf.sysinf()
archrepo = sysinf.repoSelect(inf.machine)
repofile = sysinf.getFilename(archrepo['path'] + '/' + archrepo['textfile'])

# File Urls
tarballUrl = sysinf.getFileUrl(archrepo, repofile, 'tarball')
contentsUrl = sysinf.getFileUrl(archrepo, repofile, 'contents')
digestsUrl = sysinf.getFileUrl(archrepo, repofile, 'digests')
digestsAscUrl = sysinf.getFileUrl(archrepo, repofile, 'digests.asc')

# Default data to pass to form template
gentooModel = { 
    "interface": "*", 
    "host": inf.hostname, 
    "port": 61513, 
    "target": {
        "stage": "stage3",
        "locales": {"locale": inf.locale},
        "repo_snapshot": {
            "uri": tarballUrl,
            "md5sum_uri": contentsUrl,
            "gpgsig_uri": digestsUrl
        }
    }
}

# Python 3 validator
if sys.version_info <= (3, 0):
    print (__name__ + " requires Python 3.0 and up. Exiting...\n")
    sys.exit(1)

# Instantiate Flask app
app = Flask(__name__, static_url_path='/static')

# Routing
#   Root
@app.route('/')
def welcome():
    print ("hello world: meet stager: the perfect Gentoo installer")

#   Gentoo Form
@app.route('/form')
def formtest():
    return render_template('formtemplate.html', sysinf=inf, gentooModel=gentooModel)

#    Auth
@app.route('/auth', methods=['GET', 'POST'])
def login():
    print ('auth page')
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
    print (arguments)

# Run app
app.run(debug=True)
