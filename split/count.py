import json
from argparse import ArgumentParser

# do argument parser
parser = ArgumentParser()
parser.add_argument("file", help="Input your data file")
parser.add_argument("-c", "--count", help="Filter data greater than or equal to this number ", dest="count", default="30")
args = parser.parse_args()

# initial
result = {}
content = []

with open(args.file) as csv:
    for line in csv:
        lineSplit = line.split()
        loc = "["+lineSplit[3]+","+lineSplit[4]+"]"
        # count times by location
        if result.get(loc) == None:
            result[loc] = 1
        else:
            result[loc] += 1

count = 1
# output json format
with open('C'+args.file+'.json', 'w') as fp:
    print("{", end="\n",file=fp)
    print("'time' : "+args.file, end=",\n", file=fp)
    print("'locationCount' : [", end=" ", file=fp)
    for key, value in result.items():
        if count == len(result):
            item = key[1:-1].split(',')
            print("[" + item[0] + "," + item[1] + "," + str(value) + "]", end="", file=fp)
        elif value > int(args.count):
            item = key[1:-1].split(',')
            print("[" + item[0] + "," + item[1] + "," + str(value) + "]", end=",", file=fp)
        count += 1 
    print("]\n}", file=fp)
