# echo "setup PhotonTruthStudy PhotonTruthStudy-00-00-00 in /var/clus/usera/khoo/Work_2014/AthAnaBase/MC15_Zgamma"

if test "${CMTROOT}" = ""; then
  CMTROOT=/cvmfs/atlas.cern.ch/repo/sw/software/AthAnalysisBase/x86_64-slc6-gcc48-opt/2.2.6/CMT/v1r25; export CMTROOT
fi
. ${CMTROOT}/mgr/setup.sh
cmtPhotonTruthStudytempfile=`${CMTROOT}/mgr/cmt -quiet build temporary_name`
if test ! $? = 0 ; then cmtPhotonTruthStudytempfile=/tmp/cmt.$$; fi
${CMTROOT}/mgr/cmt setup -sh -pack=PhotonTruthStudy -version=PhotonTruthStudy-00-00-00 -path=/var/clus/usera/khoo/Work_2014/AthAnaBase/MC15_Zgamma  -no_cleanup $* >${cmtPhotonTruthStudytempfile}
if test $? != 0 ; then
  echo >&2 "${CMTROOT}/mgr/cmt setup -sh -pack=PhotonTruthStudy -version=PhotonTruthStudy-00-00-00 -path=/var/clus/usera/khoo/Work_2014/AthAnaBase/MC15_Zgamma  -no_cleanup $* >${cmtPhotonTruthStudytempfile}"
  cmtsetupstatus=2
  /bin/rm -f ${cmtPhotonTruthStudytempfile}
  unset cmtPhotonTruthStudytempfile
  return $cmtsetupstatus
fi
cmtsetupstatus=0
. ${cmtPhotonTruthStudytempfile}
if test $? != 0 ; then
  cmtsetupstatus=2
fi
/bin/rm -f ${cmtPhotonTruthStudytempfile}
unset cmtPhotonTruthStudytempfile
return $cmtsetupstatus

