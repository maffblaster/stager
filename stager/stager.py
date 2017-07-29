# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# See the 'license' file in the base of the package for license information.

# stager - the perfect Gentoo installer
# Copyright 2016-2017 Matthew Marchese, Brad Magyar
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

import sys
import system_information as sysinf
import itertools
import routes
import json

__author__ = 'Matthew Marchese'
__contributors__ = 'Brad Magyar'  # People who have helped go here
__email__ = 'maffblaster@gentoo.org'
__description__ = 'The perfect Gentoo installer'
__url__ = 'https://wiki.gentoo.org/wiki/Project:Installer'
__source__ = 'https://github.com/gentoo/stager'
__copyright__ = '2016-2017'
__version__ = '0.1.0'  # Bump on version release



# Instatiate object containing system info
inf = sysinf.sysinfo()
archrepo = sysinf.repoSelect(inf.machine)
repofile = sysinf.getFilename(archrepo['path'] + '/' + archrepo['textfile'])

# File Urls
tarballUrl = sysinf.getFileUrl(archrepo, repofile, 'tarball')
contentsUrl = sysinf.getFileUrl(archrepo, repofile, 'contents')
digestsUrl = sysinf.getFileUrl(archrepo, repofile, 'digests')
digestsAscUrl = sysinf.getFileUrl(archrepo, repofile, 'digests.asc')

# Disk info
# Two-dimensional array. First index is object, second is array of json-serialized disk data for webpage display
diskObject = sysinf.getDisks()

partList = sysinf.getPartitions(0)

#print(diskObject[1][2]['path'])
'''
for disk in diskObject[1]:
    print("")
#pprint(partThing[0])

jsonDisks = {}

# Creates array of attached disks


for partition in partList:
    #print(partition)
    #print(part)
    #print("Disk: " + str(partition.disk))
    #print("Number: " + str(partition.number))
    #print("Name: " + str(partition.name))
    #print("Path: " + str(partition.path))
    #print("FileSystem: " + str(partition.fileSystem.type) + "\n")
    print('')
'''

# Default data to pass to form template
gentooModel = {
    "stager_options": {
        "autosave_config": bool(0),
        "sync_time": bool(0)
    },
    "sysinfo": {
        "interface": "*",
        "host": inf.hostname,
        "port": 61513,
        "disks": diskObject[1]
    },
    "target": {
        "host_arch": inf.machine,
        "stage": "stage3",
        "locales": {"locale": inf.locale},
        "repo_snapshot": {
            "uri": tarballUrl,
            "md5sum_uri": contentsUrl,
            "gpgsig_uri": digestsUrl
        }
    }
}


class dataclass(object):
    pass

data = dataclass()
data.inf = inf
data.gentooModel = gentooModel

# Application routing
routing = routes.routing.getroute(data)

# Python 3 validator
if sys.version_info <= (3, 0):
    print (__name__ + " requires Python 3.0 and up. Exiting...\n")
    sys.exit(1)

