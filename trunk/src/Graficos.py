# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pickle

#Grafico numero total de docentes por tipo de 
#estabelecimento. 
#vai ler a um ficheiro o ano e o nr docentes
ficheiro = open("mens.dat", "r")
nrAcesso = pickle.load(ficheiro)
codPais = pickle.load(ficheiro)
ficheiro.close()

plt.xlabel("Código do País")
plt.ylabel("Número de Acessos")
plt.title("Número Total de Acessos por Pais")
grafico = plt.plot(nrAcesso, codPais, 'ro')
plt.savefig('NumeroTotalAcePais.png')
