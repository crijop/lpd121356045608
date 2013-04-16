#*-* encoding: utf-8 *-*
'''
Created on 15 de Abr de 2013

@author: xama
'''


from appSegInformatica import bcolors
from file import is_valid_ip
import nmap
import os

class ScanningConections(object):
    
    def __init__(self, *args, **kwargs):
        

        self.error = 0 
        while True:
            os.system("clear")
            portScanningTitle = open("menus/activeConections.txt", "r")
            print bcolors.AMARELO + portScanningTitle.read() + bcolors.ENDC
            portScanningTitle.close()
            
            if self.error == 1:
                
                self.error = 0
                print bcolors.VERMELHO + "O IP que introduzio não é correcto" + bcolors.ENDC
                pass
                
          
            print "(A qualquer altura introduza '0' para voltar ao menu anterior)"
            self.address = raw_input(bcolors.AZUL + "Introduza o endereço a analisar:\t" + bcolors.ENDC)
            
            if self.address == "0":
                
                break
                pass 
            elif self.address != "" and self.analiseIP(self.address) != 0:
                
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
        print "A procurar serviços ativos..."
        nm.scan(self.address, '1-1024')
        os.system("clear")
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
                        print('port : %s\tstate : %s \tservice: %s' % (port, nm[host][proto][port]['state'], nm[host][proto][port]['name']))
            
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
    
  


    
   
