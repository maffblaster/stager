# This module mines information from the currently running system
import platform
import locale
import urllib
import psutil
import parted

class sysinf():
    
    def __init__(self):
        # Python
        self.python_version = platform.python_version()
        self.python_version_tuple = platform.python_version_tuple()
        self.python_build = platform.python_build()
        self.python_compiler = platform.python_compiler()
        self.python_branch = platform.python_branch()
        self.python_implementation = platform.python_implementation()
        self.python_revision = platform.python_revision()
        self.python_revision = platform.python_revision()
        self.python_revision = platform.python_revision()
        self.python_revision = platform.python_revision()
        
        # System
        self.processor = platform.processor()
        self.system = platform.system()
        self.hostname = platform.node()  # hostname
        self.machine = platform.machine()  # keyword (arch)
        self.kernel = platform.release()  # kernel
        self.version = platform.version()  
        self.release = platform.release()  
        self.uname = platform.uname()  
        self.system_alias = platform.system_alias(self.system, self.release, self.version)
        self.platform = platform.platform()
        self.architecture = platform.architecture()
        #self.dist = platform.dist()
        
        # C lib
        self.libc_ver = platform.libc_ver()
        
        #locale
        self.locale = locale.getlocale()
        

def repoSelect(opt):
    # Chooses base uri and text file based on architecture
    switcher = {
        "AMD64": { "path": "http://distfiles.gentoo.org/releases/amd64/autobuilds", "textfile": "latest-stage3-amd64.txt" }, 
        "x86_64": { "path": "http://distfiles.gentoo.org/releases/amd64/autobuilds", "textfile": "latest-stage3-amd64.txt" }, 
        "x86": { "path": "http://distfiles.gentoo.org/releases/x86/autobuilds", "textfile": "latest-stage3-i686.txt" }
    }
    return switcher.get(opt, "")

def getFilename(url):
    # Parses url of stage3 tarball from remote txt file
    try:
        doc = urllib.request.urlopen(url).read().decode("utf-8").splitlines()
        return doc[2].split()[0]
    except:
        pass

def getFileUrl(uri, file, filetype):
    # Assembles url of tarball
    if filetype == 'tarball':
        fileurl = uri['path'] + "/" + file
    elif filetype == 'contents':
        fileurl = uri['path'] + "/" + file + '.CONTENTS'
    elif filetype == 'digests':
        fileurl = uri['path'] + "/" + file + '.DIGESTS'
    elif filetype == 'digests.asc':
        fileurl = uri['path'] + "/" + file + '.DIGESTS.asc'
    elif (uri == '') or (file == '') or (filetype == ''):
        fileurl = ' '
    return fileurl

def getDisks():
    try:
        partlist = psutil.disk_partitions(False)
        return partlist
    except:
        pass

def checkParts():
    bah = parted.getDevice("/dev/sdb")
    return bah