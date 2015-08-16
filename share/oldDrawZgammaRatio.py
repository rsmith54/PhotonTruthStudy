import ROOT
import atlasStyle

# ptcuts = {"Gamma_211":[70,140,280,500,1000,2000,4000],
#           "Gamma_145":[140,280,500]}
ptcuts = {"Gamma_211":[140,280,500,1000,2000,4000],
          "Gamma_145":[140,280,500],
          "Z_211":[140,280,500,700,1000],
          "Z_145":[140,280,500]}

xsecs = { "Gamma_211":{0:    35002000.,
                       70:    3135200.,
                       140:    249370.,
                       280:     13874.,
                       500:       938.19,
                       1000:       19.046,
                       2000:        0.082153,
                       4000:        0.0000025431
                       },
          "Gamma_145":{140:    352610.,
                       280:     19356.,
                       500:      1384.6,
                        },
          # "Z_145":           10471000.,
          # "Z_211" :          12472000.,
          "Z_145":    {0:    10471000.,
                       70:     377430.,
                       140:     60230.,
                       280:      4664.9,
                       500:       378.43,
                        },
          "Z_211":    {0:    11933000.,
                       70:     428250.,
                       140:     65796.,
                       280:      4837.8,
                       500:       293.29,
                       700:        53.341,
                       1000:        7.6507,
                       },
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
              "ZPt0":         0.77837,
              "ZPt70":        0.64863,
              "ZPt140":       0.60566,
              "ZPt280":       0.60566, # stat error?
#              "ZPt280":       0.49112,
              "ZPt500":       0.54643,
              "ZPt700":       0.57944,
              "ZPt1000":       0.57944, # stat error?
#              "ZPt1000":      0.35762,
              },
        145: {"GammaPt140":   0.42556,
              "GammaPt280":   0.40983,
              "GammaPt500":   0.39686,
              "ZPt0":         0.63727,
              "ZPt70":        0.50634,
              "ZPt140":       0.47131,
              "ZPt280":       0.44226,
              "ZPt500":       0.41562,
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
              "ZPt0":         0.14008,
              "ZPt70":        0.21209,
              "ZPt140":       0.22794,
              "ZPt280":       0.23583,
              "ZPt500":       0.25074,
              "ZPt700":       0.20360,
              "ZPt1000":      0.19538,
              },
        145: {"GammaPt140":   0.47310,
              "GammaPt280":   0.46833,
              "GammaPt500":   0.46546,
              "ZPt0":         0.32350,
              "ZPt70":        0.39045,
              "ZPt140":       0.40475,
              "ZPt280":       0.43294,
              "ZPt500":       0.43676,
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
              "ZPt0":         0.079239,
              "ZPt70":        0.12738,
              "ZPt140":       0.13435,
#              "ZPt280":       0.074043,
              "ZPt280":       0.12721, # stat error?
              "ZPt500":       0.12721,
              "ZPt700":       0.17925,
              "ZPt1000":      0.13404,
              },
        145: {"GammaPt140":   0.10098,
              "GammaPt280":   0.12017,
              "GammaPt500":   0.13950,
              "ZPt0":         0.039883,
              "ZPt70":        0.10310,
              "ZPt140":       0.11957,
              "ZPt280":       0.13493,
              "ZPt500":       0.14685,
              }
        }
}

colours = {
    "Gamma_145":  ROOT.kBlue,
    "Gamma_211":  ROOT.kGreen+2,
    "Z_145" :     ROOT.kRed,
    "Z_211":      ROOT.kMagenta,
}

filein = {}
# filein = {
#     "Z_145":  ROOT.TFile("ZbosonTruth.Sherpa145.root"),
#     "Z_211": ROOT.TFile("ZbosonTruth.Sherpa211.root"),
# }
for sherpaversion in [145,211]:
    for flavour in ["BFilter","CFilterBVeto","CVetoBVeto"]:
        filein["Gamma_{0}{1}".format(sherpaversion,flavour)] = ROOT.TFile("PhotonTruth.{1}.Sherpa{0}.root".format(sherpaversion,flavour))
        filein["Z_{0}{1}".format(sherpaversion,flavour)] = ROOT.TFile("ZbosonTruth.{1}.Sherpa{0}.root".format(sherpaversion,flavour))

