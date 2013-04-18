# -*- coding: utf-8 -*-
'''
Created on 11 de Abr de 2013

@author: admin1
'''
from appSegInformatica import FicheiroLog, bcolors
from nmap_portScanning import PortScanning
from nmap_scanningConections import ScanningConections
import os
import sys


class Dialgo(object):
    '''
    Classe responsável por gerár o primeiro menu de 
    dialogos que será a porta de interacção com o utilizador
    '''
    def __init__(self):
        '''
        Construtor da classe que nao vai desenhpenhar nenhuma função
        '''
        pass
    
    def dIncial(self):
        '''
        Responsavel por mostrar a caixa de menus ao utilizador e 
        devolver a resposta que o utilizador introduzio
        '''
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
        """
        Consoante a resposta do utilizador assim será a acção
        que  será desencadeada.
        
        O utilizador terá ao dispor 4 opções.
        """
        resposta = self.dIncial()
        while True:
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
                        
                        self.validarDialgo()
                        pass
                    else:
                        
                        print bcolors.VERMELHO + "A sua resposta não é válida, volte a introduzir o caminho!" + bcolors.ENDC
                        print "(A qualquer altura introduza '0' para voltar ao menu anterior)"
                        caminhoFileLog = raw_input(bcolors.AZUL + "Introduza o caminho do ficheiro que deseja analisar: " + bcolors.ENDC)
                        
                        pass
                    pass
                resposta = self.dIncial()
                pass
            elif resposta == "2":
                            
                PortScanning()
               
                resposta = self.dIncial()
                
                pass
            elif resposta == "3":
                ScanningConections()
                
                resposta = self.dIncial()
                
                pass
            elif resposta == "0":
                print "Aplicação desenvolvida por:\n\tAntónio Baião\n\tCarlos Palma"
                sys.exit(0);
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
    
    