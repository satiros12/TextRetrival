import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import re 


POLITICA = []
CIENCIA = []
DEPORTE = []

with open("./Ciencia.txt","r") as RF:
    CIENCIA.append([])
    for l in RF:
        if l == "###\n": #Es un nuevo documento, abrimos una nueva lista
            CIENCIA.append([]) 
            continue
        if l != "\n":
            CIENCIA[-1].append(l[:-1])
#CIENCIA_WORDS = [w.lower() for w in np.concatenate([np.concatenate([l.split(" ") for l in] CIENCIA[0]]))]
print "Cargados ",len(CIENCIA)," documentos de ciencia" 

with open("./Deportes.txt","r") as RF:
    DEPORTE.append([])
    for l in RF:
        if l == "###\n": #Es un nuevo documento, abrimos una nueva lista
            DEPORTE.append([]) 
            continue
        if l != "\n":
            DEPORTE[-1].append(l[:-1])
print "Cargados ",len(DEPORTE)," documentos de deporte"    
    
with open("./Politica.txt","r") as RF:
    POLITICA.append([])
    for l in RF:
        if l == "###\n": #Es un nuevo documento, abrimos una nueva lista
            POLITICA.append([]) 
            continue
        if l != "\n":
            POLITICA[-1].append(l[:-1])
print "Cargados ",len(POLITICA)," documentos de politica" 



def preprocess(Docs):
    WOR = [np.concatenate([[w.lower() for w in l.split(" ")] for l in d]) for d in Docs]
    for w in xrange(len(WOR)):
        W = WOR[w]
        W = filter(lambda w : len(w) != 0, W)
        W = map(lambda w : re.sub(r'[\.\,-]',"",w) , W)
        W = filter(lambda w : len(w) != 0, W)
        W = map(lambda w : re.sub(r'[\"\'><\\\/\)\(]',"",w) , W)
        W = filter(lambda w : len(w) != 0, W)
        W = map(lambda w : re.sub(r'\d',"",w) , W)
        W = filter(lambda w : len(w) != 0, W)
        WOR[w] = W
    return WOR


POLITICA_W = preprocess(POLITICA)
CIENCIA_W = preprocess(DEPORTE)
DEPORTE_W = preprocess(CIENCIA)
TOT_D = POLITICA_W + CIENCIA_W + DEPORTE_W
TOT_W = list(set(np.concatenate(TOT_D)))


ITF_W = [np.log(len(TOT_D)*1.0/len(filter(lambda d :w in d , TOT_D)))  for w in TOT_W]
TOT_WU=np.array(TOT_W)[np.where(np.array(ITF_W)> 2.0)[0]] #Usando 3.0 Hay documentos sin palabras.

#Vector Space Model
POLW = []
count = 0
for d in TOT_D:
    print count
    count+=1
    #POLW.append([])
    POLW.append([(len(np.where(np.asanyarray(d) == w)[0]) *1.0/ len(d)) *  np.log(len(TOT_D)*1.0/len(filter(lambda d :w in d,TOT_D)))  for w in TOT_WU])
    #for w in TOT_W:
    #    ft = len(np.where(np.asanyarray(d) == w)[0]) *1.0/ len(d)
    #    itf = len(filter(lambda d :w in d,TOT_D))
    #    #for d in TOT_D:
    #    #    if w in d:
    #    #        itf+=1
    #    itf = np.log(len(TOT_D)*1.0/itf)
    #    POLW[-1].append(ft*itf)

#Numero de palabras que no son 0 en cada documento tf-itf
print [len(filter(lambda w : w != 0.0, l)) for l in POLW]