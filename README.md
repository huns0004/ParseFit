# Parsefit

A script to extract data from Google Fit TCX Files

## Usage
```text
usage: parsefitdata.py [-h] -i INPUT [-f FILTER] [-o OUTPUT] [-t {CSV,Text}]

A script to extract data from Google Fit TCX Files

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file path
  -f FILTER, --filter FILTER
                        Activity filter (Biking, Walking, etc.)
  -o OUTPUT, --output OUTPUT
                        Output file name
  -t {CSV,Text}, --format {CSV,Text}
                        Output format
```

## Requirements

Requirements can be installed by running `pip3 install -r ./requirements.txt`

## Sample Output

```
File: 2023-06-25T10_14_03.336-05_00_PT1H26M30.682S_Biking.tcx, NiceDate: 06/25/2023, Distance: 29748.637312993083
File: 2023-07-02T08_09_08.331-05_00_PT2H16M57.505S_Biking.tcx, NiceDate: 07/02/2023, Distance: 43849.77351833329
File: 2023-07-23T10_10_47.441-05_00_PT1H58M50.898S_Biking.tcx, NiceDate: 07/23/2023, Distance: 35872.04551453308
```