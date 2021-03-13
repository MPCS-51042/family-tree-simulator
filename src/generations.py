import sys, os
import networkx as nx
import matplotlib.pyplot as plt
import csv
import random
from names import Names


class FamilyTree(object):
    def __init__(self, object):
        self.tree = nx.Graph()
        self.num_generations = object.get("num_generations")
        self.year = int(object.get("start_year"))
        father_first_name = object.get("father")[0]
        father_last_name = object.get("father")[1]
        father_age = object.get("father")[2]
        mother_first_name = object.get("mother")[0]
        mother_last_name = object.get("mother")[1]
        mother_age = object.get("mother")[2]
        self.tree.add_node(0, first_name = mother_first_name, last_name = mother_last_name, age = mother_age, gender = "f", alive = "y")
        self.tree.add_node(1, first_name = father_first_name, last_name = father_last_name, age = father_age, gende = "m", alive = "y")
        self.tree.add_edge(0,1, relation = "marriage")

        self.fem_names = Names().fem_names
        self.masc_names = Names().masc_names
        self.surnames = Names().surnames
        self.person_id = 2

    def r_first_name(self, gender):
        '''
        returns a randomized first name depending on gender and year
        
        INPUTS:
	    gender (int): 0 indicates masc gender, 1 indicates femme
            year (int): number representing the year person appears in graph
        OUTPUTS:
            first_name (str): a string representation of a first name, properly formatted
        '''
        curr_era = float('inf')
        for era in self.masc_names:
            if era <= curr_era and era >= self.year:
                curr_era = era

        if gender == "m":
            name = random.choice(self.masc_names[curr_era])
        if gender == "f":
            name = random.choice(self.fem_names[curr_era])
        return name

    def r_last_name(self):
        '''
        returns a randomized last name

        OUTPUTS:
            last_name (str): a string representnation of a last name, properly formatted
        '''
        return random.choice(self.surnames)

    def individual(self, relationship, relations):
        '''
        adds a new individual to the network with given parent/spouse nodes

        INPUTS:
            relationship (str): a string representation of relationship, either 
                "marriage" or "birth"
            relations (list): a list of node identifiers of the parent or spouse
                of the node to be added

        OUTPUTS:
            nothing
        '''
        new_gender = random.choice(["f", "m"])

        if relationship == "marriage":
            # need to fix age, gender should be opposite spouse, not random
            new_age = 15 + random.choice(range(20))
            new_gender = nx.get_node_attributes("gender")[relations[0]]
            self.tree.add_node(self.person_id, first_name = self.r_first_name(new_gender), last_name = self.r_last_name, age = new_age, gender = new_gender, alive = "y" )
            self.tree.add_edge(relations[0], 0)

        if relationship == "birth":
            # need to fix last name to be the fathers last name
            # new_age = 0
            # new_gender = random.choice(["f", "m"])
            # new_last_name = 
            self.tree.add_node(self.person_id, first_name = self.r_first_name(new_gender), last_name = self.r_last_name, age = 0, gender = new_gender, alive = "y")
            for i in relations:
                 self.tree.add_edge(i, 0)

        self.person_id += 1

    def prob_dead(self):

        pass

    def prob_marry(self):

        pass

    def prob_birth(self):

        pass

        
    def year(self):

        '''
        simulates one year, modifying the self.tree attribute
        '''

        tree = self.tree
        print(tree.get_edge_data(*(0,1)))
       
        #names = nx.get_node_attributes(tree, 'name')


 
        # visit each node in tree
        # if they are dead, move on to next node
        # if they are alive increment age by 1
        # if not married:
        # 	determine probability they get married
        #       insert node for corresponding wife/husband
        # if married/they get married that year, and both are alive:
        #     determine probability they have a kid
        #     insert node for corresponding child
        #         determine probability they have a
        # determine probability that they die


        # increment year by 1

    def tree_run(self):
        '''
        runs the simulation
        '''
        self.r_first_name("f")
        self.r_last_name()

        #self.individual(1,2)
        #self.year()
        plt.subplot(122)
        nx.draw(self.tree, with_labels=True, font_weight='bold') 
        plt.savefig('test.png')


