#!/bin/bash

#Use for Installs on Kali
sudo apt-get install python-pip python-dev build-essential -y
pip install --upgrade pip -y
git clone https://github.com/weirdatfirst/EyeWitness.git
git clone https://github.com/weirdatfirst/Sublist3r.git
sudo sh EyeWitness/setup/setup.sh -y
sudo pip install -r Sublist3r/requirements.txt
