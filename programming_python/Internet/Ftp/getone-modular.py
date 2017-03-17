#!/usr/local/bin/python
"""
A Python script to download and play a media file by FTP.
Uses getfile.py, a utility module which encapsulates FTP step.
"""

from getpass import getpass

import getfile

filename = 'monkeys.jpg'

# fetch with utility
getfile.getfile(file=filename,
                site='ftp.rmi.net',
                dir='.',
                user=('lutz', getpass('Pswd?')),
                refetch=True)

# rest is the same
if input('Open file?') in ['Y', 'y']:
    from PP4E.System.Media.playfile import playfile

    playfile(filename)
