import ROOT
import AtlasStyle

# 361039	Sherpa_CT10_SinglePhotonPt35_70_CVetoBVeto		34988.		1.	0.41028	1.
# 361040	Sherpa_CT10_SinglePhotonPt35_70_CFilterBVeto		34986.		1.	0.48610	1.
# 361041	Sherpa_CT10_SinglePhotonPt35_70_BFilter			35002.		1.	0.10372	1.
# 361042	Sherpa_CT10_SinglePhotonPt70_140_CVetoBVeto		3129.		1.	0.39960	1.
# 361043	Sherpa_CT10_SinglePhotonPt70_140_CFilterBVeto		3132.9		1.	0.48201	1.
# 361044	Sherpa_CT10_SinglePhotonPt70_140_BFilter		3135.2		1.	0.11728	1.
# 361045	Sherpa_CT10_SinglePhotonPt140_280_CVetoBVeto		247.41		1.	0.39265	1.
# 361046	Sherpa_CT10_SinglePhotonPt140_280_CFilterBVeto		247.39		1.	0.47826	1.
# 361047	Sherpa_CT10_SinglePhotonPt140_280_BFilter		249.37		1.	0.12874	1.
# 361048	Sherpa_CT10_SinglePhotonPt280_500_CVetoBVeto		13.648		1.	0.38607	1.
# 361049	Sherpa_CT10_SinglePhotonPt280_500_CFilterBVeto		13.617		1.	0.47349	1.
# 361050	Sherpa_CT10_SinglePhotonPt280_500_BFilter		13.874		1.	0.14065	1.
# 361051	Sherpa_CT10_SinglePhotonPt500_1000_CVetoBVeto		0.92334		1.	0.37922	1.
# 361052	Sherpa_CT10_SinglePhotonPt500_1000_CFilterBVeto		0.92185		1.	0.47149	1.
# 361053	Sherpa_CT10_SinglePhotonPt500_1000_BFilter		0.93819		1.	0.14811	1.
# 361054	Sherpa_CT10_SinglePhotonPt1000_2000_CVetoBVeto		0.018432	1.	0.37058	1.
# 361055	Sherpa_CT10_SinglePhotonPt1000_2000_CFilterBVeto	0.018388	1.	0.46648	1.
# 361056	Sherpa_CT10_SinglePhotonPt1000_2000_BFilter		0.019046	1.	0.15750	1.
# 361057	Sherpa_CT10_SinglePhotonPt2000_4000_CVetoBVeto		0.000079163	1.	0.38039	1.
# 361058	Sherpa_CT10_SinglePhotonPt2000_4000_CFilterBVeto	0.000080515	1.	0.45148	1.
# 361059	Sherpa_CT10_SinglePhotonPt2000_4000_BFilter		0.000082153	1.	0.16548	1.
# 361060	Sherpa_CT10_SinglePhotonPt4000_CVetoBVeto		0.0000000024843	1.	0.40351	1.
# 361061	Sherpa_CT10_SinglePhotonPt4000_CFilterBVeto		0.0000000025134	1.	0.41612	1.
# 361062	Sherpa_CT10_SinglePhotonPt4000_BFilter			0.0000000025431	1.	0.14831	1.


