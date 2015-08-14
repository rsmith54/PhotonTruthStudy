import ROOT
import AtlasStyle

xsecs = {}


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

xsecs["LO"] = {
'GammaPt35' :      35002. * 0.10372,
'GammaPt70' :      3135.2 * 0.11728,
'GammaPt140' :     249.37 * 0.12874,
'GammaPt280' :     13.874 * 0.14065,
'GammaPt500' :     .93819 * 0.14811,
'GammaPt1000' :    .019046* 0.15750,
'GammaPt2000' :    0.000082153 * 0.16548,
'GammaPt4000' :    0.0000000025431* 0.14831,
}                           #filt eff     kfact              xsec
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

# xsecs["NLO"]= {"ZPt0"    :        0.080032 	*0.90105*	    11949.	,
#                "ZPt70"   :        0.132849 	*0.90105*	    428.59	,
#                "ZPt140"  :        0.147665 	*0.90105*	    66.149	,
#                "ZPt280"  :        0.161749 	*0.90105*	    4.8839	,
#                "ZPt500"  :        0.164931 	*0.90105*	    0.30345,
#                "ZPt700"  :        0.163096    *0.90105*	    0.056399	,
#                "ZPt1000" :        0.197191 *   0.90105*	    0.0078858	,
#                "ZPt2000" :        0.215729 *   0.90105*	    0.000032459	,
# }



plotdirs = [
'GammaPt35',
'GammaPt70',
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

colours = {"LO" : ROOT.kRed,
           "NLO": ROOT.kBlue,
}

filein = {
#    "LO":  ROOT.TFile("output/ZbosonTruthTest.small.root"),#.Sherpa145.root"),
    "LO": ROOT.TFile("output/user.rsmith.v3.Sherpa.hadd.BFilter.root"),
}

histnames = [
# "Zboson_refpt",
# "Zboson_fspt",
# "Zboson_refeta",
# "Zboson_fseta",
"Jet_fspt",
"Jet_fseta",
"Jet1_fspt",
"Jet1_fseta",
# "Zboson_dRjet",
# "Zboson_dPhiJet",
# "Zboson_dRjmin",
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

#for order in ["NLO"]:
for order in ["LO"]:
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
            print histname
            hist = filein[order].Get(plotdir+"/"+histname)
            hist.Scale(normalisation)
            hist.SetLineColor(ROOT.kBlack)
#            hist.SetFillColor(colours[order])
            hist.SetFillColor(fillcolor)
            stacks[histname].Add(hist)
            hists[order][plotdir][histname] = hist
            if len(hists[order])==1:
                leg.AddEntry(hist,order,'f')

c = ROOT.TCanvas("gammaTruth")
c.SetLogy()
for histname in histnames:
    c.SetLogx("pt" in histname)
    stacks[histname].Draw("hist")
    stacks[histname].SetMinimum(1e-1)
    stacks[histname].SetMaximum(1e4)
    stacks[histname].GetXaxis().SetTitle(histname)
    stacks[histname].GetYaxis().SetTitle("Events / {0} ifb".format(lumi))
    leg.Draw()
    c.SaveAs("Gammaplots/"+histname+".eps")
