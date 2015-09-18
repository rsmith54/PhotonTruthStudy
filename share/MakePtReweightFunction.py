import ROOT
import AtlasStyle

# 407163	Sherpa_CT10_Znunu_LO_Pt0_70_CVetoBVeto
# 407164	Sherpa_CT10_Znunu_LO_Pt0_70_CFilterBVeto
# 407165	Sherpa_CT10_Znunu_LO_Pt0_70_BFilter
# 407166	Sherpa_CT10_Znunu_LO_Pt70_140_CVetoBVeto
# 407167	Sherpa_CT10_Znunu_LO_Pt70_140_CFilterBVeto
# 407168	Sherpa_CT10_Znunu_LO_Pt70_140_BFilter
# 407169	Sherpa_CT10_Znunu_LO_Pt140_280_CVetoBVeto
# 407170	Sherpa_CT10_Znunu_LO_Pt140_280_CFilterBVeto
# 407171	Sherpa_CT10_Znunu_LO_Pt140_280_BFilter
# 407172	Sherpa_CT10_Znunu_LO_Pt280_500_CVetoBVeto
# 407173	Sherpa_CT10_Znunu_LO_Pt280_500_CFilterBVeto
# 407174	Sherpa_CT10_Znunu_LO_Pt280_500_BFilter
# 407175	Sherpa_CT10_Znunu_LO_Pt500_700_CVetoBVeto
# 407176	Sherpa_CT10_Znunu_LO_Pt500_700_CFilterBVeto
# 407177	Sherpa_CT10_Znunu_LO_Pt500_700_BFilter
# 407178	Sherpa_CT10_Znunu_LO_Pt700_1000_CVetoBVeto
# 407179	Sherpa_CT10_Znunu_LO_Pt700_1000_CFilterBVeto
# 407180	Sherpa_CT10_Znunu_LO_Pt700_1000_BFilter
# 407181	Sherpa_CT10_Znunu_LO_Pt1000_E_CMS_CVetoBVeto
# 407182	Sherpa_CT10_Znunu_LO_Pt1000_E_CMS_CFilterBVeto
# 407183	Sherpa_CT10_Znunu_LO_Pt1000_E_CMS_BFilter

