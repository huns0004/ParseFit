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
File: 2023-10-16T14_01_18.713-05_00_PT6M22.809S_Biking.tcx, NiceDate: 10/16/2023, Distance: 850.0007846775779, Seconds: 382.809
File: 2023-10-16T14_07_41.522-05_00_PT27M21.407S_Biking.tcx, NiceDate: 10/16/2023, Distance: 8662.627824145018, Seconds: 1641.407
File: 2023-10-17T12_55_11.358-05_00_PT2H37M5.576S_Biking.tcx, NiceDate: 10/17/2023, Distance: 50681.06278598073, Seconds: 9536.581941471999
```