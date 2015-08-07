///////////////////////// -*- C++ -*- /////////////////////////////
// PhotonTruthAlg.h
// Header file for class PhotonTruthAlg
// Author: S.Binet<binet@cern.ch>
///////////////////////////////////////////////////////////////////
#ifndef PHOTONTRUTHSTUDY_PHOTONTRUTHALG_H
#define PHOTONTRUTHSTUDY_PHOTONTRUTHALG_H 1

// STL includes
#include <string>

// FrameWork includes
#include "AthenaBaseComps/AthHistogramAlgorithm.h"


class JetProxy;
class PhysObjProxyUtils;


class PhotonTruthAlg
  : public ::AthHistogramAlgorithm
{

  ///////////////////////////////////////////////////////////////////
  // Public methods:
  ///////////////////////////////////////////////////////////////////
 public:

  // Copy constructor:

  /// Constructor with parameters:
  PhotonTruthAlg( const std::string& name, ISvcLocator* pSvcLocator );

  /// Destructor:
  virtual ~PhotonTruthAlg();

  // Assignment operator:
  //PhotonTruthAlg &operator=(const PhotonTruthAlg &alg);

  // Athena algorithm's Hooks
  virtual StatusCode  initialize();
  virtual StatusCode  execute();
  virtual StatusCode  finalize();

  ///////////////////////////////////////////////////////////////////
  // Const methods:
  ///////////////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////////////
  // Non-const methods:
  ///////////////////////////////////////////////////////////////////

  ///////////////////////////////////////////////////////////////////
  // Private data:
  ///////////////////////////////////////////////////////////////////
 private:

  float m_refy_ptmin;
  float	m_refy_ptmax;

  PhysObjProxyUtils * m_proxyUtils;

  /// Default constructor:
  PhotonTruthAlg();

  /// Containers

  // void RJigsawInit();


  // void CalculateRJigsawVariables(const std::vector<JetProxy>& jets,
  // 				 Double_t metx,
  // 				 Double_t mety,
  // 				 std::map<TString,float>& RJigsawVariables,
  // 				 Double_t jetPtCut=0.);


};

// I/O operators
//////////////////////

///////////////////////////////////////////////////////////////////
// Inline methods:
///////////////////////////////////////////////////////////////////


#endif //> !PHOTONTRUTHSTUDY_PHOTONTRUTHALG_H
