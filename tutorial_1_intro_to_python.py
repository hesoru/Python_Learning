#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: github.com/hesoru/

from cgi import print_environ
#re: wildcards
import re
#random: generate random numbers
import random as rd
from functools import reduce
import itertools
#numpy: build/read arrays
import numpy as np
#matplotlib: visualizing data
import matplotlib as plt
#json/pickle: encode and decode serialized data (python uses pickle)
import json
import pickle

################################ table of contents ################################

#setting up VSCode
#important commands
    #code introspection
#creating/printing variables

#numbers/operators
#strings
#lists/tuples
    #modify lists
    #tuples
#sets/intersections
#classes
#dictionaries

#writing blocks (several commands combined)
#intro to writing functions
    #defining functions
#string formatting
    #1. % (specifier)
    #2. str.format()
    #3. f-strings
#if/else
#for/while loops
#generators
    #return vs. yield

#applying commands to lists (list comprehension)
    #1. for loops
    #2. map()
    #3. *
    #how to run command on specific index value in list?

#modules/packages
#exception handling
#serialization

###################################################################################


#-------------------------------------------------------------------------------------------------------------------------------


################################ setting up VSCode ################################

#getting conda in path
    #change python interpreter to miniconda3\python.exe in lower bar
    #change python interpreter/python path to miniconda3\python.exe in user settings json

#where conda
    #put C:\Users\Helena\miniconda3\Scripts in path env on Windows

#conda create -n pyenv python

#activate pyenv
#conda install pandas
#conda install matplotlib
#conda install numpy

#to use python packages installed in pyenv:
    #change python interpreter/python path to miniconda3\envs\pyenv\python.exe in lower bar/user settings json

################################ important commands ################################

#shift+enter = run selected code
#ctrl+shift+P = pull up vscode command search bar

### code introspection ###

#ie. viewing properties of classes, objects, functions, etc.

#provides help on a function or module
help("matplotlib")
help("matplotlib.pyplot")
help(hasattr)
#[spacebar] for "More"
#[q] to exit

class person:
    name = "John"
    age = 28
#returns properties (attributes) of object
dir(person)
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
#'__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name']

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = ""
    def description(self):
        description = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return description

#does object have attribute?
#getattr(obj, name)
hasattr(Vehicle, "kind")
#[True]

#retur object's memory address (different each time you run it)
id(Vehicle)
#[1617321660848]

#return type of object
type(Vehicle)
#<class 'type'>

#return canonical string representation of object
repr(Vehicle) 
#"<class '__main__.Vehicle'>"

#return whether object is callable (eg. function, method, class)
callable(Vehicle)
#True

#return whether object is derived from another class or is the same class
issubclass(person, Vehicle) 
#False

car1 = Vehicle()
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00

#return whether an object is an instance of a class or of a subclass thereof
#isinstance(obj, class/type)
isinstance(car1, Vehicle) 
#True

def fib_seq(a, b):
    #function documentation
    """prints fibonacci sequence"""
    while a < 10:
        print(a, end=" ")
        a, b = b, a+b
#access object documentation
fib_seq.__doc__
#'prints fibonacci sequence'

#access name of object or script
fib_seq.__name__
#'fib_seq'
__name__
#'__main__'

################################ creating/viewing variables ################################

#create variable (object) called msg
msg = "Hello World! How's it going."
#single quote works too, but apostrophes terminate string
msg2 = 'Hello World! How is it going.'
#can create multiple variables at once
a, b = 0, 1

#print contents of msg
print("The message is", msg)
#The message is Hello World!


#-------------------------------------------------------------------------------------------------------------------------------


################################ numbers/operators ################################

#can denote decimals in python
floatingpointnumber = 1.87
print(floatingpointnumber)

# operators:
    # +, -, *, / = as expected
    # ** = exponent symbol
        # keyword arguments (kwargs): arguments with keys, like in dictionary
    # % = returns remainder of division (also specifier, see below)
    # and/or = as expected
    # in = if x in object (eg. list)

11 % 6
#[5]

#"and" example:
a = "World"
if a in msg and msg2:
    print("double match!")
#[double match!]

#"in" example:
if a in msg:
    print(msg)
#[Hello World! How's it going.]

################################ strings ################################

### string manipulation ###

#mix words together
word = "Python"
word2 = "Charming"
word_final = word[0:2] + word2[0:5]
print(word_final)
#[PyCharm]

