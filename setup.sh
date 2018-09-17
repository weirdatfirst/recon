#!/bin/bash
git clone https://github.com/weirdatfirst/EyeWitness.git
sh EyeWitness/setup/setup.sh -y
apt install snapd -y
systemctl start snapd
export PATH=$PATH:/snap/bin
snap install amass