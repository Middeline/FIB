"""
.. module:: CountWords

CountWords
*************

:Description: CountWords

    Generates a list with the counts and the words in the 'text' field of the documents in an index

:Authors: Carolina Middel i Cristina Tubert
    

:Version: 

:Created on: 04/07/2017 11:58 

"""

from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
from elasticsearch.exceptions import NotFoundError, TransportError

import argparse

__author__ = 'carolina_cristina'

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


K = 35
B = 0.488


def heaps(n):
    return K*(n**B)

def HeapValues(paraules_tot, diff): #no es fa servir
    optim, c = curve_fit(heaps, paraules_tot, diff)
    return optim

def depurar_document(paraula):
    if paraula.isalpha():
        size = len(paraula)-2
        for i in range(size):
            if paraula[i] == paraula[i+1] and paraula[i] == paraula[i+2]:
                return False
        return True
    return False
    
    
def grafic_heaps(paraules_totals, paraules_diff, v):
    fig = plt.figure(figsize=(20,10))
    plt.plot(paraules_totals, paraules_diff, color='red') #reals
    plt.plot(paraules_totals, v, color='blue') #heap
        
    plt.xlabel('x = Paraules totals')
    plt.ylabel('y = Paraules diferents')
    plt.show()
    
    
def grafic_log_heaps(paraules_totals, paraules_diff, v):
    fig = plt.figure(figsize=(20,10))
    plt.plot(np.log(paraules_totals), np.log(paraules_diff), color='red') #reals
    plt.plot(np.log(paraules_totals), np.log(v), color='blue') #heap
    
    plt.xlabel('x = Log de paraules totals')
    plt.ylabel('y = Log de paraules diferents')
    plt.show()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--alpha', action='store_true', default=False, help='Sort words alphabetically')
    args = parser.parse_args()

    index = ["n0", "n1", "n2", "n3", "n4", "n5", "n6"] #agafem els 7 indexs

    try:

        paraules_diff = []
        paraules_totals = []
        
        for i in index:   
        
            client = Elasticsearch()
            voc = {}
            sc = scan(client, index=i, query={"query" : {"match_all": {}}})
            for s in sc:
                try:
                    tv = client.termvectors(index=i, id=s['_id'], fields=['text'])
                    if 'text' in tv['term_vectors']:
                        for t in tv['term_vectors']['text']['terms']:
                            if t in voc:
                                voc[t] += tv['term_vectors']['text']['terms'][t]['term_freq']
                            else:
                                voc[t] = tv['term_vectors']['text']['terms'][t]['term_freq']
                except TransportError:
                    pass
            lpal = []

            for v in voc:
                lpal.append((v.encode("utf-8", "ignore"), voc[v]))

            cont = 0
            cont_total = 0

            for pal, cnt in sorted(lpal, key=lambda x: x[0 if args.alpha else 1]):
                if depurar_document(pal):     
                    cont_total += cnt
                    cont += 1

            paraules_totals.append(cont_total)
            paraules_diff.append(cont)

            print('--------------------')
            print(str(cont) + ' Words')  #ho canviem per veure el numero de paraules un cop depurat
        

        #K_b = HeapValues(paraules_totals, paraules_diff)
        #K = K_b[0]
        #B = K_b[1]
        
        v = []
        for r in paraules_totals:
            v.append(heaps(r))
            
        grafic_heaps(paraules_totals, paraules_diff, v)
        grafic_log_heaps(paraules_totals, paraules_diff, v)
        

    except NotFoundError:
        print(f'Index {index} does not exists')