xsecs = {"Zboson" : {
        "LO"  : {
        "CVetoBVeto"   : {"ZPt0"    : 10919.0	*0.999323*	0.76938,
                          "ZPt70"   : 378.85	*0.999323*	0.63549,
                          "ZPt140"  : 59.975	*0.999323*	0.61413,
                          "ZPt280"  : 4.3501	*0.999323*	0.59165,
                          "ZPt500"  : 0.26869	*0.999323*	0.57394,
                          "ZPt700"  : 0.048148	*0.999323*	0.56094,
                          "ZPt1000" : 0.0064279	*0.999323*	0.55025,
#                          "Apt2000" :
                              },
        "CFilterBVeto" : {"ZPt0"    : 10918.0	*0.999323*	0.14136,
                          "ZPt70"   : 379.03	*0.999323*	0.22287,
                          "ZPt140"  : 60.035	*0.999323*	0.23972,
                          "ZPt280"  : 4.3551	*0.999323*	0.25615,
                          "ZPt500"  : 0.26856	*0.999323*	0.26931,
                          "ZPt700"  : 0.048059	*0.999323*	0.27855,
                          "ZPt1000" : 0.006413	*0.999323*	0.28639,
                          },
        "BFilter"      : {"ZPt0"    : 10919.0	*0.999323*	0.08829 ,
                          "ZPt70"   : 378.98	*0.999323*	0.14063 ,
                          "ZPt140"  : 60.04	*0.999323*	0.14611 ,
                          "ZPt280"  : 4.3544	*0.999323*	0.1522  ,
                          "ZPt500"  : 0.2686	*0.999323*	0.15704 ,
                          "ZPt700"  : 0.048164	*0.999323*	0.16028 ,
                          "ZPt1000" : 0.0064412	*0.999323*	0.16369 ,
                          },
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
        # "LO"  : {
        #     "CVetoBVeto" : {'GammaPt35'  :  34988.* 0.41028 ,
        #                     'GammaPt70'  :  3129. * 0.39960 ,
        #                     'GammaPt140' :  247.41* 0.39265 ,
        #                     'GammaPt280' :  13.648* 0.38607 ,
        #                     'GammaPt500' :  0.92334*0.37922 ,
        #                     'GammaPt1000' : 0.018432*0.37058,
        #                     'GammaPt2000' : 0.000079163*0.38039,
        #                     'GammaPt4000' : 0.0000000024843*0.40351,
        #                     },
        #     "CFilterBVeto" : {'GammaPt35' :   34986. *0.48610,
        #                       'GammaPt70' :   3132.9 *0.48201,
        #                       'GammaPt140' :  247.39 *0.47826,
        #                       'GammaPt280' :  13.617 * .47349,
        #                       'GammaPt500' :  .92185 * .47149,
        #                       'GammaPt1000' : .018388* .46648,
        #                       'GammaPt2000' : .00008515*.45148,
        #                       'GammaPt4000' : 0.0000000025134*0.41612,

        #                       },
        #     "BFilter"   : {'GammaPt35' :   35002. * 0.10372,
        #                    'GammaPt70' :   3135.2 * 0.11728,
        #                    'GammaPt140' :  249.37 * 0.12874,
        #                    'GammaPt280' :  13.874 * 0.14065,
        #                    'GammaPt500' :  .93819 * 0.14811,
        #                    'GammaPt1000' : .019046* 0.15750,
        #                    'GammaPt2000' : 0.000082153 * 0.16548,
        #                    'GammaPt4000' : 0.0000000025431* 0.14831,
        #                },
        #     },
        # "NLO" : {},
        },#Zboson dict
         "Gamma" : {
        "LO"  : {
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
        },#Gamma dict
}#xsec dict

bfilts = { "Zboson" : [
        "CVetoBVeto",
        "CFilterBVeto",
        "BFilter",
        ],
           "Gamma" : [
        "CVetoBVeto",
        "CFilterBVeto",
        "BFilter",
        ],
}

plotdirs = { "Zboson" : [
        #"ZPt0"    ,
        "ZPt70",
        "ZPt140",
        "ZPt280",
        "ZPt500",
        "ZPt700",
        "ZPt1000",
        #    "ZPt2000",
        #    "ZPt4000",
        ],
             "Gamma" : [
        'GammaPt70' ,
        'GammaPt140',
        'GammaPt280',
        'GammaPt500',
        'GammaPt1000',
        'GammaPt2000',
        'GammaPt4000',
        ],
             }

# xsecs = {"LO":    10471000.,
#          "NLO":   12472000.,
#          }

# filteff = {"LO":  0.039883,
#            "NLO": 0.080719,
#            }

colours = { "Zboson" : {
    "LO":  {  "CVetoBVeto"     : ROOT.kRed,
              "CFilterBVeto"   : ROOT.kGreen,
              "BFilter"        : ROOT.kBlue,

            },
    "NLO": {# "CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_NLO.hadd.CVetoBVeto.root"  ),
            # "CFilterBVeto" :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_NLO.hadd.CFilterBVeto.root"),
            # "BFilter"      :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_NLO.hadd.BFilter.root"     ),
            }
    },
            "Gamma" : {
    "LO":  {  "CVetoBVeto"     : ROOT.kRed,
              "CFilterBVeto"   : ROOT.kGreen,
              "BFilter"        : ROOT.kBlue,

            },
    "NLO": {#"CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.CVetoBVeto.root"  ),
            #"CFilterBVeto" :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.CFilterBVeto.root"),
            #"BFilter"      :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.BFilter.root"     ),
            }
    },#photon dict
            }
filein = { "Zboson" : {
    "LO":  {"CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_LO.hadd.CVetoBVeto.root"  ),
            "CFilterBVeto" :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_LO.hadd.CFilterBVeto.root"),
            "BFilter"      :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_LO.hadd.BFilter.root"     ),
            },
    "NLO": {# "CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_NLO.hadd.CVetoBVeto.root"  ),
            # "CFilterBVeto" :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_NLO.hadd.CFilterBVeto.root"),
            # "BFilter"      :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_Znunu_NLO.hadd.BFilter.root"     ),
            },
    },#zdict
           "Gamma" : {
        "LO":  {"CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_SinglePhoton_LO.hadd.CVetoBVeto.root"),
                "CFilterBVeto" :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_SinglePhoton_LO.hadd.CFilterBVeto.root"),
                "BFilter"      :ROOT.TFile("output/user.rsmith.v4.fixOR.Sherpa_CT10_SinglePhoton_LO.hadd.BFilter.root"),


            },#ROOT.TFile("output/ZbosonTruthTest.small.root"),#.Sherpa145.root"),
    "NLO": {#"CVetoBVeto"   :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.CVetoBVeto.root"  ),
            #"CFilterBVeto" :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.CFilterBVeto.root"),
            #"BFilter"      :ROOT.TFile("output/user.rsmith.v3.Sherpa_CT10_Znunu_NLO.hadd.BFilter.root"     ),
            }
    }#photon dict
}

