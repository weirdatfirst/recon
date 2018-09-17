#!/bin/bash
git clone https://github.com/weirdatfirst/EyeWitness.git
git clone https://github.com/weirdatfirst/Sublist3r.git
sh EyeWitness/setup/setup.sh -y
pip install -r Sublist3r/requirements.txt