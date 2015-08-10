from StudyZbosonTruthSherpa211 import *


import os

from optparse import OptionParser

# print "parsing"
# parser = OptionParser()
# parser.add_option("--file"   , help="txt file listing all of your datasets" , default="")
# (options, args) = parser.parse_args()


print "input file"
#inputFile = open(directoryListPhotonStudy.txt, 'r')
inputFile = open('directoryListZbosonStudy.txt', 'r')

for line in inputFile :
    dirname = line.rstrip()

    print os.listdir(dirname)
    rawFileList = os.listdir(dirname)
    fileList = []
    for ifile in rawFileList :
        fileList.append(dirname + '/' + ifile)

    print fileList
    studyZbosonTruth(fileList)
