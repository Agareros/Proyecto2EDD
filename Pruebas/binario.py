# -*- coding: utf-8 -*-
import fileinput

class binario:

    def __init__(self):
        bufferzise=50000
        infile=open('imagen.jpg','rb')
        print infile
        outfile=open('new.jgp','wb')
        buffer = infile.read(bufferzise)
        print"--------------------------------"
        while len(buffer):
            outfile.write(buffer)
            #print "listo"
            print buffer
            buffer=infile.read(bufferzise)
        #print ""
        #print "listo"
        print "------------------------------"
bin=binario()