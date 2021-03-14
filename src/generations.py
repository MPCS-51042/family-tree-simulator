import sys, os
import networkx as nx
import matplotlib.pyplot as plt
import csv
import random
import copy
from numpy import random
from names import Names


class FamilyTree(object):
    def __init__(self, object):
        self.tree = nx.Graph()
        self.num_generations = object.get("num_generations")
        self.year = int(object.get("start_year"))
        father_first_name = object.get("father")[0]
        father_last_name = object.get("father")[1]
        father_age = object.get("father")[2]
        father_birthday = object.get("father")[3]
        mother_first_name = object.get("mother")[0]
        mother_last_name = object.get("mother")[1]
        mother_age = object.get("mother")[2]
        mother_birthday = object.get("father")[3]
        self.tree.add_node(0, first_name = mother_first_name, last_name = mother_last_name, age = mother_age, gender = "f", alive = True, birth_year = mother_birthday)
        self.tree.add_node(1, first_name = father_first_name, last_name = father_last_name, age = father_age, gender = "m", alive = True, birth_year = father_birthday)
        self.tree.add_edge(0,1, relation = "marriage")

        # TODO: change names folder to be something like "data", change Names class to be something like "Data"
        self.fem_names = Names().fem_names
        self.masc_names = Names().masc_names
        self.surnames = Names().surnames
        self.death_rate = Names().death_rate
        self.person_id = 2

        # self.temp_tree is a dummy tree because it's impossible to alter the original tree
        # as we iterate through it
        self.temp_tree = copy.deepcopy(self.tree)

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
        returns a randomized surname from the source file of british surnames

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

        if relationship == "marriage":
            # need to fix age, gender should be opposite spouse, not random
            new_age = 15 + random.choice(range(20))
            gender = nx.get_node_attributes(self.tree, "gender")[relations[0]]
            if gender == "f":
                new_gender = "m"
            if gender == "m":
                new_gender = "f"
            print(gender)
            print(new_gender)
            self.temp_tree.add_node(self.person_id, first_name = self.r_first_name(new_gender), last_name = self.r_last_name, age = new_age, gender = new_gender, alive = True, birth_year = self.year - new_age)
            self.temp_tree.add_edge(relations[0], self.person_id, relation = "marriage")

        if relationship == "child":
            # TODO: need to fix last name to be the fathers last name
            new_gender = random.choice(["f", "m"]) 
            self.temp_tree.add_node(self.person_id, first_name = self.r_first_name(new_gender), last_name = self.r_last_name, age = 0, gender = new_gender, alive = True, birth_year = self.year)
            for i in relations:
                 self.temp_tree.add_edge(i, self.person_id, relation = "child")

        self.person_id += 1

    def prob_dead(self, individual):
        '''
        determines whether an individual dies based on their age. death rates are modelled
        as a normal distribution with a mean of the life expectancy at a given year, with a
        standard deviation of 10. there were no immediately available statistics that indicated
        the standard deviation of the measurements, so 10 is somewhat arbitrary. a drawback
        to this method of simulation is that it currently ignores high child mortality, which
        should make the distribution multimodal.
        INPUTS:
            individual (int): the node in question
        OUTPUTS:
            death (bool): True if the person dies, False if they do not

        '''       
        present_rate = float('inf')
        for year in self.death_rate:
            if year <= present_rate and year >= self.year:
                present_rate = year

        model = random.normal(self.death_rate[present_rate], 10, 1)
        age = nx.get_node_attributes(self.tree, 'age')[individual]
        if model - age < 0:
            return True
        return False
 
    def prob_marry(self):
        '''
        determines whether an individual will marry. marriage rates are also modelled 
        as a normal distribution, with a mean of 30 and a standard deviation of 5. problems
        with this sort of model are ---- TODO: Finish
        '''
        # TODO: scrape data from UK website

        model = random.norma(30, 10, 1)
        age = nx.get_node_attributes(self.treem, 'age')[individual]

        if model - age < 0:
            return True
        return False


    def prob_birth(self):
        '''
        determines whether a couple will conceive a child. 
        '''
        

        
    def one_year(self):

        '''
        simulates one year, modifying the self.tree attribute
        '''
        people = list(self.tree.nodes)
        alive = nx.get_node_attributes(self.tree, "alive")
        seen_edges = []

        for person in people:
            if not alive[person]:
                break
            # TODO: need to increment all ages by 1
            # all relationships of person  
            relations = self.tree.edges(person)
            # delivers babies to married families that are expecting
            not_married = len(relations)
            for relationship in relations:
                if self.tree.edges[relationship]["relation"] == "marriage" and relationship not in seen_edges:
                    # TODO: make sure they can't have a child w/ dead husband/wife
                    self.individual("child", relationship)
                    seen_edges.append(relationship[::-1])
                if self.tree.edges[relationship]["relation"] != "marriage":
                    not_married -= 1
            if not_married == 0:
                self.individual("marriage", [person])
            

 

        # updating the year value, and replacing the real tree with the dummy tree
        self.year += 1
        self.tree = copy.deepcopy(self.temp_tree)
        #print(self.tree.nodes)

    def tree_run(self):
        '''
        runs the simulation
        '''
        #print(self.death_rate)
        self.r_first_name("f")
        self.r_last_name()
        self.one_year()
        self.one_year()
        self.one_year()
        self.prob_dead(1)
        #print(nx.get_node_attributes(self.tree, "first_name"))
        #self.individual(1,2)
        plt.subplot(122)
        nx.draw(self.tree, with_labels=True, font_weight='bold') 
        plt.savefig('test.png')



