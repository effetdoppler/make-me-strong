# -*- coding: utf-8 -*-
"""
S4 - March 2022
Strong Connectivity Homework
@author: charles.zhang
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
        return 0
    Gr, sc = scc.condensation(G)
    end, start, indeg, outdeg = __makeMeStrong(Gr)
    minedge = 0
    if len(start) > 1:
        for i in range(len(start)-1):
            outdeg[start[i]] = 1
            indeg[start[i + 1]] = 1
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
    return minedge


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

def __makeMeStrong2(G):
    indeg = [0] * G.order
    outdeg = [0] * G.order
    M = [0] * G.order
    # settup outdeg and indeg
    for i in range(G.order):
        if M[i] == 0:
            __settup(G, i, indeg, outdeg, M)
    start = []
    end = []
    isolated = []
    #find start and end vertices
    for i in range(G.order):
        if indeg[i] == 0:
            if outdeg[i] != 0:
                start.append(i)
            else:
                isolated.append(i)
        else:
            if outdeg[i] == 0:
                end.append(i)
    return end, start, isolated

def __search_raghavan(G, x, M, end):
    if M[x] == 0:
        M[x] = 1
        if x in end:
            return x
        for y in G.adjlists[x]:
            w = __search_raghavan(G, y, M, end)
            if w >= 0:
                return w
    return -1

def raghavan(G):
    """Makes G strongly connected (add edges in G to make it strongly connected)
        Return the number of added edges
    """
    Gr, sc = scc.condensation(G)
    end, start, isolated = __makeMeStrong2(Gr)
    if not end and not start and len(isolated) <= 1:
        return 0
    M = [0] * Gr.order
    p = 0
    vv = []
    ww = []
    remaining_sink = set(end)
    remaining_source = set()
    for v in start:
        if M[v]:
            continue
        w = __search_raghavan(Gr, v, M, remaining_sink)
        if w >= 0:
            p += 1
            ww.append(w)
            vv.append(v)
            remaining_sink.remove(w)
        else:
            remaining_source.add(v)
    edges = []
    if not ww:
        for i in range(len(isolated)-1):
            edges.append((isolated[i], isolated[i+1]))
        if len(isolated) > 1:
            edges.append((isolated[-1], isolated[0]))
    else:
        for i in range(p-1):
            edges.append((ww[i], vv[i+1]))
        while remaining_sink and remaining_source:
            v = remaining_source.pop()
            w = remaining_sink.pop()
            edges.append((w, v))
        w = ww[-1]
        v = vv[0]
        while remaining_sink:
            wold = w
            w = remaining_sink.pop()
            edges.append((wold, w))
        while remaining_source:
            wold = w
            w = remaining_source.pop()
            edges.append((wold, w))
        for q in isolated:
            edges.append((w, q))
            w = q
        edges.append((w, v))

    for edge in edges:
        G.addedge(sc.index(edge[0]), sc.index(edge[1]))
    return len(edges)
