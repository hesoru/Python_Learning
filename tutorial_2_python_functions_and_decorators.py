#!/usr/bin/python
# -*- coding: utf-8 -*-

# author: github.com/hesoru/

from cgi import print_environ
# functools: tools for working with functions (and other callable objects)
import functools
# time: timer
import time

################################ table of contents ################################

# review: defining functions
    # return vs. print
# lambda (anonymous) functions
# partial functions
# pass functions to other functions
# nested functions
# closures

# decorators
# nonparametric decorators
# parametric decorators
# decorating classes
# applying multiple decorators

###################################################################################


#-------------------------------------------------------------------------------------------------------------------------------


################################ review: defining functions ################################

# make fib seq block into function with "def"
def fib_seq(a, b):
    while a < 10:
        print(a, end=" ")
        a, b = b, a+b

fib_seq(0, 1)
# [0 1 1 2 3 5 8]

# args vs kwargs:
    # *args (non-keyword arguments): arguments without key
    # **kwargs (keyword arguments): arguments with key (eg. variables in dictionary)

# functions with multiple arguments
# *_ denotes all args after the first 3
def multi_arg_function(a, b, c, *d):
    print("First: %d" % a)
    print("Second: %d" % b)
    print("Third: %d" % c)
    # have to use %s for list or it won't print
    print("and all the rest... %s" % (list(d)))
multi_arg_function(1, 2, 3, 4, 5)
# First: 1
# Second: 2
# Third: 3
# and all the rest... [4, 5]

# possible to specify options in function arguments
# **_ denotes all kwargs
def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %d" % (key, value))
result = myfun(4, first=1, second=2, third=3)
# first == 1
# second == 2
# third == 3

# you can set function options using kwargs!
def multi_option_function(*a, **b):
    if b.get("action") == "sum":
        print(sum(i for i in a))
    if b.get("numbers") == "all":
        for i in a:
            print(i, end=" ")
result = multi_option_function(1, 2, 3, 4, action = "sum", numbers = "all")
# 10
# 1 2 3 4

### return vs. print ###

# return can only be used inside a function

# if you need to funnel function output into variable: use return/yield (generator function), not print
def lottery_print():
    for n in lottery_list[:6]:
        print("The next number is... %d!" % n)
lottery = lottery_print()
lottery
# [ ]
# output not stored in variable if using print

################################ lambda (anonymous) functions: when we require a function for a short time ################################

def double(x):
    return x * 2
# this can be written as a lambda function
double = lambda x: x * 2
double(5)
# [10]

# challenge: give boolean if number in l odd
l = [2,4,7,3,14,19]

for i in l:
    split = lambda i: i % 2
    if split(i) != 0:
        print("True")
    else:
        print("False")
# simpler
l = [2,4,7,3,14,19]
for i in l:
    split = lambda i: i % 2 == 1
    print(split(i))
# False
# False
# True
# True
# False
# True

# lambda functions in map()

my_floats = [4.355, 6.095, 3.255, 9.775, 2.165, 8.885, 4.595]

# calculate squares to 2 decimal places
list(map(lambda x: round(x ** 2, 2), my_floats))
# [18.97, 37.15, 10.6, 95.55, 4.69, 78.94, 21.11]

################################ partial functions ################################

# partial functions: convert variable in function to fixed value,
# creating a more limited function with fewer arguments

# import "partial" module of "functools" package

def multiply(x, y):
    return x * y
double = partial(multiply, 2)
# replaces variables starting from the left (ie. 2 replaces x)
double(4)
# [8]

# challenge: create partial function that replaces first 3 variables and outputs 60
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x
new = partial(func, 6, 6, 6)
print(new(6))
# [60]

### pass functions to other functions ###

def plus_one(n):
    return n + 1
def function_call(function):
    number_to_add = 5
    return function(number_to_add)
# can use function like object in another function
function_call(plus_one)
# return plus_one(number_to_add)
# [6]

################################ nested functions ################################

# function inside another function

def transmit_to_space(message):
    "This is the enclosing function"
    # variables in enclosing function can be accessed as readonly by nested function
    def data_transmitter():
        "The nested function"
        # use "nonlocal" to modify variables in a nested function
        nonlocal message
        if type(message) == int:
            message = "Error Code"
        print(message)
    # run nested function
    data_transmitter()
print(transmit_to_space("Testing"))
# Testing
# None
print(transmit_to_space(101))
# Error Code
# None

def transmit_to_space(message):
    "This is the enclosing function"
    # variables in enclosing function can be accessed as readonly by nested function
    def data_transmitter():
        "The nested function"
        # use "nonlocal" to modify variables in a nested function
        print(message)
    # run nested function
    data_transmitter()
print(transmit_to_space("Testing"))

################################ closures ################################

def multiplier_of(n):
    def multiplier(number):
        return number*n
    # can return function as object
    return multiplier
# using function object, can create new function with fixed argument (ie. closure) 
multiplywith5 = multiplier_of(5)
print(multiplywith5(9))
# [45]


#-------------------------------------------------------------------------------------------------------------------------------


################################ decorators ################################

# decorator: a function which takes a function and returns one
    # allows you to modify a callable object (eg. function/method/class) without modifying its structure
    # compactifies functions into single function that you can export
    # partial function can be decorator

################################ nonparametric decorators (no arguments) ################################

def uppercase(function):
    def wrapper():
        #defines argument as function, turns it into object to use with .upper()
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def say_hi():
    return 'hello there'

# pass say_hi() function to uppercase() function, returning function wrapper()
uppercase(say_hi)
# <function uppercase.<locals>.wrapper at 0x000002014FF11990>

decorator = uppercase(say_hi) #this returns wrapper(), so you've created a function called "decorator"
decorator()
# decorator() calls function wrapper()
# say_hi().upper() = 'hello there'.upper()
# 'HELLO THERE'

