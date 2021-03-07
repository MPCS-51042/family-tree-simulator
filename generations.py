import sys, os
import networkx as nx
import matplotlib.pyplot as plt
import csv
from names import Names

class FamilyTree(object):
    def __init__(self, object):
        self.num_generations = object.get("num_generations")
        self.start_year = object.get("start_year")
        self.tree = nx.Graph()
        self.fem_names = Names().fem_names
        self.masc_names = Names().masc_names

    def individual(self):
        self.tree.add_node(0, name='new_node0')
        i = 1
        while i <= self.num_generations:
            self.tree.add_node(i, name = 'new_node' + str(i))
            self.tree.add_edge(0, i)
            i+=1

    def tree_run(self):
        print(self.masc_names)
        self.individual()
        plt.subplot(122)
        nx.draw(self.tree, with_labels=True, font_weight='bold') 
        plt.savefig('test.png')



