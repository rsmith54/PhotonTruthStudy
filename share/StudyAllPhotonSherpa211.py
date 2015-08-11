from StudyPhotonTruthSherpa211 import *


import os

from optparse import OptionParser

# print "parsing"
# parser = OptionParser()
# parser.add_option("--file"   , help="txt file listing all of your datasets" , default="")
# (options, args) = parser.parse_args()


print "input file"
#inputFile = open(directoryListPhotonStudy.txt, 'r')
inputFile = open('directoryListPhotonStudy.txt', 'r')

for line in inputFile :
    dirname = line.rstrip()

    print os.listdir(dirname)
    rawFileList = os.listdir(dirname)
    fileList = []
    for ifile in rawFileList :
        fileList.append(dirname + '/' + ifile)

    print fileList
    studyPhotonTruth(fileList)

streamName = 'AnalysisHistoStream'# + path.basename(localFileList[0])

topSequence = AlgSequence()
topSequence += CfgMgr.PhotonTruthAlg("Gamma_35_70",# + path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt35',
                                     PhotonRef_PtMin=   35e3,
                                     PhotonRef_PtMax=   70e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_70_140",# + path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt70',
                                     PhotonRef_PtMin=  70e3,PhotonRef_PtMax=  140e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_140_280",# + path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt140',
                                     PhotonRef_PtMin= 140e3,
                                     PhotonRef_PtMax= 280e3,
                                     JetRJCut       = 20
                                     )
topSequence += CfgMgr.PhotonTruthAlg("Gamma_280_500",# + path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt280',
                                     PhotonRef_PtMin= 280e3,PhotonRef_PtMax= 500e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_500_1000",# + path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt500',
                                     PhotonRef_PtMin= 500e3,PhotonRef_PtMax= 1000e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_1000_2000",# + path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt1000',
                                     PhotonRef_PtMin=1000e3,PhotonRef_PtMax=2000e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_2000_4000",# + path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt2000',
                                     PhotonRef_PtMin=2000e3,PhotonRef_PtMax=4000e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_4000_inf",# + path.basename(localFileList[0]).replace(".", ""),
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt4000',
                                     PhotonRef_PtMin=4000e3,PhotonRef_PtMax=1e9,
                                     JetRJCut       = 20)
