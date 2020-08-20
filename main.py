import os
import pandas as pd

# Got these column names from GoProDataMergeProgram
cols = ['GlobalTime','DateTime','Precision_i','Latitude_i','Longitude_i','Elevation_i','Speed_i','Elevation Meters','Elevation Feet','Total Ascent Meters','Total Descent Meters','Altitude Min Meters','Altitude Max Meters','Total Ascent Feet','Total Descent Feet','Altitude Min Feet','Altitude Max Feet','Speed KPH','Speed MPH','GPS_X','GPS_Y','Distance Feet','Distance Meters','Distance Miles','Distance Kilometers','Heading','GPS AccelGs','GPS LatGs','GPS 2D Gs']
acc_cols = ['GlobalTime','Total Ascent Meters','Total Descent Meters','Altitude Min Meters','Altitude Max Meters','Total Ascent Feet','Total Descent Feet','Altitude Min Feet','Altitude Max Feet','Distance Feet','Distance Meters','Distance Miles','Distance Kilometers']
final_df = pd.DataFrame(columns=cols)
path = 'input/'
fileList = os.listdir(path)
for file in fileList:
    with pd.option_context('display.precision', 10):
        temp_df = pd.read_csv(path + file, float_precision=None)
    for acc_col in final_df[acc_cols]:
        # check if final_df already has a value to add, this is only not true for the first CSV parsed
        if len(final_df[acc_col].index) != 0:
            # save value to add as the last value in each column
            value_to_add = final_df[acc_col].iloc[-1]
            # now we must add value_to_add to temp_df[acc_col]
            temp_df[acc_col] = temp_df[acc_col] + value_to_add
    final_df = final_df.append(temp_df)
final_df = final_df[cols]
final_df.to_csv('merged_output.csv', index=False)
