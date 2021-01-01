# Data Manipulation Library
Data Manipulation Programs in Python

<br>

## Video Frame Extraction
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