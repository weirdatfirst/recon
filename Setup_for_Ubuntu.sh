#!/bin/bash
sudo echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" > /etc/apt/sources.list
sudo apt-get update

sudo apt-get install python-pip python-dev build-essential -y
sudo pip install --upgrade pip -y
git clone https://github.com/weirdatfirst/EyeWitness.git
git clone https://github.com/weirdatfirst/Sublist3r.git
cd EyeWitness/setup
sudo sh setup.sh -y
sudo pip install -r Sublist3r/requirements.txt -y
sudo apt-get install nikto -y
sudo apt-get install gobuster -y
sudo apt-get install nmap -y
