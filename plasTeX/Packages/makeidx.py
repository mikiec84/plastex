#!/usr/bin/env python

from plasTeX import Command

class see(Command):
    args = 'self page:nox'
    counter = 'see'
    
class seealso(Command):
    args = 'self page:nox'
    counter = 'also'

# Dummy macros to accompany counters above
class thesee(Command):
    unicode = ''

class thealso(Command):
    unicode = ''