# same as nonparametric decorator (no arguments for decorator)
@uppercase
def say_hi_uppercase():
    return 'hello there' #put say_hi() function here
say_hi_uppercase()
# 'HELLO THERE'

#-------------------------------

# Q: why can't you just do this? why the nested function?

def uppercase(function):
    make_uppercase = function().upper()
    return make_uppercase

def say_hi():
    return 'hello there'

# pass say_hi() function to uppercase() function, returning make_uppercase variable (string 'HELLO THERE')
uppercase(say_hi)
# 'HELLO THERE'

decorator = uppercase(say_hi) #this returns 'HELLO THERE', so you've created a variable called "decorator" (not a function)
decorator()
# TypeError: 'str' object is not callable
# you can't call a variable, it's not a function!
msg()
# calling the variable msg return the same error

# A: without a nested function, you can't return a function to then call "decorator"

#-------------------------------

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1. take start time
        value = func(*args, **kwargs)       # 2. run func
        end_time = time.perf_counter()      # 3. take end time
        run_time = end_time - start_time    # 4. calculate run time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def time_summing_numbers(num_times):
    #what does _ mean?
    for i in range(num_times):
        sum([i**2 for i in range(10000)])

time_summing_numbers(500)
# Finished 'time_summing_numbers' in 1.7840 secs


################################ parametric decorators (contain arguments) ################################

def multiply(multiplier):
    def multiply_function(old_function):
        # kwargs are options
        def new_function(*args, **kwargs):
            return multiplier * old_function(*args, **kwargs)
        return new_function
    return multiply_function

def old_function():
    return 2

# could do a closure here
multiply_by_3 = multiply(3) #fix multiplier as 3

decorator = multiply_by_3(old_function)
# multiply_by_3(old_function), ie. multiply_function(old_function) returns new_function()
decorator()
# 6

# can also call (multiply_by_3(old_function)) function without naming it
(multiply_by_3(old_function))()
# 6

# parametric decorator: contains argument(s)
@multiply(3) # fix multiplier argument as 3
def multiply_2_by_3():
    return 2 # put old_function() here
multiply_2_by_3()
# 6

# you can also insert old_function as an argument so you can modify it
@multiply(3) # fix multiplier argument as 3
def return_number(number):
    return number 
return_number(7) # set multiply_function(old_function) to multiply_function(7)?
# 21

# rule: for every new pair of brackets, add a layer of nesting to your function

def multiply(3):
    def multiply_function(return_number):
        # kwargs are options
        def new_function(7):
            return 3 * return_number(7)
        return new_function
    return multiply_function

#-----------------------------------

def generate_power(exponent):
    def power(func):
        def base(*args):
            nbase = func(*args)
            return nbase ** exponent
        return base
    return power

def base_number():
    return 7

raise_two = generate_power(2)
raise_7_to_2 = raise_two(base_number)
raise_7_to_2()
# 49

@generate_power(2) # fix exponent argument as 2
def raise_two(base_number):
    return base_number

def raise_two(base_number):
    return base_number
raise_two = generate_power(2)(raise_two)
# can pass class to function too

raise_two(4) # set power(func) to power(7)?
# 16

#-----------------------------------

# why not this? why the double-nested function?

def generate_power(exponent):
    def power(func):
        nbase = func()
        return nbase ** exponent
    return power

def base_number():
    return 7

raise_two = generate_power(2) # does this not return power()?
raise_two(base_number) # set power(func) to power(7), returning 7 ** 2?
# TypeError: 'int' object is not callable
raise_7_to_2 = raise_two(base_number)
raise_7_to_2()

@generate_power(2) 
def raise_two(old_function):
    return old_function
# TypeError: raise_two() missing 1 required positional argument: 'func'
# raise_two(7) rolled out here looks like raise_two(func()), because no arg in func()
raise_two(7)


def generate_power(nbase, exponent):
    def power(func):
        def base(*args):
            add = func(*args)
            return nbase ** exponent + add
        return base
    return power

# multiple parameter decorator: 2+ arguments
@generate_power(7, 2) # fix nbase as 7 and exponent as 2
def raise_two(func):
    return func # return power(func(*args))

raise_two(3)
# rolls out as: 3 = func(*args)
def generate_power(7, 2):
    def power(func):
        def base(*args):
            3 = func(*args)
            return 7 ** 2 + 3
        return base
    return power
# 52

################################ decorating classes ################################

def add_print(cls):
    # cls.print prints output of lambda function
    cls.print = lambda self: print(self.model)
    return cls

@add_print
class Vehicle:
    def __init__(self, model):
        self.model=model
    def __call__(self):
        print(self.model)

v=Vehicle("Honda")
v.print()
v()

################################ applying multiple decorators ################################

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

def uppercase(function):
    def wrapper():
        # defines argument as function, turns it into object to use with .upper()
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# decorators run from bottom to top! (from inside to outside)
# ie. uppercase then split into list (.upper wouldn't work on a list)
@split_string
@uppercase
def say_hi():
    return 'hello there'

say_hi()
# ['HELLO', 'THERE']


# challenge-----------------------------------

# fill in the function so decorator works
    # decorator should check if input is correct type before running the function
    # otherwise print("Bad Type")

# parametric decorator means 3 defs
def type_check(correct_type):

    # insert code here

    def inner_check(function):
        def checker(arg):
            if type(arg) == correct_type:
                return function(arg)
            else:
                print("Bad Type")
        return checker
    return inner_check

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
# 4
times2('Not A Number')
# Bad Type

@type_check(str)
def first_letter(word):
    # return first letter in string
    return word[0]

print(first_letter('Hello World'))
# H
first_letter(['Not', 'A', 'String'])
# Bad Type
