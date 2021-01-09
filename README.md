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
The video frame extraction will take a `.mp4` file or a directory of `.mp4` files and extract each frame or nth frames from them, placing them in a directory. Ensure the output directory is already created before running the function.

| Flag | Description |
|---|---|
| `-h, --help` | show this help message and exit |
| `--start STARTING_COUNT` | Starting video file count, only if perserve file off (default:0) |
| `--prefix FILENAME_PREFIX` | Video file prefix, only if perserve file off (default:video) |
| `--perserve` | Perserve filename will not use prefix or video count, but use original filename with frame number |
| `--vertical` | Flips all images vertically |
| `--horizontal` | Flips all images horizontally |
| `--output OUTPUT, -o OUTPUT` | Output directory, relative or absolute to input (default:output) |
| `--input INPUT, -i INPUT` | Input directory or file, relative or absolute(default:./) |


**Usage**<br>
Please note if you do not specify an input directory or input file will use the current directory you are in. If you do not specify output it will use `./output` relative to your input.
```sh
python video-frame-extraction.py
python video-frame-extraction.py -i videos -o frames -n 20
python video-frame-extraction.py -i video.mp4 -n 20
```