histnames = [
"{0}_refpt",
"{0}_fspt",
"{0}_fset",
"{0}_refeta",
"{0}_fseta",
"{0}_dRjet",
"{0}_dPhiJet",
"{0}_dRjmin",
"Jet_fspt",
"Jet_fseta",
"Jet1_fspt",
"Jet1_fseta",
"Njet20",
"Njet30",
"Njet60",
"Njet100",
"Njet250",
]

hists = {}
normalisation = {}
lumi = 1
for sherpaversion in [145,211]:
    for flavour in ["BFilter","CFilterBVeto","CVetoBVeto"]:
        key = "Gamma_{0}".format(sherpaversion)
        hists[key] = {}
        # Photon histograms
        for cut in ptcuts["Gamma_{0}".format(sherpaversion)]:
            plotdir = "GammaPt{0}".format(cut)
            print plotdir, sherpaversion, flavour, filein[key+flavour].GetName()
            evtsprocessed = filein[key+flavour].Get(plotdir+"/EvtsProcessed")
            evtweightsum = evtsprocessed.GetBinContent(2)
            normalisation = 0.
            if evtweightsum>0.:
                normalisation = lumi/evtweightsum*xsecs[key][cut]*filteff[flavour][sherpaversion][plotdir]
#                print normalisation

            for histtmp in histnames:
                histname = histtmp.format("Photon")
                hist = filein[key+flavour].Get(plotdir+"/"+histname)
                hist.Scale(normalisation)
                hist.SetLineColor(colours[key])
                hist.SetMarkerColor(colours[key])
                hist.SetMarkerSize(0.6)
                histkey = "Gamma_{0}_{1}".format(sherpaversion,histname)
#                print plotdir, histkey,histname,hist.Integral()
                if not histname in hists[key].keys():
                    hists[key][histname] = hist.Clone(histkey)
                else:
                    hists[key][histname].Add(hist)
#                print hists[key][histname].Integral()

        key = "Z_{0}".format(sherpaversion)
        hists[key] = {}
        # Zboson histograms
        for cut in ptcuts["Z_{0}".format(sherpaversion)]:
            plotdir = "ZPt{0}".format(cut)
            print plotdir, sherpaversion, flavour, filein[key+flavour].GetName()
            evtsprocessed = filein[key+flavour].Get(plotdir+"/EvtsProcessed")
            evtweightsum = evtsprocessed.GetBinContent(2)
            normalisation = 0.
            if evtweightsum>0.:
                print flavour, sherpaversion, plotdir
                normalisation = lumi/evtweightsum*xsecs[key][cut]*filteff[flavour][sherpaversion][plotdir]
#                print normalisation

            for histtmp in histnames:
                histname = histtmp.format("Zboson")
                print plotdir, histname
                hist = filein[key+flavour].Get(plotdir+"/"+histname)
                hist.Scale(normalisation)
                hist.SetLineColor(colours[key])
                hist.SetMarkerColor(colours[key])
                hist.SetMarkerSize(0.6)
                histkey = "Z_{0}_{1}".format(sherpaversion,histname)
#                print plotdir, histkey,histname,hist.Integral()
                if not histname in hists[key].keys():
                    hists[key][histname] = hist.Clone(histkey)
                else:
                    hists[key][histname].Add(hist)
#                print hists[key][histname].Integral()

c1 = ROOT.TCanvas("Zgamma")
c1.SetLogy()
leg1 = ROOT.TLegend(0.65,0.6,0.9,0.9)
leg1.SetBorderSize(0)
leg1.SetFillStyle(0)

c2 = ROOT.TCanvas("RZgamma")
leg2 = ROOT.TLegend(0.65,0.6,0.9,0.9)
leg2.SetBorderSize(0)
leg2.SetFillStyle(0)