#write sentences out of strings
sentence = "Hello " + word2 + " World"
sentence
#[Hello Charming World]

#can't mix strings and numbers in a sentence
mix = word + a
mix
#[TypeError: can only concatenate str (not "int") to str]

#multiply strings
lotsofhellos = "hello" * 5
lotsofhellos
#[hellohellohellohellohello]

################################ lists/tuples ################################

squares = [1,2,3,9,16]
squares
#[1, 2, 3, 9, 16]

### modify lists ###
 
#add list value (numbering starts at 0!))
squares[2] = 4
squares
#[1, 2, 4, 9, 16]

#remove list values
squares[3:4] = []
squares
#[1, 2, 4]

#multiplying lists (repeating lists)
square_repeats = squares * 3
square_repeats
#[1, 2, 3, 9, 16, 1, 2, 3, 9, 16, 1, 2, 3, 9, 16]

list1 = [1,2,3]
list2 = [4,5,6]

#combining lists together
y = list1 + list2
y
#[1, 2, 3, 4, 5, 6]

#nesting lists within lists while keeping them separate
x = [list1, list2]
x
#[[1, 2, 3], [4, 5, 6]]
#refer to value in list
x[1][0]
#[4]

### tuples ###

#tuples are like lists contained in round brackets
tuple_a = (1, 2, "three")
tuple_a
#(1, 2, 'three')

#tuples vs. lists
    #tuples/lists both ordered + allow duplicates
    #tuples not changeable like lists

################################ sets/intersections ################################

#sets are lists without duplicates
set("my name is Helena and Helena is my name".split())
#{'my', 'name', 'is', 'and', 'Helena'}

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

#see where sets intersect
print(a.intersection(b))
print(b.intersection(a))
#{'John'}

#see differences between sets
#found in set a only
print(a.difference(b))
#{'Jake', 'Eric'}
#found in set b only
print(b.difference(a))
#{'Jill'}

#see union of all sets
print(a.union(b))
#{'Jake', 'Jill', 'Eric', 'John'}

################################ classes ################################

#you can create a template for your data with classes

class Vehicle:
    #variables under class
    name = ""
    kind = "car"
    color = ""
    value = ""
    #create function called "description" ("self" to refer to variables in class itself)
    def description(self):
        #"self" to refer to variables in class itself, with string (%s) or number to 2 decimals (%.2f) specified
        description = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return description

#input variable for multiple cars
#car1 = red convertible worth $60,000.00 with a name of Fer
#car2 = blue van named Jump worth $10,000.00

#assign cars to class
car1 = Vehicle()
car2 = Vehicle()

#input variables for car1
car1.name = "Fer"
car1.kind = "convertible"
car1.color = "red"
car1.value = 60000.00
#input variables for car2
car2.name = "Jump"
car1.kind = "van"
car2.color = "blue"
car2.value = 10000.00

#access function (description) in class
print(car1.description())
#Fer is a red van worth $60000.00.
print(car2.description())
#Jump is a blue car worth $10000.00.

################################ dictionaries ################################

#dictionaries are like databases of information, where data can be accessed using a unique identifier (key)

#dictionaries vs. lists
    #dictionaries/lists are ordered + changeable
    #dictionaries don't allow duplicates

#create dictionary with {}
phonebook = {}

#enter data into dictionary
phonebook = {
    "The Kleg" : 2508082553,
    "Helena" : 7788221876
}
#or
phonebook["The Dads"] = 7787102207
phonebook
#{'The Kleg': 2508082553, 'Helena': 7788221876, 'The Dads': 7787102207}

#delete data
del phonebook["Helena"]
#or
phonebook.pop("Helena")
phonebook
#{'The Kleg': 2508082553, 'The Dads': 7787102207}

#apply commands to dictionary like you would a list
for name, number in phonebook.items():
    if name.endswith("s"):
        print("%s' number is %d" % (name, number))
    else:
        print("%s's number is %d" % (name, number))
#[The Kleg's number is 2508082553]
#[The Dads' number is 7787102207]


#-------------------------------------------------------------------------------------------------------------------------------


################################ writing blocks (several commands combined) ################################

#indent instead of curly bracket to combine commands into 1 command
x = 1
if x == 1:
    print("x is 1")

#fibonacci sequence: add last 2 numbers together
a, b = 0, 1
while a < 10:
    print(a)
    #as series moves to the right: a becomes b, b becomes a+b (fib seq)
    a, b = b, a+b
