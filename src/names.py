import csv
import os

class Names():

    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.fem_names, self.masc_names, self.surnames = self.names()

    def names(self):
        fem_names = {}
        masc_names = {}
        surnames = []

        with open(self.path + '/names/surnames.csv') as scsvfile:
            surnames_file = csv.reader(scsvfile, delimiter = ',')

            for row in surnames_file:
                surnames.append(row[0])
        
        with open(self.path + '/names/masc_names.csv') as mcsvfile:
            mnames = csv.reader(mcsvfile, delimiter = ',')

            # cleaning column names
            columns = []
            for i in next(mnames):
                new_word = ''
                for char in i:
                    if char.isnumeric():
                        new_word += char
                columns.append(int(new_word))

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

           
        with open(self.path + '/names/fem_names.csv') as fcsvfile:

            fnames = csv.reader(fcsvfile, delimiter = ',')

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

        counter = 0
        while counter < len(masc_names):
            masc_names[columns[counter]] = masc_names[counter]
            fem_names[columns[counter]] = fem_names[counter]
            del masc_names[counter]
            del fem_names[counter]
            counter += 1

        return fem_names, masc_names, surnames




        

