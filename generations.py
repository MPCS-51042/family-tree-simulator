import sys, os
from treelib import Node, Tree

class FamilyTree(object):
    def __init__(self, object):
        self.num_generations = object.get("num_generations")
        self.start_year = object.get("start_year")
        self.tree = Tree()

    def individual(self):
        self.tree.create_node("new_child0", "new_child0")
        i = 1
        while i <= self.num_generations:
            self.tree.create_node("new_child" + str(i), "new_child" + str(i), parent = "new_child" + str(i-1))
            i+=1

    def tree_run(self):

        self.individual()
        self.tree.show()
    




