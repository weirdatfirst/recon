#!/usr/bin/env python
# title           :recon.pcy
# description     :Preform initial recon
# author          :
# date            :
# version         :0.1
# usage           :recon.py domain
# =======================================================================


# AMASS kept freaking out so switched over to Sublist3r

import sys, os
import fileinput
import shlex

if len(sys.argv) != 2:
    print("Usage: %s <domain>" % (sys.argv[0]))
    sys.exit(0)

domain = sys.argv[1]
# amassoutput = domain + "/Amass/amass.txt"
sublistoutput = domain + "/Sublist3r/Sublist3r.txt"


# Define folder setup
def createfolders():
    folders = ["NMAP", "Dig", "EyeWitness", "Sublist3r", "gobuster", "Nikto", "masscan"]
    for x in folders:
        j = domain + "/" + x + "/"
        try:
            os.makedirs(j)
        except OSError:
            pass


# Define amass
def amassrun():
    amassvm = "sudo amass -freq 480 -d " + domain + " -o " + amassoutput
    os.system(amassvm)


def Sublist3r():
    sublistcommand = "sudo python /root/tools/Sublist3r/sublist3r.py -d " + domain + " -o " + sublistoutput
    os.system(sublistcommand)


# print sublistcommand

# Define Dig
def digrun():
    rundig = "sudo dig -f " + sublistoutput + " > " + domain + "/Dig/dig.txt"
    os.system(rundig)


# Define Format the IPS for NMAP
def formatdigips():
    dig_ips_formated = "sudo cat " + domain + "/Dig/dig.txt" + " | grep -v SERVER | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort -u > " + domain + "/Dig/digformated.txt"
    os.system(dig_ips_formated)


# Define NMAP PORTS 80, 8080, and 443
def nmapwebrun():
    nmap_fullcommand = "sudo nmap -v -p 80,8080,443 -oA " + domain + "/NMAP/webonly_nmap -iL " + domain + "/Dig/digformated.txt"
    os.system(nmap_fullcommand)


# Define NMAP
def nmapfullrun():
    nmap_fullcommand = "sudo nmap -p- -oA " + domain + "/NMAP/allport_nmap -iL " + domain + "/Dig/digformated.txt"
    os.system(nmap_fullcommand)

# Define Massscan
def masscanrun():
    nmap_fullcommand = "sudo masscan " + domain + "/masscan/allport_nmap -iL " + domain + "/Dig/digformated.txt"
    os.system(nmap_fullcommand)


# Define Gobuster run
def gobusterrun():
    fh = open("parsed_xml.txt")
    for line in fh:
        editline = line.rstrip('\n')
        output = line.translate(None, '/')
        gobustercommand = "sudo gobuster -e -k -fw -t 100 -u " + editline + " -w wordlists/common.txt -o " + domain + "/gobuster/" + output
        os.system(gobustercommand)
    # print gobuster
    fh.close


# Define EyeWitness
def eyewitenessrun():
    eyewitnesscommand = "sudo python /root/tools/EyeWitness/EyeWitness.py --headless --no-prompt -x " + domain + "/NMAP/webonly_nmap.xml" + " -d " + domain + "/EyeWitness/"
    os.system(eyewitnesscommand)


# define Nikto
def niktorun():
    fh = open("parsed_xml.txt")
    for line in fh:
        editline = line.rstrip('\n')
        output = line.translate(None, '/')
        niktocommand = "sudo nikto -h " + editline + " -Display V -F htm -output " + domain + "/Nikto/" + output + ".html"
        os.system(niktocommand)
    # print niktocommand
    fh.close


# Define cleanup
def cleanup():
    removethese = ["parsed_xml.txt", "geckodriver.log"]
    for r in removethese:
        os.remove(r)


# define spider


# execute code below
createfolders()
# amassrun() maybe come back to someday
Sublist3r()
digrun()
formatdigips()
nmapwebrun()
# nmaprun() # Only enable if you want all ports. Takes a long time!!
eyewitenessrun()
gobusterrun()
niktorun()
cleanup()
