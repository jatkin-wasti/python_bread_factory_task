class NaanFactory:
    def make_dough(self, ingredient1, ingredient2):
        if (ingredient1.lower() == 'water' and ingredient2.lower() == 'flour') or (ingredient1.lower() == 'flour' and
                                                                                   ingredient2.lower() == 'water'):
            return 'dough'
        else:
            return 'this attempt to make dough has failed'

    def bake_dough(self, dough_success):
        if dough_success:
            return 'naan'
        else:
            return 'this attempt to make naan has failed'

