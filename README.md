# Task
# TDD Bread Factory!

## Timings

60-90 Minutes

## Summary

TDD bread factory is the latest bread brand in Py Land. It always produces the best bread because it has the best testing strategy!

What they do is before they make any new bread, they make a test to make sure the end output is correct. Then they adjust the recipe until it's just right!

You are going to do the same with bread! This is called Test Driven Development.

## Tasks

This exercise is going to bring together lots of concepts.

### Learning Outcomes
Learning outcomes include:
- git
- github
- functions
- TDD
- Separation of concerns - this is important do not ignore!
- DRY code
- DOD


## Installing and running
To run the naan factory do the following:

```
import naan factory
run factory()
```


### TDD - test driven development

1. write the test
2. run it, and read the error
3. code and make it pass the test

this helps with:
- Stop over engineering
- Maintainable code
- Reduce technical debt
- Goes well with agile and working code
- errors can be your guide in complex systems

How it works is that we write unit tests.

##### Unit Tests

Test single pieces of code. Like a function.

**base of a test**
Usually has 3 phases.
- setup phase (know variables)
- calling of the function / piece of code with know variables
- asserting for expect output




### User stories for Naan Factory

```
#1
As a user, I can use the make dough with 'water' and 'flour' to make 'dough'.

#2
As a user, I can use the bake dough with dough to get naan.

#3
As a user, I can user the run factory with water and flour and get naan.

```

## Acceptance Criteria

* you have written tests
* test pass
* you have written more test to make sure everything works as indented
* all user stories are satisfied
* code does not break
* code has exit condition
* DOD if followed

# Solution
## Creating our test file
- First we need to make file for testing, which we'll call ```test_factory.py```
- In that file we'll import the necessary testing modules as well as the class to be tested (This hasn't been created
 yet so if you're getting an error, this is okay)
```
import unittest
import pytest
from factory import NaanFactory
```
- Creating our testing class which will inherit from the unittest TestCase framework
- We'll also create an instance of our imported class to test its (currently nonexistent) functionality
```
# Creating our testing class that inherits from the unittest Testcase framework
class TestFactory(unittest.TestCase):
    factory_test = NaanFactory()  # Creating an instance of the NaanFactory class to test its methods
```
- This method will test the make_dough function (again, this hasn't been made yet) from the imported class
- It then checks that the function produces the correct outputs depending on the arguments passed
```
    def test_make_dough(self):
        # Check if dough is output when water and flour are passed
        self.assertEqual(self.factory_test.make_dough('water', 'flour'), 'dough')
        self.assertEqual(self.factory_test.make_dough('flour', 'water'), 'dough')
        # Check if dough is output when anything other than water and flour are passed
        self.assertEqual(self.factory_test.make_dough('honey', 'meat'), 'this attempt to make dough has failed')
```
- This method will test the bake_dough function (again, this hasn't been made yet) from the imported class
- It then checks that the function produces the correct outputs depending on the arguments passed
```
    def test_bake_dough(self):
        # Check if naan is created when bake_dough is called with successful dough (True)
        self.assertEqual(self.factory_test.bake_dough(True), 'naan')
        # Check if naan is created when bake_dough is called with unsuccessful dough (False)
        self.assertEqual(self.factory_test.bake_dough(False), 'this attempt to make naan has failed')
```
- When we run these tests (by running the file or using a terminal command such as ```pytest -v```) we should see
 that both tests fail
- This makes sense as the methods we are testing don't even exist! Let's change that...
## Creating our file with functionality
- If we haven't already created the file we should do so now, calling it ```factory.py```
- In this file we'll create our NaanFactory class
```
# Creating our NaanFactory that will allow us to make delicious Naan
class NaanFactory:
```
- Creating the method to make dough from two ingredients
- If the ingredients are ```water``` and ```flour``` then it creates ```dough```, otherwise the process fails 
```
 # Creating a method to make dough out of two passed ingredients
    def make_dough(self, ingredient1, ingredient2):
        if (ingredient1.lower() == 'water' and ingredient2.lower() == 'flour') or (ingredient1.lower() == 'flour' and
                                                                                   ingredient2.lower() == 'water'):
            return 'dough'  # If the ingredients are some combination of flour and water then dough is made
        else:
            return 'this attempt to make dough has failed'  # Otherwise the dough fails
```
- Creating the method to bake the dough
- This method takes a boolean value that determines whether the dough to be used was
 correctly made, outputting ```naan``` if it was good dough, and an error message if it was bad dough
```
# Creating a method to bake our dough
    def bake_dough(self, dough_success):
        if dough_success:  # If successful dough was created then we can bake some Naan
            return 'naan'
        else:  # If not then the Naan cannot be made
            return 'this attempt to make naan has failed'
```
## Creating our run file
- Now we'll create a file that can run methods inherited from the NaanFactory class
```
from factory import NaanFactory  # Importing NaanFactory so we can create some Naan in this file
```
- Creating a function that takes two ingredients and runs the ```make_dough``` and ```bake_dough``` methods, outputting 
whether the process was successful or not
```
# Function that takes two ingredients and outputs whether you can make naan out of them or not
def run_factory(ingredient1, ingredient2):
    test_factory = NaanFactory()
    if test_factory.make_dough(ingredient1, ingredient2) == 'dough':
        print(test_factory.bake_dough(True))
    else:
        print(test_factory.bake_dough(False))
```
- We'll create a block of code asking for user ingredients that will continue until they tell us to stop
```
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
```
- We can also test the function with hardcoded function calls
- The first two function calls check that dough is made regardless of the order of ingredients
- The third checks what is output when ingredience other than water and flour are used
```
# Testing that the function works with the ingredients in any order
run_factory('water', 'flour')
run_factory('flour', 'water')
# Testing that the function works with incorrect dough ingredients
run_factory('bananas', 'maple syrup')

```