# -*- coding: utf-8 -*-
'''
Created on 19 de Mar de 2013

@author: admin1
'''

import sys
import re
import pygeoip
gi = pygeoip.GeoIP('../../../GeoIP.dat', pygeoip.MEMORY_CACHE)
print gi.country_code_by_name('www.baidu.com')
for line in sys.stdin:
    if not re.search("SRC=192", line):
        lista = line.split("SRC=")
    IP = lista[1].split(' ' )[0]
    try:
        print IP + ': ' + gi.country_code_by_addr(IP)
    except:
        continue