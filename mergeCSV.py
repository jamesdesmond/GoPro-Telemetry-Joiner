#!/usr/bin/env python3

import argparse
import os
import sys
from pathlib import Path

import pandas as pd
from gooey import Gooey, GooeyParser


@Gooey
def parse_args():
    parser = GooeyParser(
        description="rename selected files sequentially based on date-modified value"
    )
    parser.add_argument("files", help="csv files to merge", widget="MultiFileChooser")
    return parser.parse_args()


def main():
    # TODO: eventually have users select folder of mp4 files which I merge with ffmpeg, then Dashware creates a single csv,
    #  then i read the csv, and if any accumulating value goes down, then I reset it (however be careful of like
    #  Min altitude and how I check these values
    # TODO: https://community.gopro.com/t5/en/GoPro-Camera-File-Naming-Convention/ta-p/390220 is the insane way which GP
    #  names videos, I need to make sure I parse the files in correct order or else data will be all over the place.
    # Got these column names from GoProDataMergeProgram
    parsed_args = parse_args()
    fileList = list(str(parsed_args.files).split(";"))
    cols = [
        "GlobalTime",
        "DateTime",
        "Precision_i",
        "Latitude_i",
        "Longitude_i",
        "Elevation_i",
        "Speed_i",
        "Elevation Meters",
        "Elevation Feet",
        "Total Ascent Meters",
        "Total Descent Meters",
        "Altitude Min Meters",
        "Altitude Max Meters",
        "Total Ascent Feet",
        "Total Descent Feet",
        "Altitude Min Feet",
        "Altitude Max Feet",
        "Speed KPH",
        "Speed MPH",
        "GPS_X",
        "GPS_Y",
        "Distance Feet",
        "Distance Meters",
        "Distance Miles",
        "Distance Kilometers",
        "Heading",
        "GPS AccelGs",
        "GPS LatGs",
        "GPS 2D Gs",
    ]
    acc_cols = [
        "GlobalTime",
        "Total Ascent Meters",
        "Total Descent Meters",
        "Altitude Min Meters",
        "Altitude Max Meters",
        "Total Ascent Feet",
        "Total Descent Feet",
        "Altitude Min Feet",
        "Altitude Max Feet",
        "Distance Feet",
        "Distance Meters",
        "Distance Miles",
        "Distance Kilometers",
    ]
    final_df = pd.DataFrame(columns=cols)
    # path = 'input/csv/'
    # fileList = os.listdir(path)
    for file in fileList:
        print(file)
        with pd.option_context("display.precision", 10):
            temp_df = pd.read_csv(file, float_precision=None)
        for acc_col in final_df[acc_cols]:
            # check if final_df already has a value to add, this is only not true for the first CSV parsed
            if len(final_df[acc_col].index) != 0:
                # save value to add as the last value in each column
                value_to_add = final_df[acc_col].iloc[-1]
                # now we must add value_to_add to temp_df[acc_col]
                temp_df[acc_col] = temp_df[acc_col] + value_to_add
        final_df = final_df.append(temp_df)
    final_df = final_df[cols]
    final_df.to_csv(str(Path(fileList[0]).parent) + "/merged.csv", index=False)


if __name__ == "__main__":
    main()
