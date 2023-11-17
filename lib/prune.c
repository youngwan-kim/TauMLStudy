#include <TFile.h>
#include <TTree.h>
#include <TString.h>

int prune(TString filename, TString outname){

    vector<TString> list = {"Tau_pt","Tau_eta","Tau_phi","Tau_mass",
                            "Tau_decayMode","Tau_chargedIso",
                            "FatJet_pt","FatJet_eta","FatJet_phi","FatJet_mass",
                            "FatJet_nConstituents","FatJet_tau3",
                            "Jet_pt","Jet_eta","Jet_phi","Jet_mass","Jet_nConstituents",
                            "Jet_chEmEF","Jet_chHEF","Jet_neEmEF","Jet_neHEF",
                            "SubJet_pt","SubJet_eta","SubJet_phi","SubJet_mass",
                            "GenJet_pt","GenJet_eta","GenJet_phi","GenJet_mass",
                            "GenJet_partonFlavour","GenJet_hadronFlavour",
                            "MET_pt","MET_phi"};
    TFile oldfile(filename);
    TTree *oldtree;
    oldfile.GetObject("Events", oldtree);

    oldtree->SetBranchStatus("*", 0);

    for (auto activeBranchName : list)
        oldtree->SetBranchStatus(activeBranchName, 1);

    TFile newfile(outname+".root", "recreate");
    auto newtree = oldtree->CloneTree();

    newtree->Print();
    newfile.Write();

    return 0;

}