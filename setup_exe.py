#!/usr/bin/env python

__author__ = 'Clement Moussu'
__author_email__ = 'clement@bittorrent.com'

from setuptools import setup, find_packages
import sys
import py2exe

requires = [ 'httplib2' ]

if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    requires += ['argparse', 'ordereddict']

setup(
    name = 'btc',
    version = '0.1',
    packages = find_packages(),
    author = __author__,
    author_email = __author_email__,
    description = 'command line tool for remote bittorent client control',
    install_requires = requires,
    entry_points = {
        'console_scripts': [
            'btc = btc.btc:main'
        ],
    },
    console=['btc.py'],
    # console=['test.py'],
    # options={"py2exe":  {}}
    options={"py2exe":  {'bundle_files': 1}}
)

'''
set PATH=%PATH%;C:\Python34\
python -m virtualenv .envW34 --system-site-packages
.envW34\Scripts\activate
python setup.py develop
python setup_exe.py py2exe
cp btc-script.py dist\
cp btc.exe dist\

!!NOT WORK
'''

'''
echo "import btc.btc; btc.btc.main()" > btc.py
echo %PATH%
set PATH=%PATH%;C:\Python27\
python -m virtualenv .envW27 --system-site-packages
.envW27\Scripts\activate
python setup.py develop
python setup_exe.py py2exe
mv dist\library.zip dist\library_.zip
unzip dist\library_.zip to dist\library_\
mv dist\library_ dist\library.zip
cp .\btc\* dist\library.zip\btc\
cp python27.dll dist\

WORK!!!
'''
#TODO: make this work without automatically
