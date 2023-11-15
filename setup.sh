#!/bin/sh
if [[ $HOSTNAME == *"tamsa2"* ]]; then
    echo +++\> Setting up @ TAMSA2 
    export WORKDIR=$PWD
    echo ++\> WORKDIR=$WORKDIR
    source /cvmfs/sft.cern.ch/lcg/releases/LCG_102cuda/Python/3.9.12/x86_64-centos7-gcc8-opt/Python-env.sh
	echo ++\> Python Environment Set
	source /cvmfs/sft.cern.ch/lcg/releases/LCG_102cuda/tbb/2020_U2/x86_64-centos7-gcc8-opt/tbb-env.sh
	echo ++\>  ThreadBuildingBlocks Environment Set
    source /cvmfs/sft.cern.ch/lcg/releases/LCG_102cuda/ROOT/6.26.04/x86_64-centos7-gcc8-opt/ROOT-env.sh
	echo ++\>  ROOT Environment Set
elif [[ $HOSTNAME == *"cms2"* ]]; then
	echo +++\> Setting up @ CMS2 
	export WORKDIR=$PWD
	echo ++\> WORKDIR=$WORKDIR
	source $HOME/miniconda3/bin/activate
	conda activate torch
fi

alias compile-root="/usr/bin/g++ `root-config --cflags --ldflags --glibs`"

export PYTHONPATH="${PYTHONPATH}:${WORKDIR}"
export PYTHONPATH="${PYTHONPATH}:${WORKDIR}/lib/python"
