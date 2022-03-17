# -*- coding: utf-8 -*-
"""
S4 - Coloration function tests for students
@author: Nathalie
"""

from algopy import graph
from strong_connectivity import *
import os
import time

def __graphlist(dirpath):
    """builds a list of graphs from a given directory
    Args: 
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        Graph list
    """
    
    files = os.listdir(dirpath)
    files.sort()
    L = []
    for f in files:
        if ".gra" in f:
            L.append(graph.load(dirpath + "/" + f))
    return L
    
# for suscribers of "list comprehensions"

def __graphlist2(dirpath):
    files = os.listdir(dirpath)
    files.sort()
    return [graph.load(dirpath + "/" + f) for f in files if ".gra" in f]
    

#without verification!
def run_coloration(f, dirpath):
    """test coloration function on a list of graphs (without verification)
    Args: 
        f (function): the coloration function (returns (nbcol, color list)) 
            color vector: contains integers in [1, nbcol]
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        the result: list of color numbers
    """
    return [f(G)[0] for G in __graphlist(dirpath)]

# with color verification

def __testcolors(G, colors):
    for s in range(G.order):
        if not colors[s]:
            return False
        for adj in G.adjlists[s]:
            if colors[s] == colors[adj]:
                return False
    return True

def __nb_edge_digraph(G):
    if not G.directed:
        return -1
    n = 0
    for x in range(G.order):
        n += len(G.adjlists[x])
    return n

def run_verif_strong(f, dirpath):
    """test the coloration function f on a list of graphs:
        - verify each coloration is correct
        - build the list of resulted chromatic numbers
    Args: 
        f (function): the coloration function (returns (nbcol, color vector)) 
            color vector: contains integers in [1, nbcol]
        dirpath (str): path to the graph directory (".gra" format)
    Returns:
        the result list: list of color numbers for each graph
    """
    start = time.time()
    tests = __graphlist(dirpath)
    results = []
    for G in tests:
        N = 1
        if N > 1:
            nb = G.order
            for i in range(1,N):
                base = i * nb
                for n in range(nb):
                    li = G.adjlists[n].copy()
                    for k in range(len(li)):
                        li[k] += base
                    G.adjlists.append(li)
            G.order = N * G.order

        edges_before = __nb_edge_digraph(G)
        nb = f(G)
        edges_after = __nb_edge_digraph(G)
        if nb != edges_after - edges_before:
            results.append((None, "inconsistent edges"))
        elif not is_strong(G, 0):
            results.append((None, "not strongly connected"))
        else:
            results.append(nb)
    print("...............time spent: " + str(round(time.time()-start, 3)) + " s")
    return results


