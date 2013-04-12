#!/usr/bin/env python
#*-* encoding: utf-8 *-*
import nmap
from appSegInformatica import bcolors

class PortScanning(object):
    
    def __init__(self):
        
        while True:
            portScanningTitle = open("menus/portScanning.txt", "r")
            print bcolors.AMARELO + portScanningTitle.read() + bcolors.ENDC
                
            self.address = raw_input("Introduza o endereço a analisar:")
            
            if self.address != "":
                self.analiseIP(self.address)
                self.makeScan()
                break
                pass
            else:
                
                pass
            
            pass
        pass
    def makeScan(self):   
        
        nm = nmap.PortScanner() 
        self.address.strip()
        print nm.scan(self.address + '/24', '1-1024')

        # a more usefull example :
        for host in nm.all_hosts():
            print('----------------------------------------------------')
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            print('State : %s' % nm[host].state())
            
            for proto in nm[host].all_protocols():
                if proto != "addresses":
                    print('----------')
                    print('Protocol : %s' % proto)
            
                    lport = nm[host][proto].keys()
                    lport.sort()
                    for port in lport:
                        print('port : %s\tstate : %s \treason: %s' % (port, nm[host][proto][port]['state'], nm[host][proto][port]['reason']))
            
        print('--------------TERMINEI-------------------------')
        pass
    
    def analiseIP(self, ip):
        ip.strip()
        
        
        
        
        pass
    
    