xsecrat = {}
for histtmp in histnames:
    zrat = None
    grat = None
    for sherpaversion in [145,211]:
        xsecrat[sherpaversion] = None
        for proc in ["Z","Gamma"]:
            histname = histtmp.format(proc).replace("Gamma","Photon").replace("Z","Zboson")
            key = "{0}_{1}".format(proc,sherpaversion)
            hist = hists[key][histname]
            hist.GetYaxis().SetRangeUser(1e-2,1e5)
            if(histname.endswith("fset") or "pt" in histname): hist.GetXaxis().SetRangeUser(100,2000)
            # hist.GetYaxis().SetRangeUser(1,20)
            # if(histname.endswith("fset") or "pt" in histname): hist.GetXaxis().SetRangeUser(500,2000)
            hist.GetXaxis().SetTitle(histname)
            hist.GetYaxis().SetTitle("Events / {0} ifb".format(lumi))
            if proc == "Z":
                xsecrat[sherpaversion] = hist.Clone("RZG_{0}_{1}".format(sherpaversion,histname))
                xsecrat[sherpaversion].GetYaxis().SetRangeUser(0.,2.)
                xsecrat[sherpaversion].GetYaxis().SetTitle("R_{#sigma} = #sigma(Z_{#nu#nu}) / #sigma(#gamma)")
                if sherpaversion==145:
                    zrat = hist.Clone("RZ_{0}_{1}".format(sherpaversion,histname))
                    zrat.GetYaxis().SetTitle("R_{Z} = #sigma(Z_{#nu#nu}) (Sherpa 1.4.5) / #sigma(Z_{#nu#nu}) (Sherpa 2.1.1)")
                else:
                    zrat.Divide(hist)
            else:
                xsecrat[sherpaversion].Divide(hist)
                if sherpaversion==145:
                    grat = hist.Clone("RG_{0}_{1}".format(sherpaversion,histname))
                    grat.GetYaxis().SetTitle("R_{#gamma} = #sigma(#gamma) (Sherpa 1.4.5) / #sigma(Z_{#nu#nu}) (#gamma)")
                else:
                    grat.Divide(hist)
            c1.cd()
            if key == "Z_145":
                hist.Draw("pe")
            else:
                hist.Draw("pesame")
            leg1.AddEntry(hists[key][histname],key,'l')
        c2.cd()
        if sherpaversion == 145:
            xsecrat[sherpaversion].Draw("hist")
        else:
            xsecrat[sherpaversion].Draw("histsame")
        leg2.AddEntry(xsecrat[sherpaversion],'Sherpa {0}'.format(sherpaversion),'l')

    doublerat = xsecrat[145].Clone("RR_{0}".format(histname))
    doublerat.Divide(xsecrat[211])
    doublerat.GetYaxis().SetTitle("R_{#sigma} (Sherpa 1.4.5) / R_{#sigma} (Sherpa 2.1.1)")
    doublerat.SetLineColor(ROOT.kBlack)
    doublerat.SetLineStyle(ROOT.kDashed)
    doublerat.SetMarkerColor(ROOT.kBlack)
    doublerat.SetMarkerSize(0.6)
    doublerat.Draw("histsame")
    leg2.AddEntry(doublerat,'R(#sigma) 1.4.5 / 2.1.1','l')
    #
    zrat.SetLineStyle(ROOT.kDashed)
    zrat.SetLineColor(ROOT.kOrange+1)
    zrat.SetMarkerColor(ROOT.kOrange+1)
    zrat.SetMarkerSize(0.6)
    zrat.Draw("histsame")
    leg2.AddEntry(zrat,'Z 1.4.5 / 2.1.1','l')
    #
    grat.SetLineStyle(ROOT.kDashed)
    grat.SetMarkerSize(0.6)
    grat.Draw("histsame")
    leg2.AddEntry(grat,'#gamma 1.4.5 / 2.1.1','l')

    c1.cd()
    leg1.Draw()
#    c1.SetLogx("pt" in histname or histname.endswith("fset"))
    c1.SaveAs("ZYplots/{0}.eps".format(histtmp.format("Boson")))
    leg1.Clear()
    c2.cd()
    leg2.Draw()
#    c2.SetLogx("pt" in histname or histname.endswith("fset"))
    c2.SaveAs("ZYplots/{0}_rat.eps".format(histtmp.format("Boson")))
    leg2.Clear()
