#include <TFile.h>
#include <TTree.h>
#include <TH1F.h>
#include <TCanvas.h>

void drawHistogram() {
    // Open the ROOT file containing the TTree
    TFile *file = new TFile("test2.root", "READ");

    // Check if the file is opened successfully
    if (!file || file->IsZombie()) {
        std::cerr << "Error: Could not open the ROOT file!" << std::endl;
        return;
    }

    // Get the TTree from the file
    TTree *tree = dynamic_cast<TTree*>(file->Get("Events"));

    // Check if the TTree is found
    if (!tree) {
        std::cerr << "Error: Could not retrieve the TTree!" << std::endl;
        file->Close();
        return;
    }

    // Create a histogram for the branch "Tau_eta"
    TH1F *histogram = new TH1F("histogram", "Tau_eta Distribution", 60, -3, 3);

    // Fill the histogram from the TTree
    tree->Draw("Tau_eta>>histogram");

    // Create a canvas to display the histogram
    TCanvas *canvas = new TCanvas("canvas", "Tau_eta Histogram", 800, 600);
    histogram->Draw();

    // Save the canvas as an image (optional)
    // canvas->SaveAs("Tau_etaHistogram.png");

    canvas->SetLogy();
   
    canvas->SaveAs("Tau_etaHistogram_test.png");
    // Close the ROOT file
    file->Close();
}
