import AthenaPoolCnvSvc.ReadAthenaPool
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
from AthenaCommon.AppMgr import ServiceMgr
from AthenaCommon import CfgMgr
from glob import glob

import os

from optparse import OptionParser

filelist = ["/data/users/rsmith/mc15_13TeV.361060.Sherpa_CT10_SinglePhotonPt4000_CVetoBVeto.merge.DAOD_TRUTH1.e3587_p2375/DAOD_TRUTH1.05969136._000001.pool.root.1",
]`
ServiceMgr.EventSelector.InputCollections = filelist

streamName = 'AnalysisHistoStream'
fileName   = 'Photon.segfault.root'
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
histoStream = MSMgr.NewRootStream( streamName, fileName)

#theApp.EvtMax = 50000

from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()
topSequence += CfgMgr.PhotonTruthAlg("Gamma_35_70",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt35',
                                     PhotonRef_PtMin=   35e3,
                                     PhotonRef_PtMax=   70e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_70_140",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt70',
                                     PhotonRef_PtMin=  70e3,PhotonRef_PtMax=  140e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_140_280",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt140',
                                     PhotonRef_PtMin= 140e3,
                                     PhotonRef_PtMax= 280e3,
                                     JetRJCut       = 20
                                     )
topSequence += CfgMgr.PhotonTruthAlg("Gamma_280_500",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt280',
                                     PhotonRef_PtMin= 280e3,PhotonRef_PtMax= 500e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_500_1000",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt500',
                                     PhotonRef_PtMin= 500e3,PhotonRef_PtMax= 1000e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_1000_2000",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt1000',
                                     PhotonRef_PtMin=1000e3,PhotonRef_PtMax=2000e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_2000_4000",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt2000',
                                     PhotonRef_PtMin=2000e3,PhotonRef_PtMax=4000e3,
                                     JetRJCut       = 20)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_4000_inf",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt4000',
                                     PhotonRef_PtMin=4000e3,PhotonRef_PtMax=1e9,
                                     JetRJCut       = 20)
