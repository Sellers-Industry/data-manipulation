#
#   Copyright (C) 2021 Sellers Industry
#   distributed under the MIT License
#
#   author: Evan Sellers <sellersew@gmail.com>
#   date: Fri Jan 1 2021
#   file: video-frame-extraction.py
#   project: Data Manipulation Library
#   purpose: Extract Indivual Frames from MP4 Videos
#
#


import argparse
import traceback
import os
import cv2


# Default Settings
DEFUALT_CAPTURE_NTH       = 10                                                  # capture every Nth frame
DEFAULT_STARTING_NUM      = 0                                                   # start video count from
DEFAULT_PREFIX            = "video"                                             # prefix if perserve off
DEFAULT_FLIP_VERTICAL     = False                                               # vertically flip image
DEFAULT_FLIP_HORIZONTAL   = False                                               # horizontally flip image
DEFAULT_EXPORT_DIRECTORY  = "output"                                            # defualt export folder


"""
    Process File
"""
def processFile( file, video_count, settings ):
    capture    = cv2.VideoCapture( file )
    hasFrame   = True
    countFrame = 0

    while hasFrame:
        hasFrame, frame = capture.read()
        if countFrame % int( settings.nth_frame ) == 0:
            if ( settings.flip_vertical ):
                frame = cv2.flip( frame, 0 )

            if ( settings.flip_horizontal ):
                frame = cv2.flip( frame, 1 )

            if ( settings.perserve_filename ):
                file_prefix = os.path.basename( os.path.splitext( file )[ 0 ] )
            else:
                file_prefix = "{}-{}".format(
                            settings.filename_prefix,
                            video_count
                        )

            filename = "{}-frame-{}.jpg".format( file_prefix, countFrame )
            filepath = os.path.join( settings.output, filename )
            print( filepath )
            cv2.imwrite( filepath, frame )
        countFrame += 1


"""
    Process Directoires
"""
def processDirectory( directory, settings ):
    video_count = settings.starting_count
    for filename in os.listdir( directory ):
        if filename.endswith( ".mp4" ):
            try:
                processFile(
                        os.path.join( directory, filename ),
                        video_count,
                        settings
                    )
                print( "Video {} Completed".format( video_count ) )
            except Exception as e:
                traceback.print_exc() 
                print( "Error Processing {}".format( filename ) )
            video_count += 1


"""
    Main Parsing Arguments
"""
def main():
    parser = argparse.ArgumentParser( description="Extract frames from mp4" )

    # Nth Frame Counter
    parser.add_argument(
                "--frame", "-n",
                dest='nth_frame',
                type=int,
                default=DEFUALT_CAPTURE_NTH,
                help="Extracts every Nth frame (default:{})"
                        .format( DEFUALT_CAPTURE_NTH )
            )

    # Starting frame count
    parser.add_argument(
                "--start",
                dest='starting_count',
                type=int,
                default=DEFAULT_STARTING_NUM,
                help="""Starting video file count, only if perserve
                        file off (default:{})"""
                        .format( DEFAULT_STARTING_NUM )
            )

    # Starting frame count
    parser.add_argument(
                "--prefix",
                dest='filename_prefix',
                type=str,
                default=DEFAULT_PREFIX,
                help="""Video file prefix, only if perserve file
                        off (default:{})"""
                        .format( DEFAULT_PREFIX )
            )

    # Perserve file name
    parser.add_argument(
                "--perserve",
                dest='perserve_filename',
                action='store_true',
                help="""Perserve filename will not use prefix or video
                        count, but use original filename with frame number"""
            )

    # Vertical Flip
    parser.add_argument(
                "--vertical",
                dest='flip_vertical',
                action='store_true',
                help="Flips all images vertically"
            )

    # Horizontal Flip
    parser.add_argument(
                "--horizontal",
                dest='flip_horizontal',
                action='store_true',
                help="Flips all images horizontally"
            )

    # Output Directory
    parser.add_argument(
                "--output", "-o",
                dest='output',
                type=str,
                default=DEFAULT_EXPORT_DIRECTORY,
                help="""Output directory, relative or absolute
                        to input (default:{})"""
                        .format( DEFAULT_EXPORT_DIRECTORY )
            )

    # Input Directory
    parser.add_argument(
                "--input", "-i",
                dest='input',
                type=str,
                default="",
                help="""Input directory or file, relative or 
                        absolute (default:./)"""
            )

    # Splice Arguments
    args = parser.parse_args()

    # Setupt Relative Input & Outputs
    args.input  = os.path.join( os.getcwd(), args.input  )
    args.output = os.path.join( args.input, args.output  )

    # Output not directory
    if not os.path.isdir( args.output ):
        print( "Unable to find output directory: {}".format( args.output ) )
        return

    # Directory Process
    if os.path.isdir( args.input ):
        processDirectory( args.input, args )
        return

    # File process
    if os.path.isfile( args.input ):
        if not os.path.splitext( args.input )[ 1 ]:
            print( "Input file is not of MP4 format: {}".format( args.input ) )
        processFile( args.input, 0, args )
        return

    # Error
    print( "Unable to process input: {}".format( args.output ) )


main()