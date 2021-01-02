#
#   Copyright (C) 2020 Sellers Industry - All Rights Reserved
#   Unauthorized copying of this file, via any medium is strictly
#   prohibited. Proprietary and confidential.
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Sat Jan 2 2021
#   file: black-overflow-extraction.py
#   project: Data Manipulation Library
#   purpose: Remove Images w/ high percentage black
#
#


from PIL import Image
import numpy as np
import traceback 
import shutil
import sys
import os


# Settings
COLOR_THRESHHOLD     = 1                                                        # Pixel value that is counted as black
PERCENTAGE_THRESHOLD = 0.10                                                     # if precentage larger is moved
OUTPUT_FOLDER        = "output"                                                 # sub-directory to export to


# Process directory
def processDirectory( dir ):
    ndir = os.path.join( dir, OUTPUT_FOLDER )
    for filename in os.listdir( dir ):
        if filename.endswith( ".jpg" ) or filename.endswith( ".png" ):
            try:
                image  = Image.open( os.path.join( dir, filename ) )
                image  = image.convert( "L" )
                nblack = 0
                width, height = image.size
                for x in range( width ):
                    for y in range( height ):
                        if image.getpixel( ( x, y ) ) < COLOR_THRESHHOLD:
                            nblack += 1
                if ( nblack / float( width * height ) ) > PERCENTAGE_THRESHOLD:
                    shutil.move(
                            os.path.join( dir, filename ),
                            os.path.join( ndir, filename )
                        )
            except:
                traceback.print_exc() 
                print( "Error Processing {}".format( filename ) )


# main thread
# should update to use argument library
def main():
    if len( sys.argv ) > 1:
        processDirectory( os.path.join( os.getcwd(), sys.argv[ 1 ] ) )
    else:
        processDirectory( os.getcwd() )


main()