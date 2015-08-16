import ROOT
import AtlasStyle

xsecs = {"LO"  : {
        "CVetoBVeto"   : {},
        "CFilterBVeto" : {},
        "BFilter"      : {},
        },
         "NLO" : {
        "CVetoBVeto"   : {"ZPt0"    :         0.778461 	*0.90105*	    11937.	,
                          "ZPt70"   :      0.649624 	*0.90105*	    428.25	,
                          "ZPt140"  :     0.613840 	*0.90105*	    65.902	,
                          "ZPt280"  :     0.585661 	*0.90105*	    4.8378	,
                          "ZPt500"  :     0.555049 	*0.90105*	    0.29329,
                          "ZPt700"  :    0.557693   *0.90105*	    0.053341	,
                          "ZPt1000" :   0.534707   *0.90105*	    0.0076507	,
                          "ZPt2000" :  0.543622   *0.90105*	    0.000034976	,
                          },
        "CFilterBVeto" : {"ZPt0"    :      0.140128 	*0.90105*	    11933.	,
                          "ZPt70"   :    0.218402 	*0.90105*	    427.67	,
                          "ZPt140"  :   0.239057 	*0.90105*	    65.796	,
                          "ZPt280"  :   0.260628 	*0.90105*	    4.8408	,
                          "ZPt500"  :   0.274948 	*0.90105*	    0.30096,
                          "ZPt700"  :  0.303868    *0.90105*	    0.054118	,
                          "ZPt1000" : 0.312154 *   0.90105*	    0.0084891	,
                          "ZPt2000" :0.345637 *  0.90105*	    0.000021126	,
                          },
        "BFilter"      : {"ZPt0"    :        0.080032 	*0.90105*	    11949.	,
                          "ZPt70"   :        0.132849 	*0.90105*	    428.59	,
                          "ZPt140"  :        0.147665 	*0.90105*	    66.149	,
                          "ZPt280"  :        0.161749 	*0.90105*	    4.8839	,
                          "ZPt500"  :        0.164931 	*0.90105*	    0.30345,
                          "ZPt700"  :        0.163096    *0.90105*	    0.056399	,
                          "ZPt1000" :        0.197191 *   0.90105*	    0.0078858	,
                          "ZPt2000" :        0.215729 *   0.90105*	    0.000032459	,
                          },
        },#NLO subdict
         }#xsec dict

bfilts = ["CVetoBVeto",
          "CFilterBVeto",
          "BFilter",
          ]

plotdirs = [
    "ZPt0"    ,
    "ZPt70",
    "ZPt140",
    "ZPt280",
    "ZPt500",
    "ZPt700",
    "ZPt1000",
    "ZPt2000",
#    "ZPt4000",
]

# xsecs = {"LO":    10471000.,
#          "NLO":   12472000.,
#          }

# filteff = {"LO":  0.039883,
#            "NLO": 0.080719,
#            }

colours = {"LO" : ROOT.kRed,
           "NLO": ROOT.kBlue,
}

filein = {
    "LO":  {},#ROOT.TFile("output/ZbosonTruthTest.small.root"),#.Sherpa145.root"),
    "NLO": {"CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.CVetoBVeto.root"  ),
            "CFilterBVeto" :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.CFilterBVeto.root"),
            "BFilter"      :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.BFilter.root"     ),
            }
}

histnames = [
"Zboson_refpt",
"Zboson_fspt",
"Zboson_refeta",
"Zboson_fseta",
"Jet_fspt",
"Jet_fseta",
"Jet1_fspt",
"Jet1_fseta",
"Zboson_dRjet",
"Zboson_dPhiJet",
"Zboson_dRjmin",
"Njet20",
"Njet30",
"Njet60",
"Njet100",
"Njet250",
"RJVars_PP_Mass"        ,
"RJVars_PP_InvGamma",
"RJVars_PP_dPhiBetaR",
"RJVars_PP_dPhiVis",
"RJVars_PP_CosTheta",
"RJVars_PP_dPhiDecayAngle",
"RJVars_PP_VisShape",
"RJVars_PP_MDeltaR",
"RJVars_P1_Mass",
"RJVars_P1_CosTheta",
"RJVars_P2_Mass",
"RJVars_P2_CosTheta",
"RJVars_I1_Depth",
"RJVars_I2_Depth",
"RJVars_V1_N",
"RJVars_V2_N",
"RJVars_MG"  ,
"RJVars_DeltaBetaGG" ,
"RJVars_dphiVG"	 ,
"RJVars_P_0_CosTheta"	 ,
"RJVars_C_0_CosTheta"   ,
"RJVars_P_0_dPhiGC"	,
"RJVars_P_0_MassRatioGC",
"RJVars_P_0_Jet1_pT"	,
"RJVars_P_0_Jet2_pT"	,
"RJVars_P_0_PInvHS"      ,
"RJVars_P_1_CosTheta"    ,
"RJVars_C_1_CosTheta"	 ,
"RJVars_P_1_dPhiGC"	 ,
"RJVars_P_1_MassRatioGC" ,
"RJVars_P_1_Jet1_pT",
"RJVars_P_1_Jet2_pT",
"RJVars_P_1_PInvHS" ,
"RJVars_QCD_dPhiR"  ,
"RJVars_QCD_Rpt"    ,
"RJVars_QCD_Rmsib"
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

for order in ["NLO"] :
#for order in ["LO","NLO"]:
    for histname in histnames :
        stacks[order][histname] = ROOT.THStack("hs_"+order+histname,order+histname)

fillcolor = 1;
for order in ["NLO"]:
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
                print "histname : " + histname
                hist = filein[order][bfilt].Get(plotdir+"/"+histname)
                hist.Scale(normalisation)
                hist.SetLineColor(ROOT.kBlack)
                print "hist getEntries : " + str(hist.GetEntries())
                #            hist.SetFillColor(colours[order])
                hist.SetFillColor(fillcolor)
                myclone = hist.Clone()
                stacks[order][histname].Add(myclone)
                hists[order][bfilt][plotdir][histname] = myclone
                if len(hists[order])==1:
                    leg.AddEntry(myclone,order+bfilt+plotdir,'f')


c = ROOT.TCanvas("ztruth")
c.SetLogy()
#for order in ["LO","NLO"]:
for order in ["NLO"]:
    for histname in histnames:
        c.SetLogx("pt" in histname)
        stacks[order][histname].Draw("hist")
        stacks[order][histname].SetMinimum(1e-1)
        stacks[order][histname].SetMaximum(1e4)
        stacks[order][histname].GetXaxis().SetTitle(histname)
        stacks[order][histname].GetYaxis().SetTitle("Events / {0} ifb".format(lumi))
        leg.Draw()
        c.SaveAs("Zplots/"+histname+order+".eps")
