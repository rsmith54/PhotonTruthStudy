///////////////////////// -*- C++ -*- /////////////////////////////
// PhotonTruthAlg.cxx 
// Implementation file for class PhotonTruthAlg
// Author: S.Binet<binet@cern.ch>
/////////////////////////////////////////////////////////////////// 

// PhotonTruthStudy includes
#include "PhotonTruthAlg.h"

// STL includes

// FrameWork includes
#include "GaudiKernel/Property.h"

#include "TH1D.h"

#include "xAODTruth/TruthParticleContainer.h"
#include "xAODJet/JetContainer.h"
#include "xAODTruth/TruthParticleContainer.h"
#include "xAODEventInfo/EventInfo.h"

using namespace xAOD;

/////////////////////////////////////////////////////////////////// 
// Public methods: 
/////////////////////////////////////////////////////////////////// 

// Constructors
////////////////
PhotonTruthAlg::PhotonTruthAlg( const std::string& name, 
			  ISvcLocator* pSvcLocator ) : 
  ::AthHistogramAlgorithm( name, pSvcLocator )
{
  //
  // Property declaration
  // 

  declareProperty( "PhotonRef_PtMin", m_refy_ptmin=0 );
  declareProperty( "PhotonRef_PtMax", m_refy_ptmax=1e9 );

}

// Destructor
///////////////
PhotonTruthAlg::~PhotonTruthAlg()
{}

