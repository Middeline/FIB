"""
.. module:: SearchIndexWeight

SearchIndex
*************

:Description: SearchIndexWeight

    Performs a AND query for a list of words (--query) in the documents of an index (--index)
    You can use word^number to change the importance of a word in the match

    --nhits changes the number of documents to retrieve

:Authors: bejar


:Version:

:Created on: 04/07/2017 10:56

"""

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError

import argparse
import operator

import numpy as np

from elasticsearch_dsl import Search
from elasticsearch.client import CatClient
from elasticsearch_dsl.query import Q

__author__ = 'bejar'


alpha = 1
beta = 1
R = 4
nrounds = 5



def query_a_diccionari (query):
    dicc = {}
    for x in query:
        if '^' in x:
            terme, impor = x.split('^')
            dicc[terme] = float(impor)
        else:
            dicc[x] = 1.0
    return normalize(dicc)


def diccionari_a_query (dicc):
    query = []
    for t in dicc:
        val = str(dicc[t])
        lol = t + '^' + val
        query.append(lol)
    return query


def rocchio(sum_doc, query_dicc, nh):

    for t in sum_doc:
        sum_doc[t] = sum_doc.get(t,0)*beta/nh

    for t in query_dicc:
        query_dicc[t] = query_dicc.get(t,0) * alpha

    dicc = {}
    for t in set(sum_doc) | set(query_dicc):
        dicc[t] = sum_doc.get(t,0) + query_dicc.get(t, 0)

    return sorted(dicc.items(),key=operator.itemgetter(1), reverse= True)


def document_term_vector(client, index, id):
    """
    Returns the term vector of a document and its statistics a two sorted list of pairs (word, count)
    The first one is the frequency of the term in the document, the second one is the number of documents
    that contain the term

    :param client:
    :param index:
    :param id:
    :return:
    """
    termvector = client.termvectors(index=index, id=id, fields=['text'],
                                    positions=False, term_statistics=True)

    file_td = {}
    file_df = {}

    if 'text' in termvector['term_vectors']:
        for t in termvector['term_vectors']['text']['terms']:
            file_td[t] = termvector['term_vectors']['text']['terms'][t]['term_freq']
            file_df[t] = termvector['term_vectors']['text']['terms'][t]['doc_freq']
    return sorted(file_td.items()), sorted(file_df.items())



def toTFIDF(client, index, file_id):
    """
    Returns the term weights of a document

    :param file:
    :return:
    """

    # Get the frequency of the term in the document, and the number of documents
    # that contain the term
    file_tv, file_df = document_term_vector(client, index, file_id)

    max_freq = max([f for _, f in file_tv])

    dcount = doc_count(client, index)

    tfidfw = {}
    for (t, w),(_, df) in zip(file_tv, file_df):
        #
        # Something happens here
        tfdi= w/max_freq
        idfi= np.log2((dcount)/df)

        tfidfw[t] = tfdi * idfi
        #
    return normalize(tfidfw)


def print_term_weigth_vector(twv):
    """
    Prints the term vector and the correspondig weights
    :param twv:
    :return:
    """
    #
    # Program something here
    #
    for t1, t2 in twv:
        print("terme: " + t1 + ", weight: " + str(t2))


def normalize(dicc):
    """
    Normalizes the weights in t so that they form a unit-length vector
    It is assumed that not all weights are 0
    :param tw:
    :return:
    """
    #
    # Program something here
    #
    suma = 0
    for i in dicc:
        suma += dicc[i]

    arrel = np.sqrt(suma)

    result = {}
    for i in dicc:
        result[i] = dicc[i]/arrel

    return result


def cosine_similarity(tw1, tw2):
    """
    Computes the cosine similarity between two weight vectors, terms are alphabetically ordered
    :param tw1:
    :param tw2:
    :return:
    """
    #
    # Program something here
    aux_1 = 0
    aux_2 = 0

    suma = 0

    while aux_1 < len(tw1) and aux_2 < len(tw2):
        (par1, w1) = tw1[aux_1]
        (par2, w2) = tw2[aux_2]
        if par1 > par2:
            aux_2 += 1
        elif par1 < par2:
            aux_1 += 1
        else :
            suma += w1 * w2
            aux_1 += 1
            aux_2 += 1

    #
    return suma

def doc_count(client, index):
    """
    Returns the number of documents in an index

    :param client:
    :param index:
    :return:
    """
    return int(CatClient(client).count(index=[index], format='json')[0]['count'])





if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--index', default=None, help='Index to search')
    parser.add_argument('--nhits', default=10, type=int, help='Number of hits to return')
    parser.add_argument('--query', default=None, nargs=argparse.REMAINDER, help='List of words to search')

    args = parser.parse_args()

    index = args.index
    query = args.query
    nhits = args.nhits

    try:
        client = Elasticsearch()
        s = Search(using=client, index=index)

        if query is not None:

            for i in range(nrounds):
                q = Q('query_string',query=query[0])
                for i in range(1, len(query)):
                    q &= Q('query_string',query=query[i])

                s = s.query(q)
                response = s[0:nhits].execute()

                print(query)

                q_a_d = query_a_diccionari(query)
                suma_de_doc = {}

                for r in response:  # only returns a specific number of results
                    d = toTFIDF(client, index, r.meta.id)

                    for t in set(suma_de_doc) | set(d):
                        suma_de_doc[t] = suma_de_doc.get(t,0) + d.get(t, 0)

                    print(f'ID= {r.meta.id} SCORE={r.meta.score}')
                    print(f'PATH= {r.path}')
                    print(f'TEXT: {r.text[:50]}')
                    print('-----------------------------------------------------------------')

                q2 = rocchio(suma_de_doc, q_a_d, nhits)
                #q2 = diccionari_a_query(dicc2)

                q2 = q2[:R]

                dicc = {}
                for t, value in q2:
                    dicc[t] = value

                query = diccionari_a_query(dicc)

                print("\n\n\n\n\n")



        else:
            print('No query parameters passed')

        print (f"{response.hits.total['value']} Documents")

    except NotFoundError:
        print(f'Index {index} does not exists')
