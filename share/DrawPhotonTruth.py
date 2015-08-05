import ROOT
import atlasStyle

# ptcuts = {211:[140,280,500,1000,2000,4000],
#           145:[140,280,500]}
ptcuts = {211:[140],
          145:[140]}

xsecs = { 211:{"GammaPt0":    35002000.,
               "GammaPt70":    3135200.,
               "GammaPt140":    249370.,
               "GammaPt280":     13874.,
               "GammaPt500":       938.19,
               "GammaPt1000":       19.046,
               "GammaPt2000":        0.082153,
               "GammaPt4000":        0.0000025431},
          145:{"GammaPt140":  352610.,
               "GammaPt280":   19356.,
               "GammaPt500":    1384.6,
               }
          }

filteff = {
    "CVetoBVeto": {
        211: {"GammaPt0":     0.41028,
              "GammaPt70":    0.39960,
              "GammaPt140":   0.41049,
              "GammaPt280":   0.41834,
              "GammaPt500":   0.38226,
              "GammaPt1000":  0.37036,
              "GammaPt2000":  0.38030,
              "GammaPt4000":  0.40351,
              },
        145: {"GammaPt140":   0.42556,
              "GammaPt280":   0.40983,
              "GammaPt500":   0.39686,
              }
        },
    "CFilterBVeto": {
        211: {"GammaPt0":     0.48609,
              "GammaPt70":    0.48199,
              "GammaPt140":   0.50284,
              "GammaPt280":   0.47349,
              "GammaPt500":   0.47148,
              "GammaPt1000":  0.46691,
              "GammaPt2000":  0.45148,
              "GammaPt4000":  0.41614,
              },
        145: {"GammaPt140":   0.47310,
              "GammaPt280":   0.46833,
              "GammaPt500":   0.46546,
              }
        },
    "BFilter": {
        211: {"GammaPt0":     0.10752,
              "GammaPt70":    0.11728,
              "GammaPt140":   0.12874,
              "GammaPt280":   0.14069,
              "GammaPt500":   0.14811,
              "GammaPt1000":  0.15751,
              "GammaPt2000":  0.16549,
              "GammaPt4000":  0.14831,
              },
        145: {"GammaPt140":   0.10098,
              "GammaPt280":   0.12017,
              "GammaPt500":   0.13950,
              }
        }
}

colours = {"GammaPt0":     ROOT.kViolet-1,
           "GammaPt70":    ROOT.kBlue+2,
           "GammaPt140":   ROOT.kAzure+1,
           "GammaPt280":   ROOT.kGreen+2,
           "GammaPt500":   ROOT.kSpring,
           "GammaPt1000":  ROOT.kOrange,
           "GammaPt2000":  ROOT.kMagenta,
           "GammaPt4000":  ROOT.kRed,
}

histnames = [
"Photon_refpt",
"Photon_fspt",
"Photon_refeta",
"Photon_fseta",
"Jet_fspt",
"Jet_fseta",
"Jet1_fspt",
"Jet1_fseta",
"Photon_dRjet",
"Photon_dPhiJet",
"Photon_dRjmin",
"Njet20",
"Njet30",
"Njet60",
"Njet100",
"Njet250",
]

for sherpaversion in [145,211]:
    hists = {}
    normalisation = {}
    lumi = 1
    stacks = {}
    leg = ROOT.TLegend(0.7,0.7,0.9,0.9)
    leg.SetFillStyle(0)
    leg.SetBorderSize(0)
    for flavour in ["BFilter","CFilterBVeto","CVetoBVeto"]:
        filein = ROOT.TFile("PhotonTruth.{1}_140_280.Sherpa{0}.root".format(sherpaversion,flavour))
        for cut in reversed(ptcuts[sherpaversion]):
            plotdir = "GammaPt{0}".format(cut)
            evtsprocessed = filein.Get(plotdir+"/EvtsProcessed")
            evtweightsum = evtsprocessed.GetBinContent(2)
            normalisation[plotdir] = 0.
            if evtweightsum>0.:
                normalisation[plotdir] = lumi/evtweightsum*xsecs[sherpaversion][plotdir]*filteff[flavour][sherpaversion][plotdir]
    #            normalisation[plotdir] = lumi/evtweightsum

            if flavour=="BFilter": hists[plotdir] = {}
            for histname in histnames:
                if not histname in stacks.keys():
                    stacks[histname] = ROOT.THStack("hs_"+histname,histname)
                hist = filein.Get(plotdir+"/"+histname)
                hist.Scale(normalisation[plotdir])
                hist.SetLineColor(ROOT.kBlack)
                hist.SetFillColor(colours[plotdir])
                print plotdir, histname, flavour
                if flavour=="BFilter": 
                    stacks[histname].Add(hist)
                    hist.SetDirectory(0)
                    hists[plotdir][histname] = hist
                else:
                    hists[plotdir][histname].Add(hist)
                if len(hists[plotdir])==1:
                    leg.AddEntry(hist,plotdir,'f')

    c = ROOT.TCanvas("photontruth")
    c.SetLogy()
    for histname in histnames:
        #c.SetLogx("pt" in histname)
        stacks[histname].Draw("hist")
        stacks[histname].SetMinimum(1e-10)
        stacks[histname].SetMaximum(1e7)
        stacks[histname].GetXaxis().SetTitle(histname)
        stacks[histname].GetYaxis().SetTitle("Events / {0} ifb".format(lumi))
        leg.Draw()
        c.SaveAs("Yplots/sherpa{0}/{1}.eps".format(sherpaversion,histname))
