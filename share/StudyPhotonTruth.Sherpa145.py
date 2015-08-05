import AthenaPoolCnvSvc.ReadAthenaPool
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
from AthenaCommon.AppMgr import ServiceMgr
from AthenaCommon import CfgMgr

from glob import glob

# filelist = [
# 'DAOD_MCGN1.SinglePhoton.pt35_70.root',
# 'DAOD_MCGN1.SinglePhoton.pt70_140.root',
# 'DAOD_MCGN1.SinglePhoton.pt140_280.root',
# 'DAOD_MCGN1.SinglePhoton.pt280_500.root',
# 'DAOD_MCGN1.SinglePhoton.pt500_1000.root',
# 'DAOD_MCGN1.SinglePhoton.pt1000_2000.root',
# 'DAOD_MCGN1.SinglePhoton.pt2000_4000.root',
# 'DAOD_MCGN1.SinglePhoton.pt4000.root',
# ]
#filelist = ['/r03/atlas/khoo/Data_2014/DAOD_TRUTH/user.khoo.361047.Sherpa_CT10_SinglePhotonPt140_280_BFilter.DAOD_TRUTH.e3587.030415.v3_EXT0.23956901/user.khoo.5246417.EXT0._000005.DAOD_TRUTH1.test.pool.root']
filelist = ['/r03/atlas/khoo/Data_2014/DAOD_TRUTH/mc12_13TeV.177583.Sherpa_CT10_SinglePhotonMassiveCBPt140_280_BFilter.merge.DAOD_TRUTH1.e3083_p2321_tid05193453_00/DAOD_TRUTH1.05193453._000008.pool.root.1']

ServiceMgr.EventSelector.InputCollections = filelist

streamName = 'AnalysisHistoStream'
fileName   = 'PhotonTruth.test.root'
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
histoStream = MSMgr.NewRootStream( streamName, fileName )

# Set up default configurations
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()
topSequence += CfgMgr.PhotonTruthAlg("Gamma_140_280",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt140',
                                     PhotonRef_PtMin= 140e3,PhotonRef_PtMax= 280e3)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_280_500",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt280',
                                     PhotonRef_PtMin= 280e3,PhotonRef_PtMax= 500e3)
topSequence += CfgMgr.PhotonTruthAlg("Gamma_500_inf",
                                     RootStreamName=streamName,
                                     RootDirName='/GammaPt500',
                                     PhotonRef_PtMin= 500e3,PhotonRef_PtMax= 1e9)

#ServiceMgr.MessageSvc.defaultLimit = 9999999
theApp.EvtMax = -1
ServiceMgr.EventSelector.SkipEvents = 0

