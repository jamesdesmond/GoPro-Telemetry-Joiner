# GoPro telemetry splicer

This repository holds scripts for managing GoPro video files recorded with a GoPro Hero 5 or later because the video file metadata contains the telemetry data. 

I wrote a [short article](http://jamesdesmond.org/posts/how-i-merge-gopro-data/) on how to use the scripts within this repository.

## Usage

```python3
pip3 install -r requirements.txt
```

## [renameByDateModified.py](renameByDateModified.py)

| Input              	| Output                                                                                             	|
|--------------------	|----------------------------------------------------------------------------------------------------	|
| n # of video files 	| Files renamed inplace starting with "GH##" based on the date-modified parameter on the filesystem. 	|

## [mergeCSV.py](mergeCSV.py)

| Input       	| Output                                               	|
|-------------	|------------------------------------------------------	|
| n # of CSVs 	| A single CSV that has merged data of the input CSVs. 	|

Values such as `Distance Travelled` will accumulate appropriately.

## [readMP4.py](readMP4.py)

| Input               	| Output                                                                         	|
|---------------------	|--------------------------------------------------------------------------------	|
| n # of `.mp4` files 	| A single file which consists of the merged input video and telemetry metadata. 	|
