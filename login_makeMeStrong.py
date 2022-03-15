# -*- coding: utf-8 -*-
"""
S4 - March 2022
Strong Connectivity Homework
@author: insert your login
"""

from algopy import graph
import strong_connectivity as scc
# you can use any function from strong_çonnectivity.py, for instance scc.condensation

# you can import anything from algopy or built-in... (do not forget to add the import part!)


#------------------------------------------------------------------------------

# example of function:

def makeMeStrong_(G):
    """Makes G strongly connected (add edges in G to make it strongly connected)
        Return the number of added edges
    """
    if scc.is_strong(G, 0):
        return G, 0
    Gr, sc = scc.condensation(G)
    end, start, indeg, outdeg = __makeMeStrong(Gr)
    minedge = 0
    if len(start) > 1:
        for i in range(len(start)-1):
            outdeg[end[i]] = 1
            indeg[end[i + 1]] = 1
            G.addedge(sc.index(start[i]), sc.index(start[i+1]))
            minedge += 1
    if len(end) > 1:
        for i in range(len(end)-1):
            outdeg[end[i]] = 1
            indeg[end[i+1]] = 1
            G.addedge(sc.index(end[i]), sc.index(end[i+1]))
            minedge += 1
    trueend = end[len(end)-1]
    trustart = start[0]
    G.addedge(sc.index(trueend), sc.index(trustart))
    minedge += 1
    return G, minedge



def __makeMeStrong(G):
    indeg = [0] * G.order
    outdeg = [0] * G.order
    M = [0] * G.order
    #settup outdeg and indeg
    for i in range(G.order):
        if M[i] == 0:
            __settup(G, i, indeg, outdeg, M)
    start = []
    end = []
    totalin = 0
    totalout = 0
    #find start and end vertices
    for i in range(G.order):
        if indeg[i] == 0:
            start.append(i)
        else:
            totalin += 1
        if outdeg[i] == 0:
            end.append(i)
        else:
            totalout += 1
    return end, start, indeg, outdeg




def __settup(G, x, indeg, outdeg, M):
    M[x] = 1
    for adj in G.adjlists[x]:
        #mark out degree as 1
        outdeg[x] = 1
        #mark in degree as 1
        indeg[adj] = 1
        if M[adj] == 0:
            __settup(G, adj, indeg, outdeg, M)








