import ROOT

import os
from os import path
# Workaround to fix threadlock issues with GUI
ROOT.PyConfig.StartGuiThread = False
import logging
logging.basicConfig(level=logging.INFO)

def intersect(a, b) :
    return list(set(a) & set(b))

filein = {
    "Gamma"  : ROOT.TFile("output/outGammaStack.root"),
    "Zboson" : ROOT.TFile("output/outZStack.root")
}

gammaHists  = filein["Gamma" ].GetListOfKeys()
zBosonHists = filein["Zboson"].GetListOfKeys()

filteredListGamma = []
filteredListZboson = []
for hist in gammaHists :
    if(len(hist.GetName().split("_LO_")) > 1 ):
        filteredListGamma.append( hist.GetName().split("_LO_")[1])#[ hist.GetName().split("_LO_")[1] for hist in gammaHists]

for hist in zBosonHists :
    if(len(hist.GetName().split("_LO_")) > 1 ):
        filteredListZboson.append( hist.GetName().split("_LO_")[1])#[ hist.GetName().split("_LO_")[1] for hist in gammaHists]


c1 = ROOT.TCanvas("ratio")

print intersect(filteredListGamma,filteredListZboson)

for stackname in intersect(filteredListGamma,filteredListZboson) :

    print "stack object name : " + stackname
    lostub  = "hs_LO_"
    nlostub = "hs_NLO_"

 #   if(filein["Gamma"].GetListOfKeys().Contains(lostub+stackname)) :
    stackGamma  = filein["Gamma"] .Get(lostub+stackname)
#    if(filein["Zboson"].GetListOfKeys().Contains(lostub+stackname)) :
    stackZboson  = filein["Zboson"] .Get(lostub+stackname)
    # if(filein["Gamma"].GetListOfKeys().Contains(nlostub+stackname)) :
    #     stackGamma  = filein["Gamma"] .Get(nlostub+stackname)
    # if(filein["Zboson"].GetListOfKeys().Contains(nlostub+stackname)) :
    #     stackZboson  = filein["Zboson"] .Get(nlostub+stackname)

    print stackGamma .GetName()
    print stackZboson.GetName()


    histGamma  = stackGamma .GetStack().Last().Clone()#return as th1 for ratio
    histZboson = stackZboson.GetStack().Last().Clone() #return as th1

    histGamma .Sumw2()
    histZboson.Sumw2()

    histGammaScale  = 1.#./histGamma .Integral()
    histZbosonScale = 1.#./histZboson.Integral()

    histZboson.Divide(histGamma)

    histZboson.SetFillColor(0)

    histZboson.Draw("E")
    histZboson.SetMinimum(0.)
    histZboson.SetMaximum(5.)
    histZboson.GetYaxis().SetTitle("Z / gamma ")


    c1.SaveAs("ratioPlots/ratio_"+stackname+".eps")

