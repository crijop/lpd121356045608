#!/usr/bin/env python
#*-* encoding: utf-8 *-*
from appSegInformatica import bcolors
from file import is_valid_ip
import nmap
import os

class PortScanning(object):
    
    def __init__(self):
        
      
        self.error = 0 
        while True:
            os.system("clear")
            portScanningTitle = open("menus/portScanning.txt", "r")
            print bcolors.AMARELO + portScanningTitle.read() + bcolors.ENDC
            portScanningTitle.close()
            
            if self.error == 1:
                
                self.error = 0
                print bcolors.VERMELHO + "O IP que introduzio não é correcto" + bcolors.ENDC
                pass
                
          
            print "(A qualquer altura introduza '0' para voltar ao menu anterior)"
            self.address = raw_input(bcolors.AZUL + "Introduza o endereço da rede a analisar:\t" + bcolors.ENDC)
            self.mask = raw_input(bcolors.AZUL + "Introduza a mascara do endereço em decimal:\t" + bcolors.ENDC)
            if self.address == "0":
                
                break
                pass 
            elif self.address != "" and self.analiseIP(self.address) != 0 and self.analiseMask(self.mask) != 0:
                
                self.makeScan()
                break
           
                pass
           
            else:
                
                self.error = 1
                pass
            
            pass
        pass
    def makeScan(self):   
        
        nm = nmap.PortScanner() 
        self.address.strip()
        nm.scan(self.address + '/' + self.mask, '1-1024')

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
        raw_input("Prima enter para continuar...")
        self.extraMenu()
        pass
    
    def extraMenu(self):
        
        extraMenu = open("menus/extraOptions.txt", "r")
        print bcolors.VERDE + extraMenu.read() + bcolors.ENDC
        
        pass
    
    def analiseIP(self, ip):
        
        return is_valid_ip(ip)

        
        pass
    
    def analiseMask(self, mask):
        
        value = 0
        
        if mask >= 0 and mask <= 32:
            
            value = 1
        else:
            value = 0
            pass
            
        
        return value
    pass
        
    
    