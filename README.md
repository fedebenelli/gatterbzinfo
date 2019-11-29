# gatterbzinfo

gatterbzinfo.py v 0.7 (random number lol)

author: Federico E. Benelli aka Ruther
   
This is a work in progress program, that will gatter all the data from different ODF files form Battlezone and then generate json and xlsx files with the gattered data. 
As for now, the gatter of data for ordinances and guns is fully automated, but still some polish needs to be done since the result file is kinda messy. Since it's better standarized, vehicle data is easier to gatter right now I'm not familiar with BZ2/BZCC ODF files, but I guess they have similar format so it could be used there, too

## Requirements

The script is written in Python3 and it uses the Pandas library to export to xlsx files.
The Pandas library can be installed using pip with: 

`pip3 install pandas` or `pip install pandas`

depending on how the command `pip` is defined in the user's PC 

Pandas ain't mandatory for the script to work, if the user wants to just extract the data as json format without installing Pandas it can be done too without any editing.

## Usage

All the ODF files that the user wants to extract the data from must be in a subfolder called "ODFs" at the same folder of the script.
