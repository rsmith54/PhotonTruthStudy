import subprocess, datetime, os
from datasets import *

attempt='v1'
date = datetime.datetime.now()
suffix = '{dd:02d}{mm:02d}{yy:02d}.{effort}'.format(dd=date.day,mm=date.month,yy=date.year%1000,effort=attempt)

#for sherpaversion in ["Sherpa145","Sherpa211"]:
for sherpaversion in ["Sherpa211"]:

    indatasets = dataset_lists['Zvv_'+sherpaversion]
    first = True
    for indataset in indatasets:
        indscomps = indataset.split(".")

        intreeDS = ''
        outdataset = ''
        pathtemp = ''
        pathcmd = ''

        tmpdir = '/tmp/khoo/'
        tarball = tmpdir+'ZbosonTruthStudy.'+suffix

        outdataset = 'user.khoo.{dsid}.{shortname}.ZbosonTruthStudy.{suf}'.format(dsid=indscomps[2],shortname=indscomps[3],suf=suffix)
        pathtemp = r'pathena --cmtConfig=x86_64-slc6-gcc48-opt --inDS={inds} --outDS={outds} StudyZbosonTruth.{ver}.py --outTarBall={tar} --mergeOutput' 
        pathcmd = pathtemp.format(inds=indataset,outds=outdataset,tar=tarball,ver=sherpaversion)

        if first:
            if not os.path.isdir(tmpdir): os.makedirs(tmpdir)
        else:
            pathcmd = pathcmd.replace('outTarBall','inTarBall')

        first = False

        print "\n      *** submitting ***\n"
        print pathcmd
        subprocess.call(pathcmd,shell=True)

