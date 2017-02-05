# This module mines information from the currently running system

import platform

# python
platform.python_version()

# hardware
platform.processor()

platform.system()
platform.node()  # hostname
platform.machine()  # keyword (arch)
platform.release()  # kernel
platform.version()  #

# Distribution
platform.dist()

# C lib
platform.libc_ver()