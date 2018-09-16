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
amassoutput = domain + "_amass.txt"
amassvm = "amass -freq 480 -d " + domain + " -o " + amassoutput

#Define amass
def amassrun():
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
    nmap_fullcommand = "nmap -v -p 80,8080,443 -oG " + domain + "_webonly_nmap -iL " + domain + "_digformated.txt"
    os.system(nmap_fullcommand)
       
#Define NMAP
def nmapfullrun():
    nmap_fullcommand = "nmap -v -p 1-65535 -oG " + domain + "_allport_nmap -iL " + domain + "_digformated.txt"
    os.system(nmap_fullcommand)

#Define Dirb
def dirbrun():
    #dirbcommand = dirb ""
    print "dirbrun"

#Define EyeWitness
def eyewitenessrun():
    print "eyewitenessrun"

#define Nikto
def niktorun():
    print " niktorun"

#define spider


#execute code
amassrun()
digrun()
formatdigips()
nmapwebrun()
#nmaprun()
