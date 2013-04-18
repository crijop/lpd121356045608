#!/usr/bin/env python
#*-* encoding: utf-8 *-*
from appSegInformatica import bcolors
from file import is_valid_ip
from Save_PDF_CSV import PDF
import nmap
import os
import csv

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
        print "A procurar portos abertos..."
        nm.scan(self.address + '/' + self.mask, '1-1024')
        os.system("clear")
        
        self.valuesToSavePDF = []
        self.valuesToSaveCSV = []
        
        self.valuesToSavePDF.append("Network address: "+ self.address)
        self.valuesToSavePDF.append("Network mask: " + self.mask)
        self.valuesToSavePDF.append("Number of ports to search: " + '1-1024')
        
        self.valuesToSaveCSV.append(("Network adress: ", self.address))
        self.valuesToSaveCSV.append(("Network mask: " , self.mask))
        self.valuesToSaveCSV.append(("Number of ports to search: " ,'1-1024'))
        # a more usefull example :
        for host in nm.all_hosts():
            self.valuesToSaveCSV.append((" "))
            self.valuesToSavePDF.append('----------------------------------------------------')
            print('----------------------------------------------------')
            
            self.valuesToSaveCSV.append(('Host : ', host, '(' +nm[host].hostname() + ')'))
            self.valuesToSavePDF.append('Host : %s (%s)' % (host, nm[host].hostname()))
            print('Host : %s (%s)' % (host, nm[host].hostname()))
            
            self.valuesToSaveCSV.append(('State : ', nm[host].state()))
            self.valuesToSavePDF.append('State : %s' % nm[host].state())
            print('State : %s' % nm[host].state())
            
            for proto in nm[host].all_protocols():
                if proto != "addresses":
                    self.valuesToSaveCSV.append((" "))
                    self.valuesToSavePDF.append('----------')
                    print('----------')
                    
                    self.valuesToSaveCSV.append(('Protocol : ', proto))
                    self.valuesToSavePDF.append('Protocol : %s' % proto)
                    print('Protocol : %s' % proto)
                    
                    lport = nm[host][proto].keys()
                    lport.sort()
                    for port in lport:
                        
                        self.valuesToSaveCSV.append(('port : ', port, 'state : ',nm[host][proto][port]['state'], 'reason : ', nm[host][proto][port]['reason'] ))                        
                        self.valuesToSavePDF.append('port : %s\tstate : %s \treason: %s' % (port, nm[host][proto][port]['state'], nm[host][proto][port]['reason']))
                        print('port : %s\tstate : %s \treason: %s' % (port, nm[host][proto][port]['state'], nm[host][proto][port]['reason']))
            
        print('--------------TERMINEI-------------------------')
        raw_input("Prima enter para continuar...")
        self.extraMenu()
        pass
    
    def extraMenu(self):
        
        while True:
            os.system("clear")
            extraMenu = open("menus/extraOptions.txt", "r")
            print bcolors.VERDE + extraMenu.read() + bcolors.ENDC
            resposta = raw_input(bcolors.AZUL + "Faça a sua escolha: " + bcolors.ENDC)
            
            if resposta == "1":
                if len(self.valuesToSavePDF) > 3:
                    pdf = PDF()
                    pdf.setTitle("PortScanning")
                    pdf.alias_nb_pages()
                    pdf.add_page()
                    pdf.set_font('Times','',12)
                    for i in self.valuesToSavePDF:
                        pdf.cell(0,5, i ,0,1)
                    pdf.output('portScanning.pdf','F')
                    
                    print bcolors.AMARELO + "PDF gerado com sucesso" + bcolors.ENDC
                    raw_input("Prima enter para continuar...")
                    break
                else:
                    print bcolors.VERMELHO + "Não é possivel gerar qualquer resultado" + bcolors.ENDC
                    raw_input("Prima enter para continuar...")
                    break        
                pass
            
            elif resposta == "2":
                if len(self.valuesToSaveCSV) > 3:
                    with open('portScanning.csv', 'wb') as csvfile:
                        spamwriter = csv.writer(csvfile, delimiter=',')
                        for i in self.valuesToSaveCSV:
                            print len(i)
                            spamwriter.writerow(i)
                    print bcolors.AMARELO + "CSV gerado com sucesso" + bcolors.ENDC
                    raw_input("Prima enter para continuar...")
                    break 
                else:
                    print bcolors.VERMELHO + "Não é possivel gerar qualquer resultado" + bcolors.ENDC
                    raw_input("Prima enter para continuar...")
                    break   
                       
                pass
             
            elif resposta == "0":
                break
                pass
            
        pass
    
    def analiseIP(self, ip):
        
        return is_valid_ip(ip)

        
        pass
    
    def analiseMask(self, mask):
        
        value = 0
        
        if int(mask) >= 0 and int(mask) <= 32:
            
            value = 1
        else:
            value = 0
            pass
            
        
        return value
    pass
        
    
    
