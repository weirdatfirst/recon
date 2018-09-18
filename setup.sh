#!/bin/bash
sudo apt-get install python-pip python-dev build-essential -y
pip install --upgrade pip -y
git clone https://github.com/weirdatfirst/EyeWitness.git
git clone https://github.com/weirdatfirst/Sublist3r.git
sudo rm /etc/apt/sources.list
echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list.d/kali.list
apt-get get update
sudo sh EyeWitness/setup/setup.sh -y
sudo pip install -r Sublist3r/requirements.txt
sudo apt-get install -y nmap 
sudo apt-get isntall -y dirb
sudo apt-get install -y nikto

