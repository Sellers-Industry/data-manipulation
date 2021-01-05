# Data Manipulation Library
Data Manipulation Programs in Python

<br>

## Back Precentage Removal (PNG/JPG)
This will remove all images that have larger than a specific amount of black. This is used to detect errors cause by cropping images outside the bounds of the image. It will scan a directory that the script is ran from or a relative directory, it will then move all the images that contain a higher precentage of black set by the `PERCENTAGE_THRESHOLD` settings. These images will be moved to a sub directory `/output`. Ensure this directory is already created inside the directory you are scanning before the script is started.

The `COLOR_THRESHHOLD` setting sets what is considered to be black by the system on the scale 0-255. So if the pixel value is lower than the color threshhold number is will be counted as black in the total. If the total amount of black pixels is greater than the `PERCENTAGE_THRESHOLD` times the amount of pixels in the image, the image will be moved to the output sub-directory.

**Usage**<br>
You can either run the script in a current directory or run it in a relalitive directory.
```sh
python black-percentage-removal.py
python black-percentage-removal.py [ directory ]
```

<br>

## File Rename (ALL)
Will rename all files in a specific directory to a numerical file name. Go to the directory you would like to rename all the files in. Then run the script. You can set the `DIR_PATH` which is the path the script will be excicuted in, by default it starts in the directory it is in. The `PREPEND` sets what is put in front of the file name, and `APPEND` is what is added to the end of the filename, not including the extension. The `S_INDEX` is the starting number for the numeral names, by default it is set to zero but you could set it to what ever you want if you want to merge multiple directries later on. The `DIGIT_S` is the amount of digits that will be filled, for example is `DIGIT_S=3` then the number `1` will be represented as `001`.

**Usage**<br>
Will only run in the folder the script in ran in.
```sh
python file-rename.py
```


<br>

## Video Frame Extraction (MP4)
The video frame extraction will take a `.mp4` files in a directory and extract all frames from the videos and place them in the output folder inside the directory that was scanned. The images will be placed in a sub version of the folder selected in the `/output` directory. Ensure this directory is already created inside the directory you are scanning before the script is started. Inside the script you can set a vertical or horizontal flip that will be applied to the image before saving.

Videos will be saved in the following naming schema: `{PREFIX}-{VIDEO_NUM}-{NTH_FRAME_NUM}.jpg`. The nth frame number will be the total number of frames saved, not the amount frames that have been scanned. The Nth setting mods the number of frames. So if you Nth frame is set to 10, every 10th frame will be saved. For example, the first video first frame will be saved as `frame-0-0.jpg` and the 10 frame ( @ Nth=10 ) would be `frame-0-1.jpg`. You can also change the starting `video_num` so instead of starting at `0` it can start anywhere. This features is if you would like to combine multiple later you do not end up with duplicated numbers.


**Usage**<br>
You can either run the script in a current directory or run it in a relalitive directory.
```sh
python video-frame-extraction.py
python video-frame-extraction.py [ directory ]
python video-frame-extraction.py [ directory ] [ Nth frame capture ]
python video-frame-extraction.py [ directory ] [ Nth frame capture ] [ starting video_num ]
```