#0
#1
#1
#2
#3
#5
#8
#prints single "a" on each line!
#use "end" function to end "a" with something (eg. comma), so it prints entire output on one line
while a < 10:
    print(a, end=",")
    a, b = b, a+b
#[0,1,1,2,3,5,8,]

################################ intro to writing functions ################################

### defining functions ###

#make fib seq block into function with "def"
def fib_seq(a, b):
    while a < 10:
        print(a, end=" ")
        a, b = b, a+b

fib_seq(0, 1)
#[0 1 1 2 3 5 8]

################################ string formatting ################################

### 1. % (specifier) ###
# % = placeholder (specify what this should be)
    # %s (placeholder for string)
    # %f (floating point number)
    # %d (digit)

myint = 28

if isinstance(myint, int) and myint > 10:
    print("%d" % myint)
#[28]

columns = 3
rows = 18
print("you have %d rows and %d columns" % (rows, columns))
#[you have 18 rows and 3 columns]

#can also insert values from list
s = "The sum of %d and %d is %d"
x = [1, 2, 3]
print(s % tuple(x))
#The sum of 1 and 2 is 3

#can insert list
organisms = ["cat", "bear", "ant", "dog", "elephant", "n/a", "a"]
def printer(a):
    print("The animals are... %s" % (list(a)))
printer(organisms)
#The animals are... ['cat', 'bear', 'ant', 'dog', 'elephant', 'n/a', 'a']

### 2. str.format() ###

#insert variables into string
name = "John"
age = 28
"{}'s age is {}.".format(name, age)
#can specify which index number to insert where
"{1}'s age is {0}.".format(age, name)
#"John's age is 28."

phonebook = {
    "name" : "Helena",
    "number": 7788221876
}
#can define variables from dictionary (not class)
"{name}'s number is {number}.".format(name=phonebook["name"], number=phonebook["number"])
#or
"{name}'s number is {number}.".format(**phonebook)
#[Helena's number is 7788221876.]

### 3. f-strings ###

name = "john"
age = 28
f"{name}'s age is {age}."
F"{name}'s age is {age}."
#"john's age is 28."

#can put functions in string
def capitalized(x):
    return x.capitalize()
f"{capitalized(name)}'s age is {age}."
#"John's age is 28."

#__str__() vs. __repr__()
#both methods (member functions like x.function())
    #str gives string
    #repr gives 'string'

# review:
    # %s (placeholder for string)
    # %f (floating point number)
    # %d (digit)

def example_function():
    print("hello!")
def timer(func):
    run_time = 5.98745
    #__name__ is an attribute
    #f-string default to __str__(), force __repr__() with !r to get quotation marks
    #variable:.4f for floating point number to 4 decimal places
    print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
timer(example_function)
#Finished 'example_function' in 5.9874 secs

################################ if/else ################################

big_animals = ["bear", "giraffe", "elephant"]
cats = ["cat", "tiger", "cheetah"]

animal = "tiger"

if animal in big_animals:
    print("match in big_animals!")
elif animal in cats:
    print("match in cats!")
else:
    print("no match!")
#[match in cats!]

################################ for/while loops ################################

#for loops
#range doesn't include the upper boundary
c = list(range(1, 10))
for number in c:
    if number >= 5:
        print(number, end=" ")
#[5 6 7 8 9]

#while loops

#while number < 10, keep adding a to b repeatedly
a=0
b=1
while a < 10:
    print(a, end=" ")
    a, b = b, a+b
#[0 1 1 2 3 5 8]

#while number < 20, keep adding 2 repeatedly
while a < 20:
    print(a, end=" ")
    a = a+2
#[0 2 4 6 8 10 12 14 16 18]

################################ generators ################################

#generators are simple functions which return an iterable set of items, looping after the "yield" statement
    #import "random" package to generate random numbers
#generator vs. for loop
    #generator GENERATES numbers in a loop, rather than looping over a list
    #you can only use a generator once!
    #generator doesn't run until called

def lottery():
    #range(2) is the same as range(0, 2)
    for i in range(2):
        yield rd.randint(1,40)

    yield rd.randint(1,15)

#if you saved the generator itself as a variable, you couldn't use the variable twice!
generator=lottery()
for n in generator:
    print(n, end=" ")