// Athena Algorithm's Hooks
////////////////////////////
StatusCode PhotonTruthAlg::initialize()
{
  ATH_MSG_INFO ("Initializing " << name() << "...");

  ATH_CHECK( book( TH1D("EvtsProcessed", "EvtsProcessed",  2, 0., 2 ) ) );
  hist("EvtsProcessed")->Fill("NEvents",0.);
  hist("EvtsProcessed")->Fill("SumWeights",0.);

  double fac = sqrt(sqrt(sqrt(2)));
  double ptbins[57];
  ptbins[0] = 25;
  for(size_t i(1); i<57; ++i) {
    ptbins[i] = ptbins[i-1]*fac;
  }

  ATH_CHECK( book( TH1D("Photon_refpt",  "Photon_refpt",   56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Photon_fspt",   "Photon_fspt",    56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Photon_fset",   "Photon_fset",    56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Photon_refeta", "Photon_refeta",  100, -5, 5     ) ) );
  ATH_CHECK( book( TH1D("Photon_fseta",  "Photon_fseta",   100, -5, 5     ) ) );
  //
  ATH_CHECK( book( TH1D("Jet_fspt",      "Jet_fspt",       56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Jet_fseta",     "Jet_fseta",      100, -5, 5     ) ) );
  //
  ATH_CHECK( book( TH1D("Jet1_fspt",     "Jet1_fspt",      56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Jet1_fseta",    "Jet1_fseta",     100, -5, 5     ) ) );
  //
  ATH_CHECK( book( TH1D("Photon_dRjet",  "Photon_dRjet",   100, 0, 5      ) ) );
  ATH_CHECK( book( TH1D("Photon_dPhiJet","Photon_dPhiJet", 128, -3.2, 3.2 ) ) );
  ATH_CHECK( book( TH1D("Photon_dRjmin", "Photon_dRjmin",  100, 0, 5      ) ) );
  //
  ATH_CHECK( book( TH1D("Njet20",        "Njet20",         20,  0, 20     ) ) );
  ATH_CHECK( book( TH1D("Njet30",        "Njet30",         20,  0, 20     ) ) );
  ATH_CHECK( book( TH1D("Njet60",        "Njet60",         20,  0, 20     ) ) );
  ATH_CHECK( book( TH1D("Njet100",       "Njet100",        20,  0, 20     ) ) );
  ATH_CHECK( book( TH1D("Njet250",       "Njet250",        20,  0, 20     ) ) );

  hist("Photon_refpt")->Sumw2();
  hist("Photon_fspt")->Sumw2();
  hist("Photon_fset")->Sumw2();
  hist("Photon_refeta")->Sumw2();
  hist("Photon_fseta")->Sumw2();
  //
  hist("Jet_fspt")->Sumw2();
  hist("Jet_fseta")->Sumw2();
  //
  hist("Jet1_fspt")->Sumw2();
  hist("Jet1_fseta")->Sumw2();
  //
  hist("Photon_dRjet")->Sumw2();
  hist("Photon_dPhiJet")->Sumw2();
  hist("Photon_dRjmin")->Sumw2();

  return StatusCode::SUCCESS;
}

StatusCode PhotonTruthAlg::finalize()
{
  ATH_MSG_INFO ("Finalizing " << name() << "...");

  return StatusCode::SUCCESS;
}

StatusCode PhotonTruthAlg::execute()
{  
  ATH_MSG_DEBUG ("Executing " << name() << "...");

  const TruthParticleContainer* truthColl(0);
  ATH_CHECK( evtStore()->retrieve(truthColl,"TruthParticles") );

  const TruthParticle* photon_ref(0);
  const TruthParticle* photon_lead(0);

  for(const auto& truthp : *truthColl) {
    if(truthp->pdgId()==22) {
      if(truthp->status()==3) photon_ref = truthp;
      if(truthp->status()==1 && (!photon_lead || truthp->pt() > photon_lead->pt())) photon_lead = truthp;
    }
  }

  if(!photon_ref || !photon_lead) {
    ATH_MSG_WARNING("How bizarre, an event with no photon!");
    return StatusCode::SUCCESS;
  }

  if(photon_ref->pt()<m_refy_ptmin || photon_ref->pt()>m_refy_ptmax) {
    return StatusCode::SUCCESS;
  }

  const xAOD::EventInfo* eventInfo(0);
  ATH_CHECK( evtStore()->retrieve(eventInfo) );
  double weight=1;
  weight *= eventInfo->mcEventWeight();

  hist("EvtsProcessed")->Fill("NEvents",1);
  hist("EvtsProcessed")->Fill("SumWeights",weight);

  const Jet* jet_lead(0);
  const JetContainer* truthJets(0);
  float dRmin(99.);
  ATH_CHECK( evtStore()->retrieve(truthJets,"AntiKt4TruthJets") );
  size_t Nj20(0), Nj30(0), Nj60(0), Nj100(0), Nj250(0);
  for(const auto&  jet : *truthJets) {
    float dR = photon_lead->p4().DeltaR(jet->p4());
    if(dR<0.2) continue;
    if(jet->pt()>10e3) {
      if(!jet_lead || jet->pt()>jet_lead->pt()) {
	jet_lead = jet;
      }
      hist("Jet_fspt")->Fill(jet->pt()/1e3,weight);
      hist("Jet_fseta")->Fill(jet->eta(),weight);
      if(dR<dRmin) dRmin = dR;
      if(jet->pt()>20e3) ++Nj20;
      if(jet->pt()>30e3) ++Nj30;
      if(jet->pt()>60e3) ++Nj60;
      if(jet->pt()>100e3) ++Nj100;
      if(jet->pt()>250e3) ++Nj250;      
    }
  }

  hist("Photon_refpt")->Fill(photon_ref->pt()/1e3,weight);
  hist("Photon_fspt")->Fill(photon_lead->pt()/1e3,weight);
  hist("Photon_fset")->Fill(photon_lead->pt()/1e3,weight);
  hist("Photon_refeta")->Fill(photon_ref->eta(),weight);
  hist("Photon_fseta")->Fill(photon_lead->eta(),weight);
  //
  if(jet_lead) {
    hist("Jet1_fspt")->Fill(jet_lead->pt()/1e3,weight);
    hist("Jet1_fseta")->Fill(jet_lead->eta(),weight);
    hist("Photon_dRjet")->Fill(photon_lead->p4().DeltaR(jet_lead->p4()),weight);
    hist("Photon_dPhiJet")->Fill(photon_lead->p4().DeltaPhi(jet_lead->p4()),weight);
  }
  hist("Photon_dRjmin")->Fill(dRmin,weight);
  //
  hist("Njet20")->Fill(Nj20,weight);
  hist("Njet30")->Fill(Nj30,weight);
  hist("Njet60")->Fill(Nj60,weight);
  hist("Njet100")->Fill(Nj100,weight);
  hist("Njet250")->Fill(Nj250,weight);

  return StatusCode::SUCCESS;
}

/////////////////////////////////////////////////////////////////// 
// Const methods: 
///////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////// 
// Non-const methods: 
/////////////////////////////////////////////////////////////////// 

/////////////////////////////////////////////////////////////////// 
// Protected methods: 
/////////////////////////////////////////////////////////////////// 

/////////////////////////////////////////////////////////////////// 
// Const methods: 
///////////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////////// 
// Non-const methods: 
/////////////////////////////////////////////////////////////////// 


