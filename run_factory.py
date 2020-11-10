from factory import NaanFactory  # Importing NaanFactory so we can create some Naan in this file


# Function that takes two ingredients and outputs whether you can make naan out of them or not
def run_factory(ingredient1, ingredient2):
    test_factory = NaanFactory()
    if test_factory.make_dough(ingredient1, ingredient2) == 'dough':
        print(test_factory.bake_dough(True))
    else:
        print(test_factory.bake_dough(False))


# Testing that the function works with the ingredients in any order
run_factory('water', 'flour')
run_factory('flour', 'water')
# Testing that the function works with incorrect dough ingredients
run_factory('bananas', 'maple syrup')
