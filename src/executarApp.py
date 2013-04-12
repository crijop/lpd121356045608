# -*- coding: utf-8 -*-
'''
Created on 11 de Abr de 2013

@author: admin1
'''
from appSegInformatica import FicheiroLog, bcolors
from nmap_portScanning import PortScanning
import os


class Dialgo(object):
    def __init__(self):
        pass
    
    def dIncial(self):
        os.system("clear")
        mainMenu = open("menus/mainMenu.txt", "r")
        print bcolors.VERDE + mainMenu.read() + bcolors.ENDC
        #print bcolors.VERDE + "Pretende fazer:"
        #print "Análise ao ficheiro de log da firewall? -> 1"
        #print "PortScanning? -> 2"
        #print "....  -> 3" + bcolors.ENDC
        resposta = raw_input(bcolors.AZUL + "Faça a sua escolha: " + bcolors.ENDC)
        os.system("clear")
        return resposta
        pass
    
    def validarDialgo(self):
        resposta = self.dIncial()
        while (resposta != "1" or resposta != "2"):
            if resposta == "1":
                
                logFilesTitle = open("menus/FileLog.txt", "r")
                print bcolors.AMARELO + logFilesTitle.read() + bcolors.ENDC
                logFilesTitle.close()
                print "(A qualquer altura introduza '0' para voltar ao menu anterior)"
                caminhoFileLog = raw_input(bcolors.AZUL + "Introduza o caminho do ficheiro que deseja analisar: " + bcolors.ENDC)
                while True:
                    os.system("clear")
                    
                    logFilesTitle = open("menus/FileLog.txt", "r")
                    print bcolors.AMARELO + logFilesTitle.read() + bcolors.ENDC
                    logFilesTitle.close()
                    
                    '''Verificar se o caminho introduzido é ficheiro'''
                    if os.path.isfile(caminhoFileLog):
                        
                        FicheiroLog(caminhoFileLog)
                        break
                        pass
                    elif caminhoFileLog == "0":
                        
                        self.dIncial()
                        pass
                    else:
                        
                        print bcolors.VERMELHO + "A sua resposta não é válida, volte a introduzir o caminho!" + bcolors.ENDC
                        print "(A qualquer altura introduza '0' para voltar ao menu anterior)"
                        caminhoFileLog = raw_input(bcolors.AZUL + "Introduza o caminho do ficheiro que deseja analisar: " + bcolors.ENDC)
                        
                        pass
                    pass
                pass
            elif resposta == "2":
                            
                PortScanning()
                break
                pass
            elif resposta == "3":
                print bcolors.AMARELO + "Fazer ......" + bcolors.ENDC
                
                break
                pass
            else:
                print bcolors.VERMELHO + "A sua resposta não é válida, volte a responder!" + bcolors.ENDC
                resposta = self.dIncial()
                pass
            pass
        pass
    pass

if __name__ == '__main__':
    #FicheiroLog()
    d = Dialgo()
    d.validarDialgo()
    
    