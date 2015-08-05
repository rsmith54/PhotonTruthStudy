# echo "cleanup PhotonTruthStudy PhotonTruthStudy-00-00-00 in /var/clus/usera/khoo/Work_2014/AthAnaBase/MC15_Zgamma"

if ( $?CMTROOT == 0 ) then
  setenv CMTROOT /cvmfs/atlas.cern.ch/repo/sw/software/AthAnalysisBase/x86_64-slc6-gcc48-opt/2.2.6/CMT/v1r25
endif
source ${CMTROOT}/mgr/setup.csh
set cmtPhotonTruthStudytempfile=`${CMTROOT}/mgr/cmt -quiet build temporary_name`
if $status != 0 then
  set cmtPhotonTruthStudytempfile=/tmp/cmt.$$
endif
${CMTROOT}/mgr/cmt cleanup -csh -pack=PhotonTruthStudy -version=PhotonTruthStudy-00-00-00 -path=/var/clus/usera/khoo/Work_2014/AthAnaBase/MC15_Zgamma  $* >${cmtPhotonTruthStudytempfile}
if ( $status != 0 ) then
  echo "${CMTROOT}/mgr/cmt cleanup -csh -pack=PhotonTruthStudy -version=PhotonTruthStudy-00-00-00 -path=/var/clus/usera/khoo/Work_2014/AthAnaBase/MC15_Zgamma  $* >${cmtPhotonTruthStudytempfile}"
  set cmtcleanupstatus=2
  /bin/rm -f ${cmtPhotonTruthStudytempfile}
  unset cmtPhotonTruthStudytempfile
  exit $cmtcleanupstatus
endif
set cmtcleanupstatus=0
source ${cmtPhotonTruthStudytempfile}
if ( $status != 0 ) then
  set cmtcleanupstatus=2
endif
/bin/rm -f ${cmtPhotonTruthStudytempfile}
unset cmtPhotonTruthStudytempfile
exit $cmtcleanupstatus

