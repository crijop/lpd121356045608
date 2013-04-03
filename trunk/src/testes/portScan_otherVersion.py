'''
Created on 21 de Mar de 2013

@author: xama
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, sys

if 4 != len(sys.argv):
    print("Usage: {} <ip-adress> <start-port> <end-port>".format(sys.argv[0]))
    exit()
    
startPort = 0
endPort = 0

try:
    startPort = int(sys.argv[2])
    endPort = int(sys.argv[3])
    
except:
    print ("There is erro in Port Number")
    exit()
    
while startPort <= endPort:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((sys.argv[1],startPort))
        
        print ("Port {} is opened!".format(startPort))
        startPort = startPort + 1
        sock.close()
    except:
        print ("Port {} is closed!".format(startPort))
        startPort = startPort + 1
        