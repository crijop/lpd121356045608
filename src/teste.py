'''
Created on 15 de Abr de 2013

@author: admin1
'''
import os
import pickle

if __name__ == '__main__':
    ano = 2002
    nrDocentes = [299, 90, 0, 5, 5]
    
    print nrDocentes
    ficheiro = open("mens.dat", "w")
    pickle.dump(ano, ficheiro)
    pickle.dump(nrDocentes, ficheiro)
    ficheiro.close()
    os.system("python Graficos.py")
    pass
