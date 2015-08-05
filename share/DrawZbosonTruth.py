import ROOT
import atlasStyle

xsecs = {"LO":    10471000.,
         "NLO":   12472000.,
         }

filteff = {"LO":  0.039883,
           "NLO": 0.080719,
           }

colours = {"LO" : ROOT.kRed,
           "NLO": ROOT.kBlue,
}

filein = {
    "LO":  ROOT.TFile("ZbosonTruth.Sherpa145.root"),
    "NLO": ROOT.TFile("ZbosonTruth.Sherpa211.root"),
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
]

hists = {}
normalisation = {}
lumi = 1
stacks = {}
leg = ROOT.TLegend(0.7,0.7,0.9,0.9)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
for order in ["LO","NLO"]:
    plotdir = "ZPt140"
    evtsprocessed = filein[order].Get(plotdir+"/EvtsProcessed")
    print plotdir, lumi, evtsprocessed.GetBinContent(1), evtsprocessed.GetBinContent(2), xsecs[order], filteff[order]
    normalisation[order] = lumi/evtsprocessed.GetBinContent(2)*xsecs[order]*filteff[order]

    hists[order] = {}
    for histname in histnames:
        if not histname in stacks.keys():
            stacks[histname] = ROOT.THStack("hs_"+histname,histname)
        hist = filein[order].Get(plotdir+"/"+histname)
        hist.Scale(normalisation[order])
        hist.SetLineColor(ROOT.kBlack)
        hist.SetFillColor(colours[order])
        stacks[histname].Add(hist)
        hists[order][histname] = hist
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
