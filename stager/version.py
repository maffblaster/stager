
def get_version():
    # Define version variables
    v = dict(
    __name__ = 'stager', # Script name
    __author__ = 'matthew marchese', # Add authors
    __copyright__ = '2015',  # Enter a span of years.
    __credits__ = '', # People who have helped go here.

    __license__ = 'To be determined...',
    __version__ = '0.0.1',
    __status__= 'pre-alpha',

    __maintainer__ = 'matthew marchese',
    __email__ = 'maffblaster@gentoo.org',

    __url__ = 'https://wiki.gentoo.org/wiki/Project:Installer',
    __source__ = 'https://github.com/gentoo/stager')

    return v

if __name__ == '__main__':
  get_version()