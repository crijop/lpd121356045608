#*-* encoding: utf-8 *-*
'''
Created on 15 de Abr de 2013

@author: xama
'''


from appSegInformatica import bcolors
from file import is_valid_ip
from Save_PDF_CSV import PDF
import csv
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
        
        self.valuesToSavePDF = []
        self.valuesToSaveCSV = []
        
        self.valuesToSavePDF.append("Network address: "+ self.address)
        self.valuesToSavePDF.append("Number of ports to search: " + '1-1024')
        
        self.valuesToSaveCSV.append(("Network adress: ", self.address))
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
                        
                        self.valuesToSaveCSV.append(('port : ', port, 'state : ',nm[host][proto][port]['state'], 'service : ', nm[host][proto][port]['name'] ))                        
                        self.valuesToSavePDF.append('port : %s\tstate : %s \tservice: %s' % (port, nm[host][proto][port]['state'], nm[host][proto][port]['name']))
                        print('port : %s\tstate : %s \tservice: %s' % (port, nm[host][proto][port]['state'], nm[host][proto][port]['name']))
            
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
                    pdf.setTitle("Active Services")
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
    
  


    
   
