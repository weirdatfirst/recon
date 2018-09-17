#!/usr/bin/env python
#title           :recon.pcy
#description     :Preform initial recon
#author          :
#date            :
#version         :0.1
#usage           :recon.py domain
#=======================================================================
import sys, os
import pyperclip
import fileinput

if len(sys.argv) != 2:
    print "Usage: %s <domain>" % (sys.argv[0])
    sys.exit(0) 

domain = sys.argv[1]


#Define amass
def amassrun():
    amassoutput = domain + "_amass.txt"
    amassvm = "amass -freq 480 -d " + domain + " -o " + amassoutput
    os.system(amassvm) 

#Define Dig
def digrun():    
    rundig = "dig -f " + amassoutput + " > " + domain + "_dig.txt"
    os.system(rundig)

#Define Format the IPS for NMAP
def formatdigips():
    dig_ips_formated = "cat " + domain + "_dig.txt" + " | grep -v SERVER | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort -u > " + domain + "_digformated.txt"
    os.system(dig_ips_formated)

#Define NMAP PORTS 80, 8080, and 443
def nmapwebrun():
    nmap_fullcommand = "nmap -v -p 80,8080,443 -oA " + domain + "_webonly_nmap -iL " + domain + "_digformated.txt"
    os.system(nmap_fullcommand)
       
#Define NMAP
def nmapfullrun():
    nmap_fullcommand = "nmap -v -p 1-65535 -oA " + domain + "_allport_nmap -iL " + domain + "_digformated.txt"
    os.system(nmap_fullcommand)

#Define which ports to dirb
def dirbports():
    dirbhttpcommand = "cat " + domain + "_webonly_nmap.nmap | grep open | grep -v https | cut -d '/' -f1 > " + domain + "_open_http_ports.txt"
    dirbhttpscommand = "cat " + domain + "_webonly_nmap.nmap | grep open | grep -v http | cut -d '/' -f1 > " + domain + "_open_https_ports.txt"
    os.system(dirbhttpcommand)
    os.system(dirbhttpscommand)   

#Define Dirb run
def dirbrun():
    dirbhttpports =  domain + "_open_http_ports.txt" 
    dirbhttpsports = domain + "_open_https_ports.txt"
    fh = open(dirbhttpports)
    for line in fh:
        dirbruncommand = "dirb http://" + domain + ":" + line + ">>" + domain + "_all_dirb_output.txt"
        print dirbruncommand
        #os.system(dirbruncommand)
    fh.close


#Define EyeWitness
def eyewitenessrun():
    eyewitnesscommand = "python /root/tools/EyeWitness/EyeWitness.py --web --no-prompt -x " + domain + "_webonly_nmap.xml"
    os.system(eyewitnesscommand)

#define Nikto
def niktorun():
    print " niktorun"

#define spider


#execute code below

#amassrun()
#digrun()
#formatdigips()
#nmapwebrun()
#nmaprun()
#dirbports()
#dirbrun() # not working
eyewitenessrun() # working lets work on output
