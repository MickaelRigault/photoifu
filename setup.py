#! /usr/bin/env python
#

DESCRIPTION = "photoifu"
LONG_DESCRIPTION = """ Project Photometric images inside IFU and play with that"""

DISTNAME = 'photoifu'
AUTHOR = 'Mickael Rigault'
MAINTAINER = 'Mickael Rigault' 
MAINTAINER_EMAIL = 'm.rigault@ipnl.in2p3.fr'
URL = 'https://github.com/MickaelRigault/photoifu/'
LICENSE = 'Apache 2.0'
DOWNLOAD_URL = 'https://github.com/MickaelRigault/photoifu/tarball/0.1'
VERSION = '0.1.0'

try:
    from setuptools import setup, find_packages
    _has_setuptools = False
except ImportError:
    from distutils.core import setup


def check_dependencies():
    install_requires = []

    # Just make sure dependencies exist, I haven't rigorously
    # tested what the minimal versions that will work are
    # (help on that would be awesome)

    try:
        import propobject
    except ImportError:
        install_requires.append('propobject')

    try:
        import pymage
        # Only for panstarrs
    except ImportError:
        install_requires.append('pymage')
        
    try:
        import pixelproject
    except ImportError:
        install_requires.append('pixelproject')


    try:
        import pandas
    except ImportError:
        install_requires.append('pandas')


    return install_requires

if __name__ == "__main__":

    install_requires = check_dependencies()

    if _has_setuptools:
        packages = find_packages()
        print(packages)
    else:
        # This should be updated if new submodules are added
        packages = ['photoifu']

        
    setup(name=DISTNAME,
          author=AUTHOR,
          author_email=MAINTAINER_EMAIL,
                    
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license=LICENSE,
          url=URL,
          version=VERSION,
          download_url=DOWNLOAD_URL,
          install_requires=install_requires,
          scripts=[],
          packages=packages,
          include_package_data=True,
         # package_data={'sedmanalysis': []},
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3.5',              
              'License :: OSI Approved :: BSD License',
              'Topic :: Scientific/Engineering :: Astronomy',
              'Operating System :: POSIX',
              'Operating System :: Unix',
              'Operating System :: MacOS'],
      )
