#
#   Copyright (C) 2020 Sellers Industry - All Rights Reserved
#   Unauthorized copying of this file, via any medium is strictly
#   prohibited. Proprietary and confidential.
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Fri Jan 1 2021
#   file: video-frame-extraction.py
#   project: Data Manipulation Library
#   purpose: Extract Indivual Frames from MP4 Videos
#
#


import cv2
import os
import sys
import traceback 


# Settings
DEFUALT_CAPTURE_NTH  = 10                                                       # default capture every Nth frame
DEFAULT_STARTING_NUM = 0                                                        # default starting filename number
EXPORT_TYPE          = "jpg"                                                    # export file type
EXPORT_PREFIX        = "frame"                                                  # prefix applied to file
VERTICAL_FLIP        = False                                                    # vertically flip the image
HORIZONTAL_FLIP      = False                                                    # horizontally flip the image
OUTPUT_FOLDER        = "output"                                                 # sub-directory to export to


# Capture Video Frame
def captureVideo( videoFile, vidNum, nth, directory ):
    print( videoFile )
    cap = cv2.VideoCapture( videoFile )
    hasFrame = True
    count    = 0
    while hasFrame:
        hasFrame, image = cap.read()
        if count % int( nth ) == 0:
            filename = "{}-{}-{}.{}".format(
                    EXPORT_PREFIX,
                    vidNum,
                    int( count / int( nth ) ),
                    EXPORT_TYPE
                )
            fileD = os.path.join( directory, OUTPUT_FOLDER )
            fileD = os.path.join( fileD, filename )
            if VERTICAL_FLIP:
                image = cv2.flip( image, 0 ) 
            if HORIZONTAL_FLIP:
                image = cv2.flip( image, 1 ) 
            cv2.imwrite( fileD, image )
        count += 1


# Process Directory of Videos
def processDirectory( directory, nth, starting_video_num ):
    video_count = starting_video_num - 1
    for filename in os.listdir( directory ):
        if filename.endswith( ".mp4" ):
            try:
                video_count += 1
                captureVideo(
                        os.path.join( directory, filename ),
                        video_count,
                        nth,
                        directory
                    )
                print( "Video {} Completed".format( video_count ) )
            except Exception as e:
                traceback.print_exc() 
                print( e )
                print( "Error Processing {}".format( filename ) )


# Process Arguments
# should update to use argument library
def main():
    if len( sys.argv ) is 1:
        processDirectory(
                os.getcwd(),
                DEFUALT_CAPTURE_NTH,
                DEFAULT_STARTING_NUM
            )
        return
    if len( sys.argv ) is 2:
        processDirectory(
                os.path.join( os.getcwd(), sys.argv[ 1 ] ),
                DEFUALT_CAPTURE_NTH,
                DEFAULT_STARTING_NUM
            )
        return
    if len( sys.argv ) is 3:
        processDirectory(
                os.path.join( os.getcwd(), sys.argv[ 1 ] ),
                sys.argv[ 2 ],
                DEFAULT_STARTING_NUM
            )
        return
    if len( sys.argv ) is 4:
        processDirectory(
                os.path.join( os.getcwd(), sys.argv[ 1 ] ),
                sys.argv[ 2 ],
                sys.argv[ 3 ],
            )
        return


main()