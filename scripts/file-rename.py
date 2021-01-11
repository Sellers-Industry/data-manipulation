#
#   Copyright (C) 2021 Sellers Industry
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Tue Jan 05 2021
#   file: file-rename.py
#   project: Data Manipulation Library
#   purpose: Mass File Rename werwerj.png => img_0.png
#
#

import os, re


# Settings
DIR_PATH = os.getcwd()                                                          # directory to scan
PREPEND  = "img_"                                                               # add to start of file
APPEND   = ""                                                                   # add to end of file
S_INDEX  = 0                                                                    # starting index
DIGIT_S  = 3                                                                    # amout of digits to fill


# Scan Directory
index = S_INDEX
for file in os.listdir( DIR_PATH ):
    old_file = os.path.join( path, file )
    new_file = PREPEND + str( n ).zfill( DIGIT_S ) + os.path.splitext( old_file )[ 1 ] ) + APPEND
    os.rename( old_file, new_file )