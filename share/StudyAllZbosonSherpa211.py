import AthenaPoolCnvSvc.ReadAthenaPool
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
from AthenaCommon.AppMgr import ServiceMgr
from AthenaCommon import CfgMgr
from glob import glob

from StudyZbosonTruthSherpa211 import *

import os

from optparse import OptionParser

# print "parsing"
# parser = OptionParser()
# parser.add_option("--file"   , help="txt file listing all of your datasets" , default="")
# (options, args) = parser.parse_args()


print "input file"
#inputFile = open(directoryListPhotonStudy.txt, 'r')
inputFile = open('directoryListZbosonStudy.small.txt', 'r')

for line in inputFile :
    dirname = line.rstrip()

    print os.listdir(dirname)
    rawFileList = os.listdir(dirname)
    fileList = []
    for ifile in rawFileList :
        fileList.append(dirname + '/' + ifile)

    print fileList
    studyZbosonTruth(fileList)

streamName = 'AnalysisHistoStream'# + path.basename(localFileList[0])
fileName   = 'ZbosonTruthTest.small.root'# + path.basename(localFileList[0].split(".")[2]) + '.root'
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
#histoStream = MSMgr.NewRootStream( streamName, 'output/' + fileName )
histoStream = MSMgr.NewRootStream( streamName, 'output/' + fileName)

theApp.EvtMax = 1000

from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()
# topSequence += CfgMgr.ZbosonTruthAlg("Z_0_70",#+path.basename(localFileList[0]).replace(".", ""),
#                                      RootStreamName=streamName,
#                                      RootDirName='/ZPt0',
#                                      ZbosonRef_PtMin=0e3,ZbosonRef_PtMax=70e3
#                                      ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_70_140",#+path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt70',
                                     ZbosonRef_PtMin=70e3,ZbosonRef_PtMax=140e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_140_280",#+path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt140',
                                     ZbosonRef_PtMin=140e3,ZbosonRef_PtMax=280e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_280_500",#+path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt280',
                                     ZbosonRef_PtMin=280e3,ZbosonRef_PtMax=500e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_500_700",#+path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt500',
                                     ZbosonRef_PtMin= 500e3,ZbosonRef_PtMax= 700e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_700_1000",#+path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt700',
                                     ZbosonRef_PtMin= 700e3,ZbosonRef_PtMax= 1000e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_1000_2000",#+path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt1000',
                                     ZbosonRef_PtMin=1000e3,ZbosonRef_PtMax=2000e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_2000_4000",#+path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt2000',
                                     ZbosonRef_PtMin=2000e3,ZbosonRef_PtMax=4000e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_4000_inf",#+path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt4000',
                                     ZbosonRef_PtMin=4000e3,ZbosonRef_PtMax=1e9
                                     ,JetRJCut       = 20)
