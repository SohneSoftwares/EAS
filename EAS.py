#!/usr/bin/python
import sys

def en(mn):
    cc = ''
    mn = mn.lower()
    for letras in mn:
        if letras in afl:
            x = afl.find(letras) + key
            if x >= full:
                x -= full
        cc += afl[x]
    return cc

def de(mn):
    cc = ''
    mn = mn.lower()
    for letras in mn:
        if letras in afl:
            y = afl.find(letras) - key
            cc += afl[y]
    return cc
        

if(len(sys.argv) < 4):
    print "Try: EAS <key> <mn> --encrypt>"
    print "Exemplo: EAS 3 abc --encrypt"
    print "https://sohne.com.br/gnu_linux/#eas"
else:
    afl = 'zyxwvutsrpqonmlkjihgfedcba+=0987654321 _-'
    full = len(afl)
    key = int(sys.argv[1])
    msg = str(sys.argv[2])

    if "--encrypt" in sys.argv[3]:        
        print "Mensagem encripitada: " + en(en(msg))
    elif "--decrypt" in sys.argv[3]:
        print "Mensagem decripitada: " + de(de(msg))

    if "--en" in sys.argv[3]:        
        print "Mensagem encripitada: " + en(en(msg))
    elif "--de" in sys.argv[3]:
        print "Mensagem decripitada: " + de(de(msg))
