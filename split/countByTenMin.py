import json
from argparse import ArgumentParser

# do argument parser
parser = ArgumentParser()
parser.add_argument("file", help="Input your data file")
parser.add_argument("-c", "--count", help="Filter data greater than or equal to this number ", dest="count", default="30")
args = parser.parse_args()

# initial
interval = {}
result = {}
fileName = []
for time in ["00", "10", "20", "30", "40", "50"]:
    fileName.append(args.file + time)
    interval[(args.file + time)] = {}

with open(args.file) as csv:
    for line in csv:
        lineSplit = line.split()
        loc = "["+lineSplit[3]+","+lineSplit[4]+"]"
        begin = int(lineSplit[1].split(':')[1])/10
        end = int(lineSplit[2].split(':')[1])/10
        for time in ["00", "10", "20", "30", "40", "50"]:
            if int(begin) <= int(time)/10 and  int(time)/10 <= int(end):
                if interval[(args.file + time)].get(loc) == None:
                    interval[(args.file + time)][loc] = 1
                else:
                    interval[(args.file + time)][loc] += 1

# output json format
for name in fileName:
    count = 1
    with open('C'+name+'.json', 'w') as fp:
        print("{", end="\n",file=fp)
        print("'time' : "+name, end=",\n", file=fp)
        print("'locationCount' : [", end=" ", file=fp)
        for key, value in interval[name].items():
            if count == len(interval[name]):
                item = key[1:-1].split(',')
                print("[" + item[0] + "," + item[1] + "," + str(value) + "]", end="", file=fp)
            elif value > int(args.count):
                item = key[1:-1].split(',')
                print("[" + item[0] + "," + item[1] + "," + str(value) + "]", end=",", file=fp)
            count += 1 
        print("]\n}", file=fp)
