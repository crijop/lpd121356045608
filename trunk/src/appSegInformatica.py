# -*- coding: utf-8 -*-
'''
Created on 19 de Mar de 2013

@author: António Baião N:5604
@author: Carlos Palma N:5608
'''

import os
import pygeoip
import re
import sys

#classe de Colorização
class bcolors:
    #BOLD = '\033[1m'
    #FUNDO PRETO = '\033[40m'
    ROXO = '\033[95m' + '\033[1m' + '\033[40m'
    AZUL = '\033[94m' + '\033[1m' + '\033[40m'
    VERDE = '\033[92m' + '\033[1m' + '\033[40m'
    AMARELO = '\033[93m' + '\033[1m' + '\033[40m'
    VERMELHO = '\033[91m' + '\033[1m' + '\033[40m'
    ENDC = '\033[0m'
    
    def disable(self):
        self.ROXO = ''
        self.AZUL = ''
        self.VERDE = ''
        self.AMARELO = ''
        self.VERMELHO = ''
        self.ENDC = ''
        pass
    pass


'''
Classe de análise de ficheiro de logs
'''
class FicheiroLog:
    def __init__(self, caminhoFileLog):
        caminho = '../../../GeoIP.dat'
        self.analiseFicheiroLog(caminho, caminhoFileLog)
        pass
    
    '''
    Método que faz a análise do Ficheiro de log
    Recebe como parametro o caminho do file GeoIP.dat
    '''
    def analiseFicheiroLog(self, caminho, caminhoFileLog):
        
        ficheiro = open(caminhoFileLog, "r")
        
        gi = pygeoip.GeoIP(caminho, pygeoip.MEMORY_CACHE)
        print gi.country_code_by_name('www.baidu.com')
        for line in ficheiro:
            if not re.search("SRC=192", line):
                lista = line.split("SRC=")
                listaData = line.split(' ')
            IP = lista[1].split(' ' )[0]
            mes = listaData[0]
            dia = listaData[1]
            hora = listaData[2]
            #print IP
            try:
                print IP + ': ' +  mes + ': '+ dia + ': ' + hora + ' --> ' + gi.country_code_by_addr(IP)
            except:
                continue
        pass

    pass
    
#Makefile    
'''
fileLog:
    python appSegInformatica.py < ../../../ufw.log |more

'''