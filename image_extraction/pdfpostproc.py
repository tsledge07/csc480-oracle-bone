#!/usr/bin/env python3

'''
Author: Randolph Sapp
Info: Tool to navigate output tree and apply post-processing routines
'''

import glob

for f in glob.glob('*-output/*'):
    print(f)
