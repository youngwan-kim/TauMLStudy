import os
import ROOT

WORKDIR = os.getenv("WORKDIR")
ROOT.gSystem.Load(f"{WORKDIR}/lib/prune_c.so")

root_directory = "/gv0/Users/youngwan/NANOAOD/RunIISummer20UL17NanoAODv9"

for root, dirs, files in os.walk(root_directory):
    if root.count(os.sep) - root_directory.count(os.sep) == 4:
        for file in files:
            if file.endswith(".root"):
                file_path = os.path.join(root, file)
                outname = file_path.split("/")[6].rsplit("_",2)[0]
                print("Pruning file:", outname)
                ROOT.prune(file_path,f"{WORKDIR}/data/PrunedNano/{outname}_NanoAODv9")