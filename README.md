### Requirements
- Pandas
- Gooey

This repository holds scripts for managing goPro video files recorded with a goPro Hero 5 or later model. These models store telemetry data inside of the video file itself. Information on how to use these scripts can be found [here](http://jamesdesmond.org/posts/how-i-merge-gopro-data/)

## [renameByDateModified.py](https://github.com/jamesdesmond/GoPro-Telemetry-Joiner/blob/master/renameByDateModified.py)
This script takes any filetype as input, however it is meant to be used on the original MP4 files from the goPro. These files follow a nonstandard naming scheme which when sorted alphabetically, is not chronological. This is extremely annoying. Instead, the script with rename the files sequentially as "GH##" based on the date-modified parameter on the filesystem.

## [mergeCSV.py](https://github.com/jamesdesmond/GoPro-Telemetry-Joiner/blob/master/mergeCSV.py)
This script will take many CSV's, and based on the alphanumeric sorting of the filenames, will merge the data. Accumulating values like "Distance Travelled" will accumulate properly. 

## [readMP4](https://github.com/jamesdesmond/GoPro-Telemetry-Joiner/blob/master/readMP4.py)
This script when completed will take the original MP4's created by the gopro, rename them properly, strip the telemetry data from the mp4, merge the video files, and then merge the telemetry data files. This will utilize the previous two scripts as well as require ffmpeg libraries to be used, and a library like: https://github.com/stilldavid/gopro-utils