xsecs = {"LO"  : {
        "CVetoBVeto" : {'GammaPt35'  :  34988.* 0.41028 ,
                        'GammaPt70'  :  3129. * 0.39960 ,
                        'GammaPt140' :  247.41* 0.39265 ,
                        'GammaPt280' :  13.648* 0.38607 ,
                        'GammaPt500' :  0.92334*0.37922 ,
                        'GammaPt1000' : 0.018432*0.37058,
                        'GammaPt2000' : 0.000079163*0.38039,
                        'GammaPt4000' : 0.0000000024843*0.40351,
                        },
        "CFilterBVeto" : {'GammaPt35' :   34986. *0.48610,
                          'GammaPt70' :   3132.9 *0.48201,
                          'GammaPt140' :  247.39 *0.47826,
                          'GammaPt280' :  13.617 * .47349,
                          'GammaPt500' :  .92185 * .47149,
                          'GammaPt1000' : .018388* .46648,
                          'GammaPt2000' : .00008515*.45148,
                          'GammaPt4000' : 0.0000000025134*0.41612,

            },
        "BFilter"   : {'GammaPt35' :   35002. * 0.10372,
                       'GammaPt70' :   3135.2 * 0.11728,
                       'GammaPt140' :  249.37 * 0.12874,
                       'GammaPt280' :  13.874 * 0.14065,
                       'GammaPt500' :  .93819 * 0.14811,
                       'GammaPt1000' : .019046* 0.15750,
                       'GammaPt2000' : 0.000082153 * 0.16548,
                       'GammaPt4000' : 0.0000000025431* 0.14831,
                       },
        },
        "NLO" : {},
         }#xsec dict

bfilts = ["CVetoBVeto",
          "CFilterBVeto",
          "BFilter",
          ]

plotdirs = [
#'GammaPt35',
#'GammaPt70',
'GammaPt140',
'GammaPt280',
'GammaPt500',
'GammaPt1000',
'GammaPt2000',
'GammaPt4000',
]

# xsecs = {"LO":    10471000.,
#          "NLO":   12472000.,
#          }

# filteff = {"LO":  0.039883,
#            "NLO": 0.080719,
#            }


colours = {
    "LO":  {  "CVetoBVeto"     : ROOT.kRed,
              "CFilterBVeto"   : ROOT.kGreen,
              "BFilter"        : ROOT.kBlue,

            },
    "NLO": {# "CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_NLO.hadd.CVetoBVeto.root"  ),
            # "CFilterBVeto" :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_NLO.hadd.CFilterBVeto.root"),
            # "BFilter"      :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_NLO.hadd.BFilter.root"     ),
            }
}

filein = {
    "LO":  {"CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_SinglePhoton_LO.hadd.CVetoBVeto.root"),
            "CFilterBVeto" :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_SinglePhoton_LO.hadd.CFilterBVeto.root"),
            "BFilter"      :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_SinglePhoton_LO.hadd.BFilter.root"),


},#ROOT.TFile("output/ZbosonTruthTest.small.root"),#.Sherpa145.root"),
    "NLO": {#"CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.CVetoBVeto.root"  ),
            #"CFilterBVeto" :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.CFilterBVeto.root"),
            #"BFilter"      :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.BFilter.root"     ),
            }
}

histnames = [
"Photon_refpt",
"Photon_fspt",
"Photon_refeta",
"Photon_fseta",
# "Jet_fspt",
# "Jet_fseta",
# "Jet1_fspt",
# "Jet1_fseta",
"Photon_dRjet",
"Photon_dPhiJet",
"Photon_dRjmin",
# "Njet20",
# "Njet30",
# "Njet60",
# "Njet100",
# "Njet250",
# "RJVars_PP_Mass"        ,
# "RJVars_PP_InvGamma",
# "RJVars_PP_dPhiBetaR",
# "RJVars_PP_dPhiVis",
# "RJVars_PP_CosTheta",
# "RJVars_PP_dPhiDecayAngle",
# "RJVars_PP_VisShape",
# "RJVars_PP_MDeltaR",
# "RJVars_P1_Mass",
# "RJVars_P1_CosTheta",
# "RJVars_P2_Mass",
# "RJVars_P2_CosTheta",
# "RJVars_I1_Depth",
# "RJVars_I2_Depth",
# "RJVars_V1_N",
# "RJVars_V2_N",
# "RJVars_MG"  ,
# "RJVars_DeltaBetaGG" ,
# "RJVars_dphiVG"	 ,
# "RJVars_P_0_CosTheta"	 ,
# "RJVars_C_0_CosTheta"   ,
# "RJVars_P_0_dPhiGC"	,
# "RJVars_P_0_MassRatioGC",
# "RJVars_P_0_Jet1_pT"	,
# "RJVars_P_0_Jet2_pT"	,
# "RJVars_P_0_PInvHS"      ,
# "RJVars_P_1_CosTheta"    ,
# "RJVars_C_1_CosTheta"	 ,
# "RJVars_P_1_dPhiGC"	 ,
# "RJVars_P_1_MassRatioGC" ,
# "RJVars_P_1_Jet1_pT",
# "RJVars_P_1_Jet2_pT",
# "RJVars_P_1_PInvHS" ,
# "RJVars_QCD_dPhiR"  ,
# "RJVars_QCD_Rpt"    ,
# "RJVars_QCD_Rmsib"
]


