import sys, os
import networkx as nx
import csv
import random
import copy
from numpy import random
from scipy.stats import norm, bernoulli
from data import Data


class FamilyTree(object):
    def __init__(self, object):
        # initializing the tree object from input.yaml
        self.tree = nx.Graph()
        self.num_years = object.get("num_years")
        self.year = int(object.get("start_year"))
        father_first_name = object.get("father")[0]
        father_last_name = object.get("father")[1]
        father_age = object.get("father")[2]
        father_birthday = object.get("father")[3]
        mother_first_name = object.get("mother")[0]
        mother_last_name = object.get("mother")[1]
        mother_age = object.get("mother")[2]
        mother_birthday = object.get("father")[3]
        self.tree.add_node(0, first_name = mother_first_name, last_name = mother_last_name, \
        age = mother_age, gender = "f", alive = True, birth_year = mother_birthday)
        self.tree.add_node(1, first_name = father_first_name, last_name = father_last_name, \
        age = father_age, gender = "m", alive = True, birth_year = father_birthday)
        self.tree.add_edge(0,1, relation = "marriage")
        self.person_id = 2

        # initializing name/demographic datasets
        self.fem_names = Data().fem_names
        self.masc_names = Data().masc_names
        self.surnames = Data().surnames
        self.death_rate = Data().death_rate
        self.fem_marriage_rates = Data().fem_marriage_rates
        self.masc_marriage_rates = Data().masc_marriage_rates

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
        '''
        if relationship == "marriage":
            new_age = 16 + random.choice(range(20))
            gender = nx.get_node_attributes(self.tree, "gender")[relations[0]]
            if gender == "f":
                new_gender = "m"
            if gender == "m":
                new_gender = "f"
            self.temp_tree.add_node(self.person_id, first_name = self.r_first_name(new_gender), \
            last_name = self.r_last_name(), age = new_age, gender = new_gender, alive = True, \
            birth_year = self.year - new_age)
            self.temp_tree.add_edge(relations[0], self.person_id, relation = "marriage")

        if relationship == "child":
            # the new child hsa a random gender, their father's last name, and their age is set to 0
            new_gender = random.choice(["f", "m"])
            if nx.get_node_attributes(self.tree, "gender")[relations[0]] == 'f':
                old_last_name = nx.get_node_attributes(self.tree, 'last_name')[relations[1]]
            else:
                old_last_name = nx.get_node_attributes(self.tree, 'last_name')[relations[0]]
            self.temp_tree.add_node(self.person_id, first_name = self.r_first_name(new_gender), \
            last_name = old_last_name, age = 0, gender = new_gender, alive = True, \
            birth_year = self.year)
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

        age = nx.get_node_attributes(self.tree, 'age')[individual]
        model = norm.cdf(age, loc=self.death_rate[present_rate], scale=10)
        sample = bernoulli.rvs(model, size=1)
        if sample[0] == 0:
            return False
        if sample[0] == 1:
            return True
 
    def prob_marry(self, individual):
        '''
        determines whether an individual will marry. marriage rates are also modelled 
        as a normal distribution, with a mean life expectancy for a given year, taken from
        Statista, with a standard deviation of 5. like above, there were no immediately
        available statistics that indicated the standard deviation of the measurements,
        so 5 is once again arbitrary. 
        INPUTS:
            individual (int): the node in question
        OUTPUTS:
            marriage (bool): True if person gets married, False if they do not
        '''
        present_rate = float('inf')
        for year in self.fem_marriage_rates:
            if year <= present_rate and year >= self.year:
                present_rate = year

        age = nx.get_node_attributes(self.tree, 'age')[individual]
        gender = nx.get_node_attributes(self.tree, 'gender')[individual]
        if gender == 'm':
            model = norm.cdf(age, loc=self.masc_marriage_rates[present_rate], scale = 5)
        if gender == 'f':
            model = norm.cdf(age, loc=self.fem_marriage_rates[present_rate], scale = 5)
        sample = bernoulli.rvs(model, size=1)

        if sample[0] == 0:
            return False
        if sample[0] == 1:
            return True


    def prob_birth(self):
        '''
        determines whether a couple will conceive a child. i couldn't find any accurate
        statistics for estimating this parameter, so arbitrarily decided that a given couple
        should have a 1/10 chance of conceiving in any given year. while this might seem unrealistically
        low, it makes the tree sparser and easier to parse.
        OUTPUTS:
            Birth (bool): True if a child is conceived, False if not
        '''
        sample = bernoulli.rvs(.1, size=1)
        if sample[0] == 0:
            return False
        return True

    def one_year(self):
        '''
        simulates one year, modifying the self.tree attribute. increments the age of all
        alive individuals by one, calls probability functions to determine whether 
        individuals die, have chilren, or get married, and then calls the self.individual()
        function to insert an appropriate node into the tree. the self.temp_tree object 
        is used as a dummy variable, as networkx graph datastructure uses dictionaries, 
        which cannot be modified mid-iteration.
        '''
        people = list(self.tree.nodes)
        alive = nx.get_node_attributes(self.tree, "alive")
        seen_edges = []
        self.temp_tree = self.tree.copy()

        for person in people:
            if not alive[person]:
                continue

            # increasing age of all alive individuals by 1
            self.temp_tree.nodes[person]['age'] = self.tree.nodes[person]['age'] + 1
            relations = self.tree.edges(person)
            gender = nx.get_node_attributes(self.tree, 'gender')[person]
            age = nx.get_node_attributes(self.tree, 'age')[person]

            # determines whether married couple have child
            not_married = len(relations)
            for relationship in relations:
                if (self.tree.edges[relationship]["relation"] == "marriage") and \
                    (self.prob_birth()) and gender == 'f' and age < 50:
                    self.individual("child", relationship)
                    seen_edges.append(relationship[::-1])
                if self.tree.edges[relationship]["relation"] != "marriage":
                    not_married -= 1

            # determines whether individual gets married in a given year
            if not_married == 0 and self.prob_marry(person):
                self.individual("marriage", [person])

            # determines whether individual dies that year
            if self.prob_dead(person):
                self.temp_tree.nodes[person]['alive'] = False
            #print(self.temp_tree.nodes[person])

        # updating the year value, and replacing the real tree with the dummy tree
        self.year += 1
        self.tree = self.temp_tree.copy()

    def output_file(self):
        '''
        outputs the self.tree in a .txt file format. couples are written on 
        '''

        people = self.tree
        output = open('family_tree.txt', 'w')

        # get list of all people who have married
        for person in people:
            mother = False
            relations = self.tree.edges(person)
            gender = nx.get_node_attributes(people, 'gender')[person]
            first_names = nx.get_node_attributes(people, 'first_name')
            last_names = nx.get_node_attributes(people, 'last_name')
            genders = nx.get_node_attributes(people, 'gender')
            birth_years = nx.get_node_attributes(people, 'birth_year')
            ages = nx.get_node_attributes(people, 'age')
            livings = nx.get_node_attributes(people, 'alive')

            # formats and writes married couple nodes
            for relationship in relations:
                if self.tree.edges[relationship]['relation'] == 'marriage' and gender == 'f':
                    mother = True
                    deathday = ''
                    if not livings[person]:
                        deathday = f', deathday={birth_years[person]+ages[person]}'
                    output.write(f'{first_names[person]} {last_names[person]} (id={person}, {genders[person].capitalize()}, birthday={birth_years[person]}{deathday}) \n')
                    deathday = ''
                    if not livings[relationship[1]]:
                        deathday = f', deathday={birth_years[relationship[1]]+ages[relationship[1]]}'
                    output.write(f'{first_names[relationship[1]]} {last_names[relationship[1]]} (id={relationship[1]}, {genders[relationship[1]].capitalize()}, birthday={birth_years[relationship[1]]}{deathday}) \n')

            # formats and writes nodes of children
            for relationship in relations:
                deathday = ''
                if not livings[relationship[1]]:
                    deathday = f', deathday={birth_years[relationship[1]]+ages[relationship[1]]}'
                if self.tree.edges[relationship]['relation'] == 'child' and mother == True and \
                    birth_years[relationship[0]] < birth_years[relationship[1]]:
                    output.write(f'\t{first_names[relationship[1]]} {last_names[relationship[1]]} (id={relationship[1]}, {genders[relationship[1]].capitalize()}, birthday={birth_years[relationship[1]]}{deathday}) \n')

            if mother == True:
                output.write('\n')

        output.close()

    def main(self):
        '''
        runs the simulation, calling self.one_year self.num_years times. writes
        the tree data to the output file, and then calls familytreemaker to
        create the .png image representation of the tree
        '''
        i=0
        while i <= self.num_years:
            self.one_year()
            i+=1

        root_firstname = nx.get_node_attributes(self.tree, 'first_name')[0]
        root_lastname = nx.get_node_attributes(self.tree, 'last_name')[0]

        self.output_file()
        os.system(f"./familytreemaker.py -a '{root_firstname} {root_lastname}' family_tree.txt | dot -Tpng -o family_tree.png")

