///////////////////////// -*- C++ -*- /////////////////////////////
// ZbosonTruthAlg.cxx 
// Implementation file for class ZbosonTruthAlg
// Author: S.Binet<binet@cern.ch>
/////////////////////////////////////////////////////////////////// 

// ZbosonTruthStudy includes
#include "ZbosonTruthAlg.h"

// STL includes

// FrameWork includes
#include "GaudiKernel/Property.h"

#include "TH1D.h"

#include "xAODTruth/TruthParticleContainer.h"
#include "xAODJet/JetContainer.h"
#include "xAODTruth/TruthParticleContainer.h"
#include "xAODEventInfo/EventInfo.h"
#include "xAODMissingET/MissingETContainer.h"

using namespace xAOD;

/////////////////////////////////////////////////////////////////// 
// Public methods: 
/////////////////////////////////////////////////////////////////// 

// Constructors
////////////////
ZbosonTruthAlg::ZbosonTruthAlg( const std::string& name, 
			  ISvcLocator* pSvcLocator ) : 
  ::AthHistogramAlgorithm( name, pSvcLocator )
{
  //
  // Property declaration
  // 

  declareProperty( "ZbosonRef_PtMin", m_refz_ptmin=0 );
  declareProperty( "ZbosonRef_PtMax", m_refz_ptmax=1e9 );

}

// Destructor
///////////////
ZbosonTruthAlg::~ZbosonTruthAlg()
{}

// Athena Algorithm's Hooks
////////////////////////////
StatusCode ZbosonTruthAlg::initialize()
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

  ATH_CHECK( book( TH1D("Zboson_refpt",  "Zboson_refpt",   56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Zboson_fspt",   "Zboson_fspt",    56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Zboson_fset",   "Zboson_fset",    56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Zboson_refeta", "Zboson_refeta",  100, -5, 5     ) ) );
  ATH_CHECK( book( TH1D("Zboson_fseta",  "Zboson_fseta",   100, -5, 5     ) ) );
  //
  ATH_CHECK( book( TH1D("Jet_fspt",      "Jet_fspt",       56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Jet_fseta",     "Jet_fseta",      100, -5, 5     ) ) );
  //
  ATH_CHECK( book( TH1D("Jet1_fspt",     "Jet1_fspt",      56, ptbins     ) ) );
  ATH_CHECK( book( TH1D("Jet1_fseta",    "Jet1_fseta",     100, -5, 5     ) ) );
  //
  ATH_CHECK( book( TH1D("Zboson_dRjet",  "Zboson_dRjet",   100, 0, 5      ) ) );
  ATH_CHECK( book( TH1D("Zboson_dPhiJet","Zboson_dPhiJet", 128, -3.2, 3.2 ) ) );
  ATH_CHECK( book( TH1D("Zboson_dRjmin", "Zboson_dRjmin",  100, 0, 5      ) ) );
  //
  ATH_CHECK( book( TH1D("Njet20",        "Njet20",         20,  0, 20     ) ) );
  ATH_CHECK( book( TH1D("Njet30",        "Njet30",         20,  0, 20     ) ) );
  ATH_CHECK( book( TH1D("Njet60",        "Njet60",         20,  0, 20     ) ) );
  ATH_CHECK( book( TH1D("Njet100",       "Njet100",        20,  0, 20     ) ) );
  ATH_CHECK( book( TH1D("Njet250",       "Njet250",        20,  0, 20     ) ) );

  hist("Zboson_refpt")->Sumw2();
  hist("Zboson_fspt")->Sumw2();
  hist("Zboson_fset")->Sumw2();
  hist("Zboson_refeta")->Sumw2();
  hist("Zboson_fseta")->Sumw2();
  //
  hist("Jet_fspt")->Sumw2();
  hist("Jet_fseta")->Sumw2();
  //
  hist("Jet1_fspt")->Sumw2();
  hist("Jet1_fseta")->Sumw2();
  //
  hist("Zboson_dRjet")->Sumw2();
  hist("Zboson_dPhiJet")->Sumw2();
  hist("Zboson_dRjmin")->Sumw2();

  return StatusCode::SUCCESS;
}

StatusCode ZbosonTruthAlg::finalize()
{
  ATH_MSG_INFO ("Finalizing " << name() << "...");

  return StatusCode::SUCCESS;
}

StatusCode ZbosonTruthAlg::execute()
{  
  ATH_MSG_DEBUG ("Executing " << name() << "...");

  const TruthParticleContainer* truthColl(0);
  ATH_CHECK( evtStore()->retrieve(truthColl,"TruthParticles") );

  TLorentzVector zboson_ref;
  TLorentzVector zboson_lead;
  const TruthParticle *refnu1(0), *refnu2(0);
  const TruthParticle *leadnu1(0), *leadnu2(0);
  for(const auto& truthP : *truthColl) {
    if( abs(truthP->pdgId())==12 || abs(truthP->pdgId())==14 || abs(truthP->pdgId())==16) {
      if(truthP->status()==3) {
	if(!refnu1) refnu1 = truthP;
	else refnu2 = truthP;
      } else if(truthP->status()==1) {
	if(leadnu1) {
	  if(truthP->pt()>leadnu1->pt()) {
	    leadnu2 = leadnu1;
	    leadnu1 = truthP;
	  } else if(!leadnu2 || truthP->pt()>leadnu2->pt()) {
	    leadnu2 = truthP;
	  }
	} else {
	  leadnu1 = truthP;
	}
      }
    }
    if(refnu1 && refnu2 && leadnu1 && leadnu2) break;
  }
  if(!refnu1 || !refnu2 || !leadnu1 ||!leadnu2) {
    ATH_MSG_WARNING("How bizarre, an event with no zboson!");
    return StatusCode::SUCCESS;
  }
  zboson_ref += refnu1->p4();
  zboson_ref += refnu2->p4();
  zboson_lead += leadnu1->p4(); 
  zboson_lead += leadnu2->p4(); 

  const MissingETContainer* met_truth(0);
  ATH_CHECK( evtStore()->retrieve(met_truth,"MET_Truth") );
  const MissingET* truthmet = (*met_truth)["NonInt"];

  if(zboson_ref.Pt()<m_refz_ptmin || zboson_ref.Pt()>m_refz_ptmax) {
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
    float dR = zboson_ref.DeltaR(jet->p4());
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

  hist("Zboson_refpt")->Fill(zboson_ref.Pt()/1e3,weight);
  hist("Zboson_fspt")->Fill(zboson_lead.Pt()/1e3,weight);
  hist("Zboson_fset")->Fill(sqrt(zboson_lead.Pt()*zboson_lead.Pt()+90e3*90e3)/1e3,weight);
  hist("Zboson_refeta")->Fill(zboson_ref.Eta(),weight);
  hist("Zboson_fseta")->Fill(zboson_lead.Eta(),weight);
  //
  if(jet_lead) {
    hist("Jet1_fspt")->Fill(jet_lead->pt()/1e3,weight);
    hist("Jet1_fseta")->Fill(jet_lead->eta(),weight);
    hist("Zboson_dRjet")->Fill(zboson_lead.DeltaR(jet_lead->p4()),weight);
    hist("Zboson_dPhiJet")->Fill(zboson_lead.DeltaPhi(jet_lead->p4()),weight);
  }
  hist("Zboson_dRjmin")->Fill(dRmin,weight);
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


