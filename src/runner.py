import utils
from generations import FamilyTree


params = utils.get_inputs()
family = FamilyTree(params)

family.main()

