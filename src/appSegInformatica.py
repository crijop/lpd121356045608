# -*- coding: utf-8 -*-
'''
Created on 19 de Mar de 2013

@author: António Baião N:5604
@author: Carlos Palma N:5608
'''

from Crypto.Util.number import size
from ImageShow import show
from Save_PDF_CSV import PDF
from bdb import bar
from matplotlib import figure
from textwrap import fill
import array
import csv
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
import os
import pygeoip
import re
import sys



#classe de Colorização
class bcolors:
    '''
    bcolors permite colorir o output gerado no terminal
    por forma a ser mais facil de interpertar
    '''
    
    #BOLD = '\033[1m'
    #FUNDO PRETO = '\033[40m'
    ROXO = '\033[95m' + '\033[1m' + '\033[40m'
    AZUL = '\033[94m' + '\033[1m' + '\033[40m'
    VERDE = '\033[92m' + '\033[1m' + '\033[40m'
    AMARELO = '\033[93m' + '\033[1m' + '\033[40m'
    VERMELHO = '\033[91m' + '\033[1m' + '\033[40m'
    ENDC = '\033[0m'
    
    def disable(self):
        '''
        desativa qualquer cor que tiver ativa 
        no terminal
        '''
        self.ROXO = ''
        self.AZUL = ''
        self.VERDE = ''
        self.AMARELO = ''
        self.VERMELHO = ''
        self.ENDC = ''
        pass
    pass



class FicheiroLog:
    '''
    Classe de análise de ficheiro de logs
    '''
    def __init__(self, caminhoFileLog):
        '''
        Inicializa a lista onde guardrá os objectos analizado
        e chama o metodo que fará a analise
        
        Parametro: caminho para o ficheiro
        '''
        caminho = 'GeoIP.dat'
        self.lista = []
        self.analiseFicheiroLog(caminho, caminhoFileLog)
        pass
    
    '''
    Método que faz a análise do Ficheiro de log
    Recebe como parametro o caminho do file GeoIP.dat
    '''
    def analiseFicheiroLog(self, caminho, caminhoFileLog):
        '''
        Método que faz a análise do Ficheiro de log
        Recebe como parametro o caminho do file GeoIP.dat
        '''
        
        ficheiro = open(caminhoFileLog, "r")
        
        gi = pygeoip.GeoIP(caminho, pygeoip.MEMORY_CACHE)
        
        #print gi.country_code_by_name('www.baidu.com')
        
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
                code = gi.country_code_by_addr(IP)
                self.lista.append((IP, mes, dia, hora, code))
                
            except:
                continue
                pass
            
        print('--------------TERMINEI-------------------------')
        raw_input("Prima enter para continuar...")
        self.extraMenu()
        pass
    
    def extraMenu(self):
        '''
        Menu com opções extra, tais como imprimir a informação em PDF,
        CSV entre outros.
        
        Este menu será apresentado no fim de cada acção
        '''
        while True:
            os.system("clear")
            extraMenu = open("menus/extraOptionsLog.txt", "r")
            print bcolors.VERDE + extraMenu.read() + bcolors.ENDC
            resposta = raw_input(bcolors.AZUL + "Faça a sua escolha: " + bcolors.ENDC)
            
            if resposta == "1":
                if len(self.lista) > 1:
                    pdf = PDF()
                    pdf.setTitle("FileLog")
                    pdf.alias_nb_pages()
                    pdf.add_page()
                    pdf.set_font('Times','',12)
                    for i in self.lista:
                        pdf.cell(0,5, str(i[0] + " - "+ i[1] + " - " + i[2] + " - " + i[3] + " - " + i[4]) ,0,1)
                    pdf.output('fileLog.pdf','F')
                    
                    print bcolors.AMARELO + "PDF gerado com sucesso" + bcolors.ENDC
                    raw_input("Prima enter para continuar...")
                    break
                else:
                    print bcolors.VERMELHO + "Não é possivel gerar qualquer resultado" + bcolors.ENDC
                    raw_input("Prima enter para continuar...")
                    break        
                pass
            
            elif resposta == "2":
                if len(self.lista) > 1:
                    with open('fileLog.csv', 'wb') as csvfile:
                        spamwriter = csv.writer(csvfile, delimiter=',')
                        for i in self.lista:
                            #print len(i)
                            spamwriter.writerow(i)
                    print bcolors.AMARELO + "CSV gerado com sucesso" + bcolors.ENDC
                    raw_input("Prima enter para continuar...")
                    break 
                else:
                    print bcolors.VERMELHO + "Não é possivel gerar qualquer resultado" + bcolors.ENDC
                    raw_input("Prima enter para continuar...")
                    break   
                       
                pass
            elif resposta == "3":
                
                self.infoForGraph()
                
                #Construção do grafico
                
                #figure(figsize=(4, 2)) # image dimensions   
                title("Try Connections - FileLog", size='large')
                
                ylabel("How many access")
                xlabel("Countries")
                # add bars
                for i, key in zip(range(len(self.codeFreq)), self.codeFreq.keys()):
                    bar(i + 0.25 , self.codeFreq[key], color='red')
                
                # axis setup
                xticks(arange(0.65, len(self.codeFreq)), 
                    [('%s: %d' % (name, value)) for name, value in 
                    zip(self.codeFreq.keys(), self.codeFreq.values())], 
                    size='large')
                max_value = max(self.codeFreq.values())
                tick_range = arange(0, max_value, (max_value / 7))
                yticks(tick_range, size='large')
                formatter = FixedFormatter([str(x) for x in tick_range])
                gca().yaxis.set_major_formatter(formatter)
                gca().yaxis.grid(which='major')
                
                show()
                
                pass
             
            elif resposta == "0":
                break
                pass
            
        pass

    

    def infoForGraph(self):
        '''
        Constroi dicionario com informação 
        para geração do gráfico estatistico
        '''
        
        self.codeFreq = {}
     
        for line in self.lista:
            
            if  line[4] in self.codeFreq:
                self.codeFreq[line[4]] += 1
                pass
            else:
                self.codeFreq[line[4]] = 1
                pass
            
        
       
    pass
            

    
#Makefile    
'''
fileLog:
    python appSegInformatica.py < ../../../ufw.log |more

'''