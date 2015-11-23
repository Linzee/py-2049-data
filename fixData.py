#!/usr/bin/python
# -*- coding: utf-8 -*-

DATA_PATH = 'data/delays.json'
DATA_PATH_OUT = 'data/delays-out.json'

from optparse import OptionParser
import sys
import json

parser = OptionParser()
parser.add_option("-r", "--remove-train",
                  dest="removeTrain",
                  help="Remove train(s) by name")

parser.add_option("-t", "--twenty-four",
                  dest="twentyFour", action="store_true", default=False,
                  help="Show train(s) with  24 hour delay")

options, optionsValues = parser.parse_args()

# fix console encoding
for option, value in vars(options).iteritems():
    if isinstance(value, basestring):
        setattr(options, option, value.decode(sys.getfilesystemencoding()))
for i in range(0, len(optionsValues)):
    optionsValues[i] = optionsValues[i].decode(sys.getfilesystemencoding())

def processItem(options, item):

    if options.removeTrain:
        if options.removeTrain in item['name']:
            return None

    if options.twentyFour:
        if int(item['delay']) == 1440:
            print item['name']

    return item

with open(DATA_PATH) as file:
    with open(DATA_PATH_OUT, 'a') as outfile:
        for line in file:
            try:
                item = json.loads(line)
                processedItem = processItem(options, item)
                if processedItem:
                    json.dump(processedItem, outfile)
                    outfile.write('\n')
            except ValueError:
                print "Invalid JSON line! ("+line+")"
