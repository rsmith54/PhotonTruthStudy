import AthenaPoolCnvSvc.ReadAthenaPool
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
from AthenaCommon.AppMgr import ServiceMgr
from AthenaCommon import CfgMgr

from glob import glob
filelist = ["/r03/atlas/khoo/Data_2014/DAOD_TRUTH/user.khoo.167820.Sherpa_CT10_ZnunuMassiveCBPt140_280_CVetoBVeto.DAOD_TRUTH.e2798.080415.v1_EXT0//user.khoo.5272457.EXT0._000014.DAOD_TRUTH1.test.pool.root"]
ServiceMgr.EventSelector.InputCollections = filelist

streamName = 'AnalysisHistoStream'
fileName   = 'ZbosonTruth.root'
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr
histoStream = MSMgr.NewRootStream( streamName, fileName )

# Set up default configurations
from AthenaCommon.AlgSequence import AlgSequence
topSequence = AlgSequence()
topSequence += CfgMgr.ZbosonTruthAlg("Z_140_280",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt140',
                                     ZbosonRef_PtMin=140e3,ZbosonRef_PtMax=280e3)
topSequence += CfgMgr.ZbosonTruthAlg("Z_280_500",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt280',
                                     ZbosonRef_PtMin=280e3,ZbosonRef_PtMax=500e3)
topSequence += CfgMgr.ZbosonTruthAlg("Z_500_700",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt500',
                                     ZbosonRef_PtMin= 500e3,ZbosonRef_PtMax= 700e3)
topSequence += CfgMgr.ZbosonTruthAlg("Z_700_1000",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt700',
                                     ZbosonRef_PtMin= 700e3,ZbosonRef_PtMax= 1000e3)
topSequence += CfgMgr.ZbosonTruthAlg("Z_1000_2000",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt1000',
                                     ZbosonRef_PtMin=1000e3,ZbosonRef_PtMax=2000e3)
topSequence += CfgMgr.ZbosonTruthAlg("Z_2000_4000",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt2000',
                                     ZbosonRef_PtMin=2000e3,ZbosonRef_PtMax=4000e3)
topSequence += CfgMgr.ZbosonTruthAlg("Z_4000_inf",
                                     RootStreamName=streamName,
                                     RootDirName='/ZPt4000',
                                     ZbosonRef_PtMin=4000e3,ZbosonRef_PtMax=1e9)

#ServiceMgr.MessageSvc.defaultLimit = 9999999
theApp.EvtMax = -1
ServiceMgr.EventSelector.SkipEvents = 0

