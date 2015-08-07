import AthenaPoolCnvSvc.ReadAthenaPool
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
from AthenaCommon.AppMgr import ServiceMgr
from AthenaCommon import CfgMgr

from glob import glob

#filelist = ['/r03/atlas/khoo/Data_2014/DAOD_TRUTH/user.khoo.361047.Sherpa_CT10_SinglePhotonPt140_280_BFilter.DAOD_TRUTH.e3587.030415.v3_EXT0.23956901/user.khoo.5246417.EXT0._000005.DAOD_TRUTH1.test.pool.root']
filelist = ['/data/users/rsmith/mc15_13TeV.361047.Sherpa_CT10_SinglePhotonPt140_280_BFilter.merge.DAOD_TRUTH1.e3587_p2375/DAOD_TRUTH1.05969087._000001.pool.root.1']
#filelist = ['/r03/atlas/khoo/Data_2014/DAOD_TRUTH/mc12_13TeV.177583.Sherpa_CT10_SinglePhotonMassiveCBPt140_280_BFilter.merge.DAOD_TRUTH1.e3083_p2321_tid05193453_00/DAOD_TRUTH1.05193453._000008.pool.root.1']

ServiceMgr.EventSelector.InputCollections = filelist

streamName = 'AnalysisHistoStream'
fileName   = 'PhotonTruth.test.root'
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
histoStream = MSMgr.NewRootStream( streamName, fileName )

# Set up default configurations
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()
# topSequence += CfgMgr.PhotonTruthAlg("Gamma_0_70",
#                                      RootStreamName=streamName,
#                                      RootDirName='/GammaPt0',
#                                      PhotonRef_PtMin=   0e3,PhotonRef_PtMax=   70e3)
# topSequence += CfgMgr.PhotonTruthAlg("Gamma_70_140",
#                                      RootStreamName=streamName,
#                                      RootDirName='/GammaPt70',
#                                      PhotonRef_PtMin=  70e3,PhotonRef_PtMax=  140e3)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_140_280",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt140',
                                     PhotonRef_PtMin= 140e3,
                                     PhotonRef_PtMax= 280e3,
                                     JetRJCut       = 5
                                     )
topSequence += CfgMgr.PhotonTruthAlg("Gamma_280_500",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt280',
                                     PhotonRef_PtMin= 280e3,PhotonRef_PtMax= 500e3)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_500_1000",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt500',
                                     PhotonRef_PtMin= 500e3,PhotonRef_PtMax= 1000e3)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_1000_2000",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt1000',
                                     PhotonRef_PtMin=1000e3,PhotonRef_PtMax=2000e3)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_2000_4000",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt2000',
                                     PhotonRef_PtMin=2000e3,PhotonRef_PtMax=4000e3)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_4000_inf",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt4000',
                                     PhotonRef_PtMin=4000e3,PhotonRef_PtMax=1e9)

#ServiceMgr.MessageSvc.defaultLimit = 9999999
#theApp.EvtMax = 100
theApp.EvtMax = -1
ServiceMgr.EventSelector.SkipEvents = 0