histnames = [
"Zboson_refpt",
"Zboson_fspt",
"Zboson_refeta",
"Zboson_fseta",
# "Jet_fspt",
# "Jet_fseta",
# "Jet1_fspt",
# "Jet1_fseta",
# "Zboson_dRjet",
# "Zboson_dPhiJet",
# "Zboson_dRjmin",
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
stacks = {"Zboson":{
              "LO" :{},
              "NLO":{},
              },
          "Gamma":{
        "LO" :{},
        "NLO":{},
        }
          }
leg = ROOT.TLegend(0.7,0.7,0.9,0.9)
leg.SetFillStyle(0)
leg.SetBorderSize(0)

#for order in ["NLO"] :
#for order in ["LO","NLO"]:
for phys in xsecs.keys() :
    for order in ["LO"]:
        for histname in histnames :
            stacks[phys][order][histname] = ROOT.THStack("hs_"+phys+"_"+order+"_"+histname,"hs_"+phys+"_"+order+"_"+histname)

print "xsecs keys : "
print xsecs.keys()

from  __builtin__ import any as b_any

for phys  in xsecs.keys() :
#for phys  in ["Zboson"] :
    hists[phys] = {}
    for order in ["LO"]:#,"NLO"]:
        hists[phys][order] = {}

        for bfilt in bfilts[phys] :
            hists[phys][order][bfilt] = {}
            for plotdir in plotdirs[phys] :
                # fillcolor = fillcolor + 1
                # if fillcolor > 9 : fillcolor = 2
                hists[phys][order][bfilt][plotdir] = {}
        #        plotdir = "ZPt500"
                print "filein    : " + filein[phys][order][bfilt].GetName()
                evtsprocessed = filein[phys][order][bfilt].Get(plotdir+"/EvtsProcessed")
            #    evtsprocessed = 1000
                print "plotdir   : " + str( plotdir)
                print "lumi      : " + str( lumi   )
                print "nevnts    : " + str( evtsprocessed.GetBinContent(1))
                print "sumweight : " + str( evtsprocessed.GetBinContent(2))
                print "xsecs thing : " + str( xsecs[phys][order][bfilt])
#                if not b_any(phys in x for x in xsecs[phys][order][bfilt].keys()) : continue



                print "xsec      : " + str( xsecs[phys][order][bfilt][plotdir])
                if(evtsprocessed.GetBinContent(2) < 1) : continue
            #        normalisation[order] = lumi/evtsprocessed.GetBinContent(2)*xsecs[phys][order]*filteff[order]
                normalisation =  lumi/evtsprocessed.GetBinContent(2)*xsecs[phys][order][bfilt][plotdir]
                print "normalisation : " + str(normalisation)

                for histname in histnames:
                    #                if not histname in stacks[phys].keys():
                    print "histname : " + histname
                    hist = None
                    if(("Zboson" in histname) and ("Photon" in filein[phys][order][bfilt].GetName())):
                        hist = filein[phys][order][bfilt].Get(plotdir+"/"+histname.replace("Zboson","Photon"))
                    else :
                        hist = filein[phys][order][bfilt].Get(plotdir+"/"+histname)

                    hist.Scale(normalisation)
                    hist.SetLineColor(ROOT.kBlack)
                    print "hist getEntries : " + str(hist.GetEntries())
                    hist.SetFillColor(colours[phys][order][bfilt])
                #                hist.SetFillColor(fillcolor)
                    myclone = hist.Clone()
                    stacks[phys][order][histname].Add(myclone)
                    hists[phys][order][bfilt][plotdir][histname] = myclone
#                    if len(hists[phys][order][bfilt][plotdir])==1:



#for order in ["LO","NLO"]:
outfile = ROOT.TFile("ReweightingFiles/reweightinghistos.root", "RECREATE")

#for order in ["LO","NLO"]:
#for phys in xsecs.keys() :
ROOT.gStyle.SetOptStat(0)


for order in ["LO"]:
#for order in ["NLO"]:
    legendAdded = False
    for histname in histnames:
            #           if not b_any(phys in x for x in xsecs[phys][order][bfilt].keys()) : continue
        c = ROOT.TCanvas(phys+histname+"canvas")
#        c.SetLogy()
        c.SetLogx("pt" in histname)
        c.Divide(1,2,0,0)
        ROOT.SetOwnership(c, False)

        pad1 = ROOT.TPad("pad1", "pad1",0.0,0.35,1.0,1.0 , 0)
        pad2 = ROOT.TPad("pad2", "pad2",0.0,0.0 ,1.0,0.35, 0)

        pad1.SetBottomMargin(0)
        pad2.SetTopMargin(0)

        pad1.Draw()
        pad2.Draw()
#        c.cd(1)

        histGamma  = stacks["Gamma"][order][histname].GetStack().Last().Clone() #return as th1
        histZboson = stacks["Zboson"][order][histname].GetStack().Last().Clone() #return as th1

#        histGamma .Sumw2()
#        histZboson.Sumw2()
#        if not "Njet" in histname :
#            histGamma.Rebin(4)
#            histZboson.Rebin(4)

        pad1.cd()
        pad1.SetGrid()
        pad1.SetLogy()


        leg.Draw()
#        histGamma.GetXaxis().SetNdivisions(500);

        histGamma.GetXaxis().SetTitle("")
#        histGamma.GetYaxis().SetTitle("a.u.")
        histGamma.SetFillColor(ROOT.kYellow)
#        histGamma.SetMarkerStyle(21)

        histZboson.SetMarkerStyle(21)
        histZboson.SetFillColor(ROOT.kWhite)

        if( not legendAdded ) :
            leg.AddEntry(histZboson,"Z + jets")
            leg.AddEntry(histGamma, "#gamma + jets")
            legendAdded = True

        # histGamma .Scale(1/histGamma.Integral())
        # histZboson.Scale(1/histZboson.Integral())

        # ratio  = histZboson.Clone()
        # ratio2 = histGamma.Clone()


        histGamma.Draw("hist")
        histZboson.Draw("same")
        leg.Draw();

        pad2.cd()
        pad2.SetGrid()
#        pad1.Update()

        ratio = histZboson.Clone()
#        ratio.Sumw2()
        ratio.Divide(histGamma)
        ratio.SetMarkerStyle(21)
        ratio.SetMinimum(0.)
        ratio.SetMaximum(.5)
#        ratio.GetXaxis().SetTitle()
        ratio.SetBit(ROOT.TH1.kNoTitle)
#        ratio.GetXaxis().SetNdivisions(500);
#        ratio.GetYaxis().SetNdivisions(-500);
        ratio.GetYaxis().SetTitle("Z / gamma ")
        ratio.GetYaxis().SetTitleSize(.10)

        ratio.GetXaxis().SetLabelSize(.10)
        ratio.GetYaxis().SetLabelSize(.10)

        ratio.Draw("ep")
        ratio.Write()

        c.cd()
        c.SaveAs("ReweightingFiles/"+histname+order+".eps")



#  LocalWords:  filein
