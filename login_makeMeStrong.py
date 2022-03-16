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

def __split(G):
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

def __search_sink_pair(G, x, M, end):
    if M[x] == 0:
        if x in end:
            M[x] = 1
            return x
        M[x] = 1
        for y in G.adjlists[x]:
            w = __search_sink_pair(G, y, M, end)
            if w >= 0:
                return w
    return -1

def raghavan(G):
    """Makes G strongly connected (add edges in G to make it strongly connected)
        Return the number of added edges
    """
    Gr, sc = scc.condensation(G)
    end, start, isolated = __split(Gr)
    if not end and not start and len(isolated) <= 1:
        return 0
    M = [0] * Gr.order
    minedge = 0
    edges = []
    unmatched_sink = set(end)
    unmatched_source = set()
    for v in start:
        if M[v]:
            continue
        w = __search_sink_pair(Gr, v, M, unmatched_sink)
        if w >= 0:
            minedge += 1
            edges.append((w, v))
            unmatched_sink.remove(w)
        else:
            unmatched_source.add(v)
    if unmatched_sink:
        for w in unmatched_sink:
            minedge += 1
            edges.append((w, edges[0][1]))
    if unmatched_source:
        for v in unmatched_source:
            minedge += 1
            edges.append((edges[0][0], v))
    if isolated:
        if edges:
            edges.append((edges[0][0], isolated[0]))
            edges.append((isolated[-1], edges[0][1]))
            minedge += 2
        elif len(isolated) > 1:
            edges.append((isolated[-1], isolated[0]))
            minedge += 1
        for i in range(len(isolated)-1):
            edges.append((isolated[i], isolated[i+1]))
            minedge += 1
    for edge in edges:
        G.adjlists[sc.index(edge[0])].append(sc.index(edge[1]))
    return minedge



#def __determine_reach(G, v, reach, unvisited):
#    path = [v]
#    while v in unvisited:
#        unvisited.remove(v)
#        if not G.adjlists[v]:
#            break;
#        v = G.adjlists[v][0]
#        path.append(v)
#    for i in path:
#        reach[i] = v
#
#def contest(G):
#    n = G.order
#    # Determine in-degree of all the nodes
#    indegree = [0 for i in range(n)]
#    for i in range(n):
#        for adj in G.adjlists[i]:
#            indegree[adj] += 1
#
#    # Nodes with indegree = 0 will need to be an end-point of a new edge
#    endpoints = [i for i in range(n) if (indegree[i] == 0)]
#    nr_indegree_zero = len(endpoints)
#
#    # Determine which (hereto unvisited) nodes will be reached by these endpoints
#    unvisited = set(range(n))
#    reach = [None for i in range(n)]
#
#    for v in endpoints:
#        __determine_reach(G, v, reach, unvisited)
#
#    # The reached nodes form good start-points for the new edges
#    startpoints = [reach[v] for v in endpoints]
#
#    # Check for isolated cycles that are not connected to the rest of the graph
#    nr_cycles = 0
#    while len(unvisited) > 0:
#        # Select a node from the unvisited set (without removing it)
#        v = unvisited.pop()
#        unvisited.add(v)
#
#        nr_cycles += 1
#        __determine_reach(G, v, reach, unvisited)
#        endpoints.append(v)
#        startpoints.append(reach[v])
#
#    # Special case: no indegree 0 nodes and only 1 cycle
#    if (nr_indegree_zero == 0) and (nr_cycles == 1):
#        # No edges need to be added
#        return 0
#
#    # Rotate the lists to each start point connects to the end-point of the next item
#    endpoints = endpoints[1:] + endpoints[:1]
#    nb = len(endpoints)
#    for i in range(nb):
#        G.adjlists[startpoints[i]].append(endpoints[i])
#    return nb
#





