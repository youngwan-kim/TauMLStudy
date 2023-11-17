#include <TFile.h>
#include <TTree.h>

int printBranch(){

    TFile* f = TFile::Open("../data/WR2000_N100_NanoAODv9.root");
    TTree* t = (TTree*) f->Get("Events");
    t->Print();

    return 0;
}