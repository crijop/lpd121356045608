#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import sys
import threading, Queue

MAX_THREADS = 50

class Scanner(threading.Thread):
    def __init__(self, inq, outq):
        threading.Thread.__init__(self)
        self.setDaemon(1)
        # queues for (host, port)
        self.inq = inq
        self.outq = outq

    def run(self):
        while 1:
            host, port = self.inq.get()
            
            sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            #print "\nporto: ", port      
        
                # connect to the given host:port
            try:
                sd.connect((host, port))
                print "Vou conectar me"
           
            
            except socket.error:
                # set the CLOSED flag
                self.outq.put((host, port, 'CLOSED'))
            else:
                self.outq.put((host, port, 'OPEN'))
                sd.close()
            
def scan(host, start, stop, nthreads=MAX_THREADS):
    toscan = Queue.Queue()
    scanned = Queue.Queue()

    scanners = [Scanner(toscan, scanned) for i in range(nthreads)]
    for scanner in scanners:
		#print "iniciar Scanner"
		scanner.start()

    hostports = [(host, port) for port in xrange(start, stop+1)]
    for hostport in hostports:
        toscan.put(hostport)

    results = {}
    for host, port in hostports:
        while (host, port) not in results:
            nhost, nport, nstatus = scanned.get()
            results[(nhost, nport)] = nstatus
        status = results[(host, port)]
        if status <> 'CLOSED':
            print '%s:%d %s' % (host, port, status)

if __name__ == '__main__':
    scan('192.168.1.91', 0, 1024)
