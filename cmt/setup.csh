# echo "setup PhotonTruthStudy PhotonTruthStudy-00-00-00 in /var/clus/usera/khoo/Work_2014/AthAnaBase/MC15_Zgamma"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/AthAnalysisBase/x86_64-slc6-gcc48-opt/2.2.6/CMT/v1r25
endif
source ${CMTROOT}/mgr/setup.csh
set cmtPhotonTruthStudytempfile=`${CMTROOT}/mgr/cmt -quiet build temporary_name`
if $status != 0 then
  set cmtPhotonTruthStudytempfile=/tmp/cmt.$$
endif
${CMTROOT}/mgr/cmt setup -csh -pack=PhotonTruthStudy -version=PhotonTruthStudy-00-00-00 -path=/var/clus/usera/khoo/Work_2014/AthAnaBase/MC15_Zgamma  -no_cleanup $* >${cmtPhotonTruthStudytempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/mgr/cmt setup -csh -pack=PhotonTruthStudy -version=PhotonTruthStudy-00-00-00 -path=/var/clus/usera/khoo/Work_2014/AthAnaBase/MC15_Zgamma  -no_cleanup $* >${cmtPhotonTruthStudytempfile}"
  set cmtsetupstatus=2
  /bin/rm -f ${cmtPhotonTruthStudytempfile}
  unset cmtPhotonTruthStudytempfile
  exit $cmtsetupstatus
endif
set cmtsetupstatus=0
source ${cmtPhotonTruthStudytempfile}
if ( $status != 0 ) then
  set cmtsetupstatus=2
endif
/bin/rm -f ${cmtPhotonTruthStudytempfile}
unset cmtPhotonTruthStudytempfile
exit $cmtsetupstatus

