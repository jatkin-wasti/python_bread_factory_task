from factory import NaanFactory  # Importing NaanFactory so we can create some Naan in this file


# Function that takes two ingredients and outputs whether you can make naan out of them or not
def run_factory(ingredient1, ingredient2):
    test_factory = NaanFactory()
    if test_factory.make_dough(ingredient1, ingredient2) == 'dough':
        print(test_factory.bake_dough(True))
    else:
        print(test_factory.bake_dough(False))


# We only want this welcome message to run once so we'll print it before the while loop
print("Welcome to our amazing Naan Factory! If you give us two ingredients, we'll try to make some "
      "tasty Naan with them (good Naan dough only requires water and flour)")
while True:  # This will run until explicitly broken
    # Getting the users ingredients to use in our make_dough method
    ing1 = input("Please enter your first ingredient:  ")
    ing2 = input("Please enter your second ingredient:  ")
    # Running our function with the users ingredients
    run_factory(ing1, ing2)
    # Checking if the user wishes to continue or break out of the loop
    response = input("Would you like to make more bread(Y/N)?  ")
    if response == 'Y':
        continue
    elif response == 'N':
        break
    # If the input isn't 'Y' or 'N' we'll default to Y but tell the user we didn't recognise the input
    else:
        print("Answer was not recognised")

# # Testing that the function works with the ingredients in any order
# run_factory('water', 'flour')
# run_factory('flour', 'water')
# # Testing that the function works with incorrect dough ingredients
# run_factory('bananas', 'maple syrup')
