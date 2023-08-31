import os
import xml.etree.ElementTree as ET
import argparse
from pathlib import Path
import re
from dateutil import parser
from datetime import datetime
import sys
import csv

def parse_xml_file(xml_file_path, filter=None):
    distance=0.0
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    # Since the TCX file has a namespace, we can't search for just things like "Lap" and "DistanceMeters" without including the namespace
    # This extracts the namespace for later use
    ns = re.match(r'{.*}', root.tag).group(0)
    for activity in root[0]:
        # Check to see if the activity matches the filter
        if filter!='' and activity.attrib['Sport']!=filter:
            continue
        lap = activity.find(f'{ns}Lap')
        date = lap.attrib['StartTime']
        distance += float(lap.find(f'{ns}DistanceMeters').text)

    return distance, date

def parse_folder(folder_path, filter, format, output):
    if format=="CSV":
        # Create file and header
        csvfile = open(output, mode='w', newline='')
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Filename","Date","Distance"])
    for filename in os.listdir(folder_path):
        if filename.endswith(".tcx") and filter in filename:
            xml_file_path = os.path.join(folder_path, filename)
            distance, date = parse_xml_file(xml_file_path, filter)
            nicedate=parser.isoparse(date).strftime("%m/%d/%Y")
            if format=="CSV":
                csvwriter.writerow([filename, nicedate, distance])
            elif format=="Text":
                print(f"File: {filename}, NiceDate: {nicedate}, Distance: {distance}")

def main():
    parser = argparse.ArgumentParser(description="A script to extract data from Google Fit TCX Files")
    parser.add_argument("-i", "--input", type=Path, help="Input file path", required=True)
    parser.add_argument("-f", "--filter", type=str, help="Activity filter (Biking, Walking, etc.)", default='')
    parser.add_argument("-o", "--output", type=str, help="Output file name")
    parser.add_argument("-t", "--format", type=str, choices=['CSV', 'Text'], help="Output format", default='Text')
    args = parser.parse_args()
    if args.format!='Text' and args.output is None:
        print("Must include an output file argument when using a non-text format!")
        sys.exit()
    if os.path.exists(args.input):
        parse_folder(args.input, args.filter, args.format, args.output)

if __name__ == "__main__":
    main()
