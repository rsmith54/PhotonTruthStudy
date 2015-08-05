# Run arguments file auto-generated on Sun May  3 23:18:31 2015 by:
# JobTransform: EVNTtoDAOD
# Version: $Id: trfExe.py 643045 2015-01-30 13:43:56Z graemes $
# Import runArgs class
from PyJobTransforms.trfJobOptions import RunArguments
runArgs = RunArguments()
runArgs.trfSubstepName = 'EVNTtoDAOD' 

runArgs.reductionConf = ['TRUTH1']

# Explicitly added to process all events in this step
runArgs.maxEvents = -1

# Input data
runArgs.inputEVNTFile = ['mc15_13TeV.361054.Sherpa_CT10_SinglePhotonPt1000_2000_CVetoBVeto.evgen.EVNT.e3587_tid04954625_00/EVNT.04954625._000522.pool.root.1']
runArgs.inputEVNTFileType = 'EVNT'
runArgs.inputEVNTFileNentries = 200L

# Output data
runArgs.outputDAOD_TRUTH1File = 'DAOD_TRUTH1.test.pool.root'
runArgs.outputDAOD_TRUTH1FileType = 'aod'

# Extra runargs

# Extra runtime runargs

# Literal runargs snippets