hists = {}
#normalisation = {}
lumi = 1
stacks = {"LO" :{},
          "NLO":{},
          }
leg = ROOT.TLegend(0.7,0.7,0.9,0.9)
leg.SetFillStyle(0)
leg.SetBorderSize(0)

#for order in ["NLO"] :
for order in ["LO"] :
#for order in ["LO","NLO"]:
    for histname in histnames :
        stacks[order][histname] = ROOT.THStack("hs_"+order+"_"+histname,"hs_"+order+"_"+histname)

fillcolor = 1;
for order in ["LO"]:
#for order in ["NLO"]:
    hists[order] = {}

    for bfilt in bfilts :
        hists[order][bfilt] = {}
        for plotdir in plotdirs :
            fillcolor = fillcolor + 1
            if fillcolor > 9 : fillcolor = 2
            hists[order][bfilt][plotdir] = {}
        #        plotdir = "ZPt500"
            print "filein " + filein[order][bfilt].GetName()
            evtsprocessed = filein[order][bfilt].Get(plotdir+"/EvtsProcessed")
        #    evtsprocessed = 1000
            print "plotdir   : " + str( plotdir)
            print "lumi      : " + str( lumi   )
            print "nevnts    : " + str( evtsprocessed.GetBinContent(1))
            print "sumweight : " + str( evtsprocessed.GetBinContent(2))
            print "xsec      : " + str( xsecs[order][bfilt][plotdir])
            if(evtsprocessed.GetBinContent(2) < 1) : continue
        #        normalisation[order] = lumi/evtsprocessed.GetBinContent(2)*xsecs[order]*filteff[order]
            normalisation = lumi/evtsprocessed.GetBinContent(2)*xsecs[order][bfilt][plotdir]#*filteff[order][plotdir]
            print "normalisation : " + str(normalisation)

            for histname in histnames:
#                if not histname in stacks.keys():
#                print "histname : " + histname
                hist = filein[order][bfilt].Get(plotdir+"/"+histname)
                hist.Scale(normalisation)
                hist.SetLineColor(ROOT.kBlack)
                #                print "hist getEntries : " + str(hist.GetEntries())
                hist.SetFillColor(colours[order][bfilt])
                #hist.SetFillColor(fillcolor)
                myclone = hist.Clone()
                stacks[order][histname].Add(myclone)
                hists[order][bfilt][plotdir][histname] = myclone
                if len(hists[order][bfilt][plotdir])==1:
                    leg.AddEntry(myclone,order+bfilt+plotdir,'f')


c = ROOT.TCanvas("ztruth")
c.SetLogy()

#outfile = ROOT.TFile("output/outGammaStack.root", "RECREATE")
#for order in ["LO","NLO"]:
#for order in ["NLO"]:
for order in ["LO"]:
    for histname in histnames:
        c.SetLogx("pt" in histname)
        stacks[order][histname].Draw("hist")
        stacks[order][histname].SetMinimum(1e-1)
        stacks[order][histname].SetMaximum(1e4)
        stacks[order][histname].GetXaxis().SetTitle(histname)
        stacks[order][histname].GetYaxis().SetTitle("Events / {0} ifb".format(lumi))
        leg.Draw()
#        stacks[order][histname].Write()
        c.SaveAs("GammaPlots/"+histname+order+".eps")


