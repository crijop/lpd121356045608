#!/usr/bin/env python
from socket import * 

if __name__ == '__main__':
    target = raw_input('Enter host to scan: ')
    targetIP = gethostbyname(target)
    print 'Starting scan on host ', target

    #scan reserved ports
    for i in range(20, 1025):
        s = socket(AF_INET, SOCK_STREAM)
        print "tetse"
        result = s.connect_ex((target, i))

        if(result == 0) :
            print 'Port %d: OPEN' % (i,)
        s.close()