#[6 27 6]
#try again:
for n in generator:
    print(n, end=" ")
#[ ]
#can't use generators twice!

#solution 1:
#coerce generator output (<generator object lottery at 0x000001D38A666880>) to list, then save list as variable
lottery_list = list(lottery())
lottery_list
#[22, 10, 4]

#solution 2:
#using the generator function directly would allow you to continuously use the generator
def lottery_print():
    for n in lottery():
        yield "The next number is... %d!" % n
list(lottery_print())
#['The next number is... 22!', 'The next number is... 21!', 'The next number is... 9!']

### return vs. yield ### 

#compare lottery_print() above using "yield" to this one using "return"
def lottery_print():
    for n in lottery():
        return "The next number is... %d!" % n
(lottery_print())
#'The next number is... 22!'
#only stored 1 number out of 3, because function stops at first return

#challenge: write generator for fibonacci sequence
def fib(n):
    #has to be inside function, otherwise "UnboundLocalError: local variable 'a' referenced before assignment"?
    a, b = 0, 1
    #good way to loop function n number of times
    for n in range(n):
        #yield first so series starts with 0
        yield a
        a, b = b, a+b
print(list(fib(10)))
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

#challenge 2: give infinite fib seq generator, get series up to 1000

def inf_fib():
    a, b = 0, 1
    #iter() returns iterable object until it reaches sentinel character (1)
    #int() always returns 0
    for n in iter(int, 1):
        yield a
        a, b = b, a+b
#or
def inf_fib_2():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

for n in inf_fib():
    if n < 1000:
        print(n, end=" ")
#this keeps looping since you didn't break it with "return"
#have to break loop
for n in inf_fib_2():
    if n < 1000:
        print(n, end=" ")
    else:
        break
#[0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987]


#-------------------------------------------------------------------------------------------------------------------------------


################################ applying commands to lists (list comprehension) ################################

#if applying operator to object with 1 value, no problem
y = 2
y ** 2
#[4]

# 1. for loops ----------------------------------------------

#apply operator to entire list
#challenge: list squares of 1-10
c = list(range(1, 11))
result = [number ** 2 for number in c]
result
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#find words (>1 letter) in list starting with "a" 
organisms = ["cat", "bear", "ant", "dog", "elephant", "n/a", "a"]
result = [aword for aword in organisms if aword.startswith("a") and re.findall("a+\w", aword)]
result
#['ant']

#another method:
for aword in organisms:
    if aword.startswith("a") and re.findall("a+\w", aword):
        print("%s starts with an A" % aword)
#[ant starts with an A]

#--------------------------------

### how to run command on specific index value in list? ###

#specify index position with list[x:y]
#note: [-1] means last number, [0,-1] encompasses entire list

def lottery():
    #range(2) is the same as range(0, 2)
    for i in range(2):
        yield rd.randint(1,40)

    yield rd.randint(1,15)

lottery_list = list(lottery())
lottery_list
#[22, 10, 4]

lottery_list[1:-1]
def printer():
    for i in lottery_list[:2]:
        print("The next number is... %d!" % i)
    for j in lottery_list[2:]:
        print("And the last number is... %d!" % j)
#or
def printer():
    for i in range(2):
        print("The next number is... %d!" % lottery_list[i])
    for j in range(2,3):
        print("And the last number is... %d!" % lottery_list[j])
printer()
#The next number is... 22!
#The next number is... 10!
#And the last number is... 4!

# 2. map() ----------------------------------------------

#can use "map" to apply function to each item in a list/tuple
    # map(func, *iterables)   
        #map() takes however many arguments func requires
    #really simplifies code

def summer(a, b):
    return a + b
#convert to list since "<map object at 0x000001D38A69BFD0>" unreadable
#use map() to sum individual numbers from each list
result = list(map(summer, (1, 2, 3), (5, 6, 7)))
result
#[6, 8, 10]

#challenge: round my_floats to 2 decimal places
my_floats = [4.355, 6.095, 3.255, 9.775, 2.165, 8.885, 4.595]

round_to = [2]*len(my_floats)

#map() w/ lambda function
map_result = list(map(lambda x: round(x, 2), my_floats))
#map() w/o lambda function
map_result = list(map(round, my_floats, round_to))
#for loop
map_result = [round(x, 2) for x in my_floats]
map_result
#[4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

### reduce() ###

# reduce(func, iterable, initial value)
    #reduces num1*num2 to 1 value (product) and passes back to function

