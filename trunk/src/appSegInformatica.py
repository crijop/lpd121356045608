# -*- coding: utf-8 -*-
'''
Created on 19 de Mar de 2013

@author: António Baião N:5604
@author: Carlos Palma N:5608
'''

import sys
import re
import pygeoip

'''
Classe de análise de ficheiro de logs
'''
class FicheiroLog:
    def __init__(self):
        caminho = '../../../GeoIP.dat'
        self.analiseFicheiroLog(caminho)
        pass
    
    '''
    Método que faz a análise do Ficheiro de log
    Recebe como parametro o caminho do file GeoIP.dat
    '''
    def analiseFicheiroLog(self, caminho):
        gi = pygeoip.GeoIP(caminho, pygeoip.MEMORY_CACHE)
        print gi.country_code_by_name('www.baidu.com')
        for line in sys.stdin:
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


if __name__ == '__main__':
    FicheiroLog()    
    


#Makefile    
'''
fileLog:
    python appSegInformatica.py < ../../../ufw.log |more

'''