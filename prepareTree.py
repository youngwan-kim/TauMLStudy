import os, shutil
import argparse
import ROOT

WORKDIR = os.getenv("WORKDIR")
ROOT.gSystem.Load(f"{WORKDIR}/lib/obj/prepareTree.so")
ROOT.EnableImplicitMT(4)

parser = argparse.ArgumentParser()
parser.add_argument("--era", required=True, type=str, help="era")
parser.add_argument("--channel", required=True, type=str, help="channel")
parser.add_argument("--signal", required=True, type=str, help="signal mass point")
parser.add_argument("--sample", required=True, type=str, help="sample name")
args = parser.parse_args()

Systematics = {
        "prompt": ["Central", "MuonIDSFUp", "MuonIDSFDown", "DblMuTrigSFUp", "DblMuTrigSFDown",
                              "JetEnUp", "JetEnDown", "JetResUp", "JetResDown"],
        "nonprompt": ["Central", "NonpromptUp", "NonpromptDown"]
}