#if multiple arguments are in the same object, you need to use reduce()
c = list(range(1, 11))
def internal_multiplier(num1, num2):
    return num1 * num2

reduce(internal_multiplier, c)
#[3628800]
#can specify first value in loop
reduce(internal_multiplier, c, 10)
#[36288000]

# 3. * ----------------------------------------------

# *list unpacks the list into individual items

big_animals = ["bear", "giraffe", "elephant"]

def announcement(a, *b):
    print("The winner is... %s" % a)
    print("Honourable mentions are... %s" % b)
announcement(big_animals[0], big_animals[1:3])
#The winner is... bear
#Honourable mentions are... ['giraffe', 'elephant']

# 4. round-bracket generator ----------------------------------------------

def summer(ls):
    return list(number ** 2 for number in ls)
summer(c)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


#-------------------------------------------------------------------------------------------------------------------------------


################################ modules/packages ################################

#modules AKA .py files
#many modules compiled into a package (directory)

#specify additional directories to look for modules/packages
PYTHONPATH=/directory python_game.py
#or
sys.path.append("/directory")

#import pyplot module from matplotlib package
from matplotlib import pyplot
#or
import matplotlib.pyplot

#import matplotlib package 
import matplotlib
#same as importing all modules from package (note: not good if package components change)
from matplotlib import *

#abbreviate packages so easier to type commands
import matplotlib as plt

#when importing module, .pyc file created so python doesn't have to parse files each time module is loaded

def histogram(a):
    plt.hist(a, bins = 20)

#if this script is executed, run command histogram()
if __name__ == '__main__':
    histogram()

#local variables in module initialized only once (as a "singleton")
#even if another module imports the same module again

#singleton: class (eg. object) that is initialized only once
class Singleton(object):
    __instance = None

    def __new__(a):
        if a.__instance is None:
            a.__instance = super(Singleton,a).__new__(a)
            a.__instance.__initialized = False
        return a.__instance

    def __init__(self):      
        if(self.__initialized): return
        self.__initialized = True
        print ("INIT")

x = Singleton()
#[INIT]
y = Singleton()
print (x is y)
#[True]

#or more simply: (initialize function_1 as a singleton)
class Singleton():
    ...
function_1 = Singleton()

#Q: what is the point of a singleton?

### writing packages ###

#every package MUST contain __init__.py in its directory (specifies it's a package)

#can specify which modules to load from package in __init__.py
__all__ = ["pyplot"]

################################ exception handling ################################

#exception = python's solution to error

#try/except block defines what to do when exception is raised
def printer(n):
    print(n)
def exception_handled():
    tuple = (1,2,3)
    for i in range(5):
        try:
            printer(tuple[i])
        #IndexError raised when accessing a non-existing index of a list
        except IndexError:
            printer("No more numbers!")
exception_handled()
#1
#2
#3
#No more numbers!
#No more numbers!

#challenge: return last name of actor
actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name(): 
    #"string".split(separator)[index]
    return actor["name"].split()[1]
get_last_name()

################################ serialization ################################

#data can be serialized and stored in JSON file, then transferred to another server/app
#use json module to encode and decode data

#json data can be in 2 formats:
    #object datastructure: applies python methods to datastructure
    #string: pass data into another datastructure/program

#encode datastructure to JSON using .dumps
json_string = json.dumps([1,2,3,"a"])

#load (decode) JSON back to a datastructure using the .loads method
print(json.loads(json_string))
#[1, 2, 3, 'a']

#python serializes data using pickle (or cPickle) package
pickled_json_string = pickle.dumps([1,2,3,"a"])
print(pickle.loads(pickled_json_string))
#[1, 2, 3, 'a']

#challenge: add "Me": 800 to dictionary and print JSON contents
salaries = '{"Alfred" : 300, "Jane" : 400 }'

def add_employee(salaries_json, name, salary):
    #decode JSON object to "salaries"
    salaries = json.loads(salaries_json)
    #remember: add to dictionary using dictionary[key] = x
    salaries[name] = salary
    #encode "salaries" to JSON object
    return json.dumps(salaries)
new_salaries_json = add_employee(salaries, "Me", 800)
#decode new_salaries_json
decoded_salaries = json.loads(new_salaries_json)
print(decoded_salaries)
#{'Alfred': 300, 'Jane': 400, 'Me': 800}
