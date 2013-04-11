# -*- coding: utf-8 -*-
'''
Created on 11 de Abr de 2013

@author: admin1
'''
from appSegInformatica import FicheiroLog, bcolors
import os


class Dialgo(object):
    def __init__(self):
        pass
    
    def dIncial(self):
        print bcolors.VERDE + "Pretende fazer a análise ao ficheiro de log da firewall? -> 1"
        print "....  -> 2"
        print "....  -> 3" + bcolors.ENDC
        resposta = raw_input(bcolors.AZUL + "Faça a sua escolha: " + bcolors.ENDC)
        return resposta
        pass
    
    def validarDialgo(self):
        resposta = self.dIncial()
        while (resposta != "1" or resposta != "2"):
        
            if resposta == "1":
                print bcolors.AMARELO + "Analise do ficheiro de Logs" + bcolors.ENDC
                caminhoFileLog = raw_input(bcolors.AZUL + "Introduza o caminho do ficheiro que deseja analisar: " + bcolors.ENDC)
                '''Verificar se o caminho introduzido é ficheiro'''
                
                if os.path.isfile(caminhoFileLog):
                    FicheiroLog(caminhoFileLog)
                    break
                    pass
                else:
                    print bcolors.VERMELHO + "A sua resposta não é válida, volte a introduzir o caminho!" + bcolors.ENDC
                    caminhoFileLog = raw_input(bcolors.AZUL + "Introduza o caminho do ficheiro que deseja analisar: " + bcolors.ENDC)
                    
                    pass
                pass
            elif resposta == "2":
                print bcolors.AMARELO + "Fazer portScan" + bcolors.ENDC
                
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
    
    