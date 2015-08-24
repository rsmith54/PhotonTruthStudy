import subprocess, datetime, os
from datasets import *

attempt='v1'
date = datetime.datetime.now()
suffix = '{dd:02d}{mm:02d}{yy:02d}.{effort}'.format(dd=date.day,mm=date.month,yy=date.year%1000,effort=attempt)

for sherpaversion in ["Sherpa211"]:#,"Sherpa211"]:

    indatasets = dataset_lists['Gamma_'+sherpaversion]
    first = True
    for indataset in indatasets:
        indscomps = indataset.split(".")
        if indscomps[0] == 'user':
            indscomps.pop(0)

        intreeDS = ''
        outdataset = ''
        pathtemp = ''
        pathcmd = ''

        tmpdir = '/tmp/rsmith/'
        tarball = tmpdir+'PhotonTruthStudy.'+suffix

        outdataset = 'user.rsmith.v4.fixOR.{dsid}.{shortname}.PhotonTruthStudy.{suf}'.format(dsid=indscomps[1],shortname=indscomps[2],suf=suffix)
        pathtemp = r'pathena --inDS={inds} --outDS={outds} StudyAllPhotonSherpa211.py  --outTarBall={tar} --mergeOutput'
        pathcmd = pathtemp.format(inds=indataset,outds=outdataset,ver=sherpaversion,tar=tarball)

        if first:
            if not os.path.isdir(tmpdir): os.makedirs(tmpdir)
        else:
            pathcmd = pathcmd.replace('outTarBall','inTarBall')

        first = False

        print "\n      *** submitting ***\n"
        print pathcmd
        subprocess.call(pathcmd,shell=True)

