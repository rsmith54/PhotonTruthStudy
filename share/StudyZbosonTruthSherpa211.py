import AthenaPoolCnvSvc.ReadAthenaPool
from AthenaCommon.AthenaCommonFlags import athenaCommonFlags
from AthenaCommon.AppMgr import ServiceMgr
from AthenaCommon import CfgMgr

from glob import glob
from AthenaCommon.AlgSequence import AlgSequence
from OutputStreamAthenaPool.MultipleStreamManager import MSMgr

from AthenaCommon.AppMgr import theApp

def studyZbosonTruth(filelist = None) :
    if filelist == None :
#        filelist = ['/data/users/rsmith/mc15_13TeV.407168.Sherpa_CT10_Znunu_LO_Pt70_140_BFilter.merge.DAOD_TRUTH1.e4105_p2375/DAOD_TRUTH1.05970499._000001.pool.root.1']
        filelist = ['/data/users/rsmith/mc15_13TeV.407171.Sherpa_CT10_Znunu_LO_Pt140_280_BFilter.merge.DAOD_TRUTH1.e4105_p2375/DAOD_TRUTH1.05970514._000001.pool.root.1']

    print filelist
#filelist = ["/r03/atlas/khoo/Data_2014/DAOD_TRUTH/user.khoo.167820.Sherpa_CT10_ZnunuMassiveCBPt140_280_CVetoBVeto.DAOD_TRUTH.e2798.080415.v1_EXT0//user.khoo.5272457.EXT0._000014.DAOD_TRUTH1.test.pool.root"]
    ServiceMgr.EventSelector.InputCollections = filelist


    from os import path

    streamName = 'AnalysisHistoStream' + path.basename(filelist[0])
    fileName   = 'ZbosonTruth.' + path.basename(filelist[0].split(".")[2]) + '.root'

    histoStream = MSMgr.NewRootStream( streamName, 'output/' + fileName )

    # Set up default configurations
    from AthenaCommon.AlgSequence import AlgSequence
    topSequence = AlgSequence()
    topSequence += CfgMgr.ZbosonTruthAlg("Z_0_70" + path.basename(filelist[0]).replace(".", ""),
                                         RootStreamName=streamName,
                                         RootDirName='/ZPt0',
                                         ZbosonRef_PtMin=0e3,ZbosonRef_PtMax=70e3
                                         ,JetRJCut       = 20)
    # topSequence += CfgMgr.ZbosonTruthAlg("Z_70_140" + path.basename(filelist[0]).replace(".", ""),
    #                                      RootStreamName=streamName,
    #                                      RootDirName='/ZPt70',
    #                                      ZbosonRef_PtMin=70e3,ZbosonRef_PtMax=140e3
    #                                      ,JetRJCut       = 20)
    # topSequence += CfgMgr.ZbosonTruthAlg("Z_140_280" + path.basename(filelist[0]).replace(".", ""),
    #                                      RootStreamName=streamName,
    #                                      RootDirName='/ZPt140',
    #                                      ZbosonRef_PtMin=140e3,ZbosonRef_PtMax=280e3
    #                                      ,JetRJCut       = 20)
    # topSequence += CfgMgr.ZbosonTruthAlg("Z_280_500" + path.basename(filelist[0]).replace(".", ""),
    #                                      RootStreamName=streamName,
    #                                      RootDirName='/ZPt280',
    #                                      ZbosonRef_PtMin=280e3,ZbosonRef_PtMax=500e3
    #                                      ,JetRJCut       = 20)
    # topSequence += CfgMgr.ZbosonTruthAlg("Z_500_700" + path.basename(filelist[0]).replace(".", ""),
    #                                      RootStreamName=streamName,
    #                                      RootDirName='/ZPt500',
    #                                      ZbosonRef_PtMin= 500e3,ZbosonRef_PtMax= 700e3
    #                                      ,JetRJCut       = 20)
    # topSequence += CfgMgr.ZbosonTruthAlg("Z_700_1000" + path.basename(filelist[0]).replace(".", ""),
    #                                      RootStreamName=streamName,
    #                                      RootDirName='/ZPt700',
    #                                      ZbosonRef_PtMin= 700e3,ZbosonRef_PtMax= 1000e3
    #                                      ,JetRJCut       = 20)
    # topSequence += CfgMgr.ZbosonTruthAlg("Z_1000_2000" + path.basename(filelist[0]).replace(".", ""),
    #                                      RootStreamName=streamName,
    #                                      RootDirName='/ZPt1000',
    #                                      ZbosonRef_PtMin=1000e3,ZbosonRef_PtMax=2000e3
    #                                      ,JetRJCut       = 20)
    # topSequence += CfgMgr.ZbosonTruthAlg("Z_2000_4000" + path.basename(filelist[0]).replace(".", ""),
    #                                      RootStreamName=streamName,
    #                                      RootDirName='/ZPt2000',
    #                                      ZbosonRef_PtMin=2000e3,ZbosonRef_PtMax=4000e3
    #                                      ,JetRJCut       = 20)
    # topSequence += CfgMgr.ZbosonTruthAlg("Z_4000_inf" + path.basename(filelist[0]).replace(".", ""),
    #                                      RootStreamName=streamName,
    #                                      RootDirName='/ZPt4000',
    #                                      ZbosonRef_PtMin=4000e3,ZbosonRef_PtMax=1e9
    #                                      ,JetRJCut       = 20)

if __name__ == '__main__':
    # test1.py executed as script
    # do something
#   theApp.EvtMax = 100
#    ServiceMgr.EventSelector.SkipEvents = 0

    studyZbosonTruth() #using a default filename


