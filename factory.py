# Creating our NaanFactory that will allow us to make delicious Naan
class NaanFactory:
    # Creating a method to make dough out of two passed ingredients
    def make_dough(self, ingredient1, ingredient2):
        if (ingredient1.lower() == 'water' and ingredient2.lower() == 'flour') or (ingredient1.lower() == 'flour' and
                                                                                   ingredient2.lower() == 'water'):
            return 'dough'  # If the ingredients are some combination of flour and water then dough is made
        else:
            return 'this attempt to make dough has failed'  # Otherwise the dough fails

    # Creating a method to bake our dough
    def bake_dough(self, dough_success):
        if dough_success:  # If successful dough was created then we can bake some Naan
            return 'naan'
        else:  # If not then the Naan cannot be made
            return 'this attempt to make naan has failed'

