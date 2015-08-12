///////////////////////// -*- C++ -*- /////////////////////////////
// ZbosonTruthAlg.cxx
// Implementation file for class ZbosonTruthAlg
// Author: S.Binet<binet@cern.ch>
///////////////////////////////////////////////////////////////////

// ZbosonTruthStudy includes
#include "ZbosonTruthAlg.h"
#include "PhotonTruthStudy/PhysObjProxies.h"
#include "PhotonTruthStudy/PhysObjProxyUtils.h"

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
  ::AthHistogramAlgorithm( name, pSvcLocator ),
  m_proxyUtils(nullptr)
{
  //
  // Property declaration
  //

  declareProperty( "ZbosonRef_PtMin", m_refz_ptmin=0 );
  declareProperty( "ZbosonRef_PtMax", m_refz_ptmax=1e9 );
  declareProperty( "JetRJCut", m_jetRJcut=30000. );
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

  m_proxyUtils = new PhysObjProxyUtils(false);
  m_proxyUtils->RJigsawInit();

  gErrorIgnoreLevel = kError; //suppress tvector3 complaints

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

  ATH_CHECK( book( TH1D("RJVars_PP_Mass"        ,     "RJVars_PP_Mass"            ,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_PP_InvGamma"	  ,   "RJVars_PP_InvGamma"	  ,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_PP_dPhiBetaR"	  ,   "RJVars_PP_dPhiBetaR"	  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_PP_dPhiVis"	  ,   "RJVars_PP_dPhiVis"	  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_PP_CosTheta"	  ,   "RJVars_PP_CosTheta"	  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_PP_dPhiDecayAngle", "RJVars_PP_dPhiDecayAngle", 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_PP_VisShape"	  ,   "RJVars_PP_VisShape"	  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_PP_MDeltaR"	  ,   "RJVars_PP_MDeltaR"	  ,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P1_Mass"	  ,   "RJVars_P1_Mass"	  ,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P1_CosTheta"	  ,   "RJVars_P1_CosTheta"	  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_P2_Mass"          , "RJVars_P2_Mass"          ,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P2_CosTheta"	  ,   "RJVars_P2_CosTheta"	  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_I1_Depth"	  ,   "RJVars_I1_Depth"	  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_I2_Depth"	  ,   "RJVars_I2_Depth"	  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_V1_N"	  ,	      "RJVars_V1_N"	  ,    100 , 0,20 )));
  ATH_CHECK( book( TH1D("RJVars_V2_N"            ,  "RJVars_V2_N"            ,    100 , 0,20 )));
  ATH_CHECK( book( TH1D("RJVars_MG"		 ,    "RJVars_MG"		 ,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_DeltaBetaGG"	 ,    "RJVars_DeltaBetaGG"	 , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_dphiVG"	 ,    "RJVars_dphiVG"	         , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_P_0_CosTheta"	 ,    "RJVars_P_0_CosTheta"	 , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_C_0_CosTheta"   ,   "RJVars_C_0_CosTheta"   , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_P_0_dPhiGC"	,     "RJVars_P_0_dPhiGC"	, 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_P_0_MassRatioGC",   "RJVars_P_0_MassRatioGC",    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P_0_Jet1_pT"	,     "RJVars_P_0_Jet1_pT"	,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P_0_Jet2_pT"	,     "RJVars_P_0_Jet2_pT"	,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P_0_PInvHS"      ,  "RJVars_P_0_PInvHS"      ,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P_1_CosTheta"    ,  "RJVars_P_1_CosTheta"    , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_C_1_CosTheta"	 ,    "RJVars_C_1_CosTheta"	 , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_P_1_dPhiGC"	 ,    "RJVars_P_1_dPhiGC"	 , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_P_1_MassRatioGC" ,  "RJVars_P_1_MassRatioGC" ,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P_1_Jet1_pT",	      "RJVars_P_1_Jet1_pT",    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P_1_Jet2_pT",	      "RJVars_P_1_Jet2_pT",    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_P_1_PInvHS" ,	      "RJVars_P_1_PInvHS" ,    100 , 0,2e6 )));
  ATH_CHECK( book( TH1D("RJVars_QCD_dPhiR"  ,	      "RJVars_QCD_dPhiR"  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_QCD_Rpt"    ,	      "RJVars_QCD_Rpt"    , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_QCD_Rmsib"  ,	      "RJVars_QCD_Rmsib"  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_QCD_Rpsib"  ,	      "RJVars_QCD_Rpsib"  , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_QCD_Delta1" ,	      "RJVars_QCD_Delta1" , 128, -3.2, 3.2 )));
  ATH_CHECK( book( TH1D("RJVars_QCD_Delta2" ,       "RJVars_QCD_Delta2" , 128, -3.2, 3.2 )));





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


  hist("RJVars_PP_Mass"        )->Sumw2();
  hist("RJVars_PP_InvGamma"	  )->Sumw2();
  hist("RJVars_PP_dPhiBetaR"	  )->Sumw2();
  hist("RJVars_PP_dPhiVis"	  )->Sumw2();
  hist("RJVars_PP_CosTheta"	  )->Sumw2();
  hist("RJVars_PP_dPhiDecayAngle")->Sumw2();
  hist("RJVars_PP_VisShape"	  )->Sumw2();
  hist("RJVars_PP_MDeltaR"	  )->Sumw2();
  hist("RJVars_P1_Mass"	  )->Sumw2();
  hist("RJVars_P1_CosTheta"	  )->Sumw2();
  hist("RJVars_P2_Mass"          )->Sumw2();
  hist("RJVars_P2_CosTheta"	  )->Sumw2();
  hist("RJVars_I1_Depth"	  )->Sumw2();
  hist("RJVars_I2_Depth"	  )->Sumw2();
  hist("RJVars_V1_N"	  )->Sumw2();
  hist("RJVars_V2_N"            )->Sumw2();
  hist("RJVars_MG"		 )->Sumw2();
  hist("RJVars_DeltaBetaGG"	 )->Sumw2();
  hist("RJVars_dphiVG"	 )->Sumw2();
  hist("RJVars_P_0_CosTheta"	 )->Sumw2();
  hist("RJVars_C_0_CosTheta"   )->Sumw2();
  hist("RJVars_P_0_dPhiGC"	)->Sumw2();
  hist("RJVars_P_0_MassRatioGC")->Sumw2();
  hist("RJVars_P_0_Jet1_pT"	)->Sumw2();
  hist("RJVars_P_0_Jet2_pT"	)->Sumw2();
  hist("RJVars_P_0_PInvHS"      )->Sumw2();
  hist("RJVars_P_1_CosTheta"    )->Sumw2();
  hist("RJVars_C_1_CosTheta"	 )->Sumw2();
  hist("RJVars_P_1_dPhiGC"	 )->Sumw2();
  hist("RJVars_P_1_MassRatioGC" )->Sumw2();
  hist("RJVars_P_1_Jet1_pT")->Sumw2();
  hist("RJVars_P_1_Jet2_pT")->Sumw2();
  hist("RJVars_P_1_PInvHS" )->Sumw2();
  hist("RJVars_QCD_dPhiR"  )->Sumw2();
  hist("RJVars_QCD_Rpt"    )->Sumw2();
  hist("RJVars_QCD_Rmsib"  )->Sumw2();
  hist("RJVars_QCD_Rpsib"  )->Sumw2();
  hist("RJVars_QCD_Delta1" )->Sumw2();
  hist("RJVars_QCD_Delta2" )->Sumw2();


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

  const TruthParticleContainer* truthNus(0);
  ATH_CHECK( evtStore()->retrieve(truthNus,"TruthNeutrinos") );

  TLorentzVector zboson_ref;
  TLorentzVector zboson_lead;
  const TruthParticle *refnu1(0), *refnu2(0);
  const TruthParticle *leadnu1(0), *leadnu2(0);
  for(const auto& truthP : *truthColl) {
    if( abs(truthP->pdgId())==12 || abs(truthP->pdgId())==14 || abs(truthP->pdgId())==16) {
      //std::cout << __PRETTY_FUNCTION__ << " at line : " << __LINE__ << std::endl;
      if(truthP->status()==3) {
      //std::cout << __PRETTY_FUNCTION__ << " at line : " << __LINE__ << std::endl;
	if(!refnu1) refnu1 = truthP;
	else if(!refnu2) refnu2 = truthP;
	else if(truthP->pt() > refnu2->pt()){
      //std::cout << __PRETTY_FUNCTION__ << " at line : " << __LINE__ << std::endl;
	  refnu1 = (refnu2->pt() >  truthP->pt()) ? refnu2 : truthP;
	  refnu2 = (refnu2->pt() <= truthP->pt()) ? refnu2 : truthP;
	}
	// if(!refnu1) refnu1 = truthP;
	// else refnu2 = truthP;
      }
    }
  }
  //std::cout << __PRETTY_FUNCTION__ << " at line : " << __LINE__ << std::endl;
  //std::cout << " nu size " << truthNus->size() << std::endl;

  for(const auto& truthNu : *truthNus) {
    //std::cout << __PRETTY_FUNCTION__ << " at line : " << __LINE__ << std::endl;
    if(!leadnu1) leadnu1 = truthNu;
    else if(!leadnu2) leadnu2 = truthNu;
    else if(truthNu->pt() > leadnu2->pt()){
      //std::cout << __PRETTY_FUNCTION__ << " at line : " << __LINE__ << std::endl;
      leadnu1 = (leadnu2->pt() >  truthNu->pt()) ? leadnu2 : truthNu;
      leadnu2 = (leadnu2->pt() <= truthNu->pt()) ? leadnu2 : truthNu;
    }
  }

  if(!refnu1 || !refnu2 || !leadnu1 ||!leadnu2) {
    ATH_MSG_WARNING("Event without a zboson!");
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

  std::vector<JetProxy> truth_jets_proxy;

  for(const auto&  jet : *truthJets) {
    JetProxy const jetproxy(jet->p4(),
			    true,
			    false,
			    true,
			    true);
    truth_jets_proxy.push_back(jetproxy);

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

  std::map<TString,float> RJigsawVariables;
  m_proxyUtils->CalculateRJigsawVariables(truth_jets_proxy,
					  truthmet->mpx(),
					  truthmet->mpy(),
					  RJigsawVariables,
					  m_jetRJcut
					  );

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



  hist("RJVars_PP_Mass")->Fill(RJigsawVariables["RJVars_PP_Mass"]);
  hist("RJVars_PP_InvGamma")->Fill(RJigsawVariables["RJVars_PP_InvGamma"]);
  hist("RJVars_PP_dPhiBetaR")->Fill(RJigsawVariables["RJVars_PP_dPhiBetaR"]);
  hist("RJVars_PP_dPhiVis")->Fill(RJigsawVariables["RJVars_PP_dPhiVis"]);
  hist("RJVars_PP_CosTheta")->Fill(RJigsawVariables["RJVars_PP_CosTheta"]);
  hist("RJVars_PP_dPhiDecayAngle")->Fill(RJigsawVariables["RJVars_PP_dPhiDecayAngle"]);
  hist("RJVars_PP_VisShape")->Fill(RJigsawVariables["RJVars_PP_VisShape"]);
  hist("RJVars_PP_MDeltaR")->Fill(RJigsawVariables["RJVars_PP_MDeltaR"]);
  hist("RJVars_P1_Mass")->Fill(RJigsawVariables["RJVars_P1_Mass"]);
  hist("RJVars_P1_CosTheta")->Fill(RJigsawVariables["RJVars_P1_CosTheta"]);
  hist("RJVars_P2_Mass")->Fill(RJigsawVariables["RJVars_P2_Mass"]);
  hist("RJVars_P2_CosTheta")->Fill(RJigsawVariables["RJVars_P2_CosTheta"]);
  hist("RJVars_I1_Depth")->Fill(RJigsawVariables["RJVars_I1_Depth"]);
  hist("RJVars_I2_Depth")->Fill(RJigsawVariables["RJVars_I2_Depth"]);
  hist("RJVars_V1_N")->Fill(RJigsawVariables["RJVars_V1_N"]);
  hist("RJVars_V2_N")->Fill(RJigsawVariables["RJVars_V2_N"]);
  hist("RJVars_MG")->Fill(RJigsawVariables["RJVars_MG"]);
  hist("RJVars_DeltaBetaGG")->Fill(RJigsawVariables["RJVars_DeltaBetaGG"]);
  hist("RJVars_dphiVG")->Fill(RJigsawVariables["RJVars_dphiVG"]);
  hist("RJVars_P_0_CosTheta")->Fill(RJigsawVariables["RJVars_P_0_CosTheta"]);
  hist("RJVars_C_0_CosTheta")->Fill(RJigsawVariables["RJVars_C_0_CosTheta"]);
  hist("RJVars_P_0_dPhiGC")->Fill(RJigsawVariables["RJVars_P_0_dPhiGC"]);
  hist("RJVars_P_0_MassRatioGC")->Fill(RJigsawVariables["RJVars_P_0_MassRatioGC"]);
  hist("RJVars_P_0_Jet1_pT")->Fill(RJigsawVariables["RJVars_P_0_Jet1_pT"]);
  hist("RJVars_P_0_Jet2_pT")->Fill(RJigsawVariables["RJVars_P_0_Jet2_pT"]);
  hist("RJVars_P_0_PInvHS")->Fill(RJigsawVariables["RJVars_P_0_PInvHS"]);
  hist("RJVars_P_1_CosTheta")->Fill(RJigsawVariables["RJVars_P_1_CosTheta"]);
  hist("RJVars_C_1_CosTheta")->Fill(RJigsawVariables["RJVars_C_1_CosTheta"]);
  hist("RJVars_P_1_dPhiGC")->Fill(RJigsawVariables["RJVars_P_1_dPhiGC"]);
  hist("RJVars_P_1_MassRatioGC")->Fill(RJigsawVariables["RJVars_P_1_MassRatioGC"]);
  hist("RJVars_P_1_Jet1_pT")->Fill(RJigsawVariables["RJVars_P_1_Jet1_pT"]);
  hist("RJVars_P_1_Jet2_pT")->Fill(RJigsawVariables["RJVars_P_1_Jet2_pT"]);
  hist("RJVars_P_1_PInvHS")->Fill(RJigsawVariables["RJVars_P_1_PInvHS"]);
  hist("RJVars_QCD_dPhiR")->Fill(RJigsawVariables["RJVars_QCD_dPhiR"]);
  hist("RJVars_QCD_Rpt")->Fill(RJigsawVariables["RJVars_QCD_Rpt"]);
  hist("RJVars_QCD_Rmsib")->Fill(RJigsawVariables["RJVars_QCD_Rmsib"]);
  hist("RJVars_QCD_Rpsib")->Fill(RJigsawVariables["RJVars_QCD_Rpsib"]);
  hist("RJVars_QCD_Delta1")->Fill(RJigsawVariables["RJVars_QCD_Delta1"]);
  hist("RJVars_QCD_Delta2")->Fill(RJigsawVariables["RJVars_QCD_Delta2"]);



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


