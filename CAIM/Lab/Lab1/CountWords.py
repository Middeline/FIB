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


a = 0.85
b = 0
c = 206546

def zipfs(x):
    return c/(x+b)**a

def depurar_document(paraula):
    if paraula.isalpha():
        size = len(paraula)-2
        for i in range(size):
            if paraula[i] == paraula[i+1] and paraula[i] == paraula[i+2]:
                return False
        return True
    return False
    
def grafic_freq(freq):
    fig = plt.figure(figsize=(20,10))
    plt.bar(list(range(300)), freq[0 : 300]) #tractem les 300 paraules més freqüents
    
    plt.xlabel('x = Rang de les paraules més freqüents (ordenades decreixentment)')
    plt.ylabel('y = Freqüència de les paraules')
    plt.show()
    
def grafic_zipfs(freq):
    v = []
    for r in range(300):    #tractem les 300 paraules més freqüents
        v.append(zipfs(r+1))
        
    fig = plt.figure(figsize=(20,10))
    plt.plot(list(range(300)), freq[0 : 300], color='red') #reals
    plt.plot(list(range(300)), v, color='blue') #zipfs

    plt.xlabel('x = Rang de les paraules més freqüents (ordenades decreixentment)')
    plt.ylabel('y = Freqüència de les paraules')
    plt.show()
        
        
def grafic_log_zipfs(freq):
    v = []
    for r in range(300):    #tractem les 300 paraules més freqüents
        v.append(np.log(zipfs(r+1)))

    fig = plt.figure(figsize=(20,10))
    plt.plot(np.log(list(range(300))), np.log(freq[0 : 300]), color='red') #reals
    plt.plot(np.log(list(range(300))), v, color='blue') #zipfs
        
    plt.xlabel('x = Log del rang de les paraules més freqüents (ordenades decreixentment)')
    plt.ylabel('y = Log de la freqüència de les paraules')
    plt.show()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', default=None, required=True, help='Index to search')
    parser.add_argument('--alpha', action='store_true', default=False, help='Sort words alphabetically')
    args = parser.parse_args()

    index = args.index

    try:
        client = Elasticsearch()
        voc = {}
        sc = scan(client, index=index, query={"query" : {"match_all": {}}})
        for s in sc:
            try:
                tv = client.termvectors(index=index, id=s['_id'], fields=['text'])
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

        freq = []
        cont = 0

        for pal, cnt in sorted(lpal, key=lambda x: x[0 if args.alpha else 1]):
            if depurar_document(pal):
                freq.append(cnt)
                cont += 1
                
                print(f'{cnt}, {pal.decode("utf-8")}')
        print('--------------------')
        print(str(cont) + ' Words')  #ho canviem per veure el número de paraules un cop depurat
     
        freq.reverse()
        
        #grafic_freq(freq)
        grafic_zipfs(freq)
        grafic_log_zipfs(freq)
    

    except NotFoundError:
        print(f'Index {index} does not exists')
