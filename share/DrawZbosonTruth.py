import ROOT
import AtlasStyle

xsecs = {}
xsecs["LO"] = {}                           #filt eff     kfact              xsec
# xsecs["NLO"]= {"ZPt0_70_CVetoBVeto" :        0.778461 	*0.90105*	    11937.	,
#                "ZPt0_70_CFilterBVeto" :      0.140128 	*0.90105*	    11933.	,
#                "ZPt0_70_BFilter" :           0.080032 	*0.90105*	    11949.	,
#                "ZPt70_140_CVetoBVeto" :      0.649624 	*0.90105*	    428.25	,
#                "ZPt70_140_CFilterBVeto" :    0.218402 	*0.90105*	    427.67	,
#                "ZPt70_140_BFilter" :         0.132849 	*0.90105*	    428.59	,
#                "ZPt140_280_CVetoBVeto" :     0.613840 	*0.90105*	    65.902	,
#                "ZPt140_280_CFilterBVeto" :   0.239057 	*0.90105*	    65.796	,
#                "ZPt140_280_BFilter" :        0.147665 	*0.90105*	    66.149	,
#                "ZPt280_500_CVetoBVeto" :     0.585661 	*0.90105*	    4.8378	,
#                "ZPt280_500_CFilterBVeto" :   0.260628 	*0.90105*	    4.8408	,
#                "ZPt280_500_BFilter" :        0.161749 	*0.90105*	    4.8839	,
#                "ZPt500_700_CVetoBVeto" :     0.555049 	*0.90105*	    0.29329,
#                "ZPt500_700_CFilterBVeto" :   0.274948 	*0.90105*	    0.30096,
#                "ZPt500_700_BFilter" :        0.164931 	*0.90105*	    0.30345,
#                "ZPt700_1000_CVetoBVeto" :    0.557693    *0.90105*	    0.053341	,
#                "ZPt700_1000_CFilterBVeto" :  0.303868    *0.90105*	    0.054118	,
#                "ZPt700_1000_BFilter" :       0.163096    *0.90105*	    0.056399	,
#                "ZPt1000_2000_CVetoBVeto" :   0.534707 *   0.90105*	    0.0076507	,
#                "ZPt1000_2000_CFilterBVeto" : 0.312154 *   0.90105*	    0.0084891	,
#                "ZPt1000_2000_BFilter" :      0.197191 *   0.90105*	    0.0078858	,
#                "ZPt2000_E_CMS_CVetoBVeto" :  0.543622 *   0.90105*	    0.000034976	,
#                "ZPt2000_E_CMS_CFilterBVeto" :0.345637 *  0.90105*	    0.000021126	,
#                "ZPt2000_E_CMS_BFilter" :     0.215729 *   0.90105*	    0.000032459	,
# }

xsecs["NLO"]= {"ZPt0"    :        0.080032 	*0.90105*	    11949.	,
               "ZPt70"   :        0.132849 	*0.90105*	    428.59	,
               "ZPt140"  :        0.147665 	*0.90105*	    66.149	,
               "ZPt280"  :        0.161749 	*0.90105*	    4.8839	,
               "ZPt500"  :        0.164931 	*0.90105*	    0.30345,
               "ZPt700"  :        0.163096    *0.90105*	    0.056399	,
               "ZPt1000" :        0.197191 *   0.90105*	    0.0078858	,
               "ZPt2000" :        0.215729 *   0.90105*	    0.000032459	,
}



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
#    "LO":  ROOT.TFile("output/ZbosonTruthTest.small.root"),#.Sherpa145.root"),
    "NLO": ROOT.TFile("output/user.rsmith.v3.hadd.Sherpa_CT10_Znunu.BFilter.merge.ZbosonTruthStudy.root"),
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
stacks = {}
leg = ROOT.TLegend(0.7,0.7,0.9,0.9)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
#for order in ["LO","NLO"]:

for order in ["NLO"]:
    hists[order] = {}
    fillcolor = 1;
    for plotdir in plotdirs :
        fillcolor = fillcolor + 1
        hists[order][plotdir] = {}
#        plotdir = "ZPt500"
        evtsprocessed = filein[order].Get(plotdir+"/EvtsProcessed")
    #    evtsprocessed = 1000
        print "plotdir   : " + str( plotdir)
        print "lumi      : " + str( lumi   )
        print "nevnts    : " + str( evtsprocessed.GetBinContent(1))
        print "sumweight : " + str( evtsprocessed.GetBinContent(2))
        print "xsec      : " + str( xsecs[order][plotdir])
        if(evtsprocessed.GetBinContent(2) < 1) : continue
#        normalisation[order] = lumi/evtsprocessed.GetBinContent(2)*xsecs[order]*filteff[order]
        normalisation = lumi/evtsprocessed.GetBinContent(2)*xsecs[order][plotdir]#*filteff[order][plotdir]


        for histname in histnames:
            if not histname in stacks.keys():
                stacks[histname] = ROOT.THStack("hs_"+histname,histname)
            hist = filein[order].Get(plotdir+"/"+histname)
            hist.Scale(normalisation)
            hist.SetLineColor(ROOT.kBlack)
#            hist.SetFillColor(colours[order])
            hist.SetFillColor(fillcolor)
            stacks[histname].Add(hist)
            hists[order][plotdir][histname] = hist
            if len(hists[order])==1:
                leg.AddEntry(hist,order,'f')

c = ROOT.TCanvas("ztruth")
c.SetLogy()
for histname in histnames:
    c.SetLogx("pt" in histname)
    stacks[histname].Draw("hist")
    stacks[histname].SetMinimum(1e-1)
    stacks[histname].SetMaximum(1e7)
    stacks[histname].GetXaxis().SetTitle(histname)
    stacks[histname].GetYaxis().SetTitle("Events / {0} ifb".format(lumi))
    leg.Draw()
    c.SaveAs("Zplots/"+histname+".eps")
