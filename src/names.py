import csv
import os

class Names():

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.fem_names, self.masc_names, self.surnames = self.names()
        self.death_rate = self.deaths()

    def names(self):
        '''
        creates the surname, fem_names, and masc_names data structures for
        the generations.py file. see README for sources

        INPUTS:
            None
        OUTPUTS:
            fem_names (dict): a dictionary of lists of fem names keyed by year
            masc_names (dict): a dictionary of lists of masc names keyed by year
            surnames (list): a list of surnames
        '''
        fem_names = {}
        masc_names = {}
        surnames = []

        with open(self.path + '/names/surnames.csv', encoding='utf-8-sig') as scsvfile:
            surnames_file = csv.reader(scsvfile, delimiter = ',')
            for row in surnames_file:
                surnames.append(row[0])
        
        with open(self.path + '/names/masc_names.csv', encoding='utf-8-sig') as mcsvfile:
            mnames = csv.reader(mcsvfile, delimiter = ',')
            # cleaning column names for both masc_names and fem_names
            columns = []
            for i in next(mnames):
                new_word = ''
                for char in i:
                    if char.isnumeric():
                        new_word += char
                columns.append(int(new_word))

            # adding masc_names to data structure
            for row in mnames:
                counter = 0
                if masc_names == {}:
                    for element in row:
                        masc_names[counter] = []
                        counter += 1
                else:
                    for element in row:
                        masc_names[counter].append(element)
                        counter += 1

           
        with open(self.path + '/names/fem_names.csv', encoding='utf-8-sig') as fcsvfile:
            fnames = csv.reader(fcsvfile, delimiter = ',')
            # adding fem_names to data structure
            for row in fnames:
                counter = 0
                if fem_names == {}:
                    for element in row:
                        fem_names[counter] = []
                        counter += 1
                else:
                    for element in row:
                        fem_names[counter].append(element)
                        counter += 1

        # just a little more cleaning of the dataset to make the format nice and readable
        counter = 0
        while counter < len(masc_names):
            masc_names[columns[counter]] = masc_names[counter]
            fem_names[columns[counter]] = fem_names[counter]
            del masc_names[counter]
            del fem_names[counter]
            counter += 1

        return fem_names, masc_names, surnames

    def deaths(self):
        '''
        cretaes the death_rate datastructure for the generations.py program

        INPUTS:
            none
        OUTPUTS:
            death_rates (dict): dictionary of year:life expectancy values
        '''
        death_rates = {}
        with open(self.path + "/names/death_rates.csv", encoding='utf-8-sig') as csvfile:
            years = csv.reader(csvfile, delimiter = ',')
            for row in years:
                death_rates[int(row[0])] = float(row[1])


        return death_rates


        

