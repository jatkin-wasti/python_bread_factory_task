from factory import NaanFactory


def run_factory(ingredient1, ingredient2):
    test_factory = NaanFactory()
    if test_factory.make_dough(ingredient1, ingredient2) == 'dough':
        print(test_factory.bake_dough(True))
    else:
        print(test_factory.bake_dough(False))


run_factory('water', 'flour')
run_factory('flour', 'water')
