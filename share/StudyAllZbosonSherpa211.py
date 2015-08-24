import AthenaPoolCnvSvc.ReadAthenaPool
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
from AthenaCommon.AppMgr import ServiceMgr
from AthenaCommon import CfgMgr
from glob import glob

from StudyZbosonTruthSherpa211 import *

import os

from optparse import OptionParser

# print "input file"
# inputFile = open('directoryListZbosonStudy.txt', 'r')

# for line in inputFile :
#     dirname = line.rstrip()

#     print os.listdir(dirname)
#     rawFileList = os.listdir(dirname)
#     fileList = []
#     for ifile in rawFileList :
#         fileList.append(dirname + '/' + ifile)

#     print fileList
#     studyZbosonTruth(fileList)

#ServiceMgr.EventSelector.InputCollections += localFileList
filelist = ['/data/users/rsmith/mc15_13TeV.361449.Sherpa_CT10_Znunu_Pt70_140_BFilter.merge.DAOD_TRUTH1.e3651_p2375/DAOD_TRUTH1.05969994._000001.pool.root.1']
ServiceMgr.EventSelector.InputCollections = filelist


streamName = 'AnalysisHistoStream'
fileName   = 'ZbosonTruthTest.alllarge.root'
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
histoStream = MSMgr.NewRootStream( streamName, 'output/' + fileName)

#theApp.EvtMax = 500
#theApp.EvtMax = 100000

from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()
topSequence += CfgMgr.ZbosonTruthAlg("Z_0_70",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt0',
                                     ZbosonRef_PtMin=0e3,ZbosonRef_PtMax=70e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_70_140",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt70',
                                     ZbosonRef_PtMin=70e3,ZbosonRef_PtMax=140e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_140_280",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt140',
                                     ZbosonRef_PtMin=140e3,ZbosonRef_PtMax=280e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_280_500",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt280',
                                     ZbosonRef_PtMin=280e3,ZbosonRef_PtMax=500e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_500_700",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt500',
                                     ZbosonRef_PtMin= 500e3,ZbosonRef_PtMax= 700e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_700_1000",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt700',
                                     ZbosonRef_PtMin= 700e3,ZbosonRef_PtMax= 1000e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_1000_2000",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt1000',
                                     ZbosonRef_PtMin=1000e3,ZbosonRef_PtMax=2000e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_2000_4000",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt2000',
                                     ZbosonRef_PtMin=2000e3,ZbosonRef_PtMax=4000e3
                                     ,JetRJCut       = 20)
topSequence += CfgMgr.ZbosonTruthAlg("Z_4000_inf",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt4000',
                                     ZbosonRef_PtMin=4000e3,ZbosonRef_PtMax=1e9
                                     ,JetRJCut       = 20)
