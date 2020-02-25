#!/usr/bin/env python
# coding: utf-8

# 1. Import and test 3 of the functions from your functions exercise file.
#    Your functions exercise are not currently in a file with a name that can be easily imported. 
#    Copy your functions exercise file and name the copy functions_exercises.py.

#    Import each function in a different way:
#         import the module and refer to the function with the . syntax
#         use from to import the function directly
#         use from and give the function a different name

import functions_exercises

assert functions_exercises.calculate_tip(10, 100) == 110
assert functions_exercises.calculate_tip(10, 110) != 110

from functions_exercises import handle_commas

assert handle_commas('1,111') == 1111
assert handle_commas('1,111') != 1110

from functions_exercises import get_letter_grade as glg

assert glg(86) == 'B'
assert glg(86) != 'A'

# For the following exercises, read about and use the itertools module from the standard library 
# to help you solve the problem.

# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

from itertools import product

list(product("abc", ('123')))

len(list(product("abc", ('123'))))


# 2. How many different ways can you combine two of the letters from "abcd"?
from itertools import permutations

list(permutations("abcd", 2))
len(list(permutations("abcd", 2)))

# Save this file as profiles.json inside of your exercises directory. Use the load function from the 
# json module to open this file, it will produce a list of dictionaries. Using this data, write some 
# code that calculates and outputs the following information:

from json import load

profiles = load(open("profiles.json"))


# Total number of users
len(profiles)


# Number of active users
len([profile for profile in profiles if profile['isActive'] == True])


# Number of inactive users
len([profile for profile in profiles if profile['isActive'] == False])


# Grand total of balances for all users
def float_convertor(num):
    return float(num.replace(',','').replace('$',''))

profile_balances = [profile['balance'] for profile in profiles]
profile_balances

newlist = []

for profile in profile_balances:
    newlist.append(float_convertor(profile))
newlist

total = sum(newlist)


# Average balance per user
total / len(newlist)


# User with the lowest balance
min(newlist)

minlist = []
minlist = [x for x in range(len(newlist)) if newlist[x] == min(newlist)]
minlist

profiles[minlist[0]]['name'], profiles[minlist[0]]['balance']


# User with the highest balance
maxlist = []
maxlist = [x for x in range(len(newlist)) if newlist[x] == max(newlist)]
maxlist

profiles[maxlist[0]]['name'], profiles[maxlist[0]]['balance']


# Most common favorite fruit
fruitlist = [profile['favoriteFruit'] for profile in profiles]
fruitlist

fruit_count = [fruitlist.count(fruit) for fruit in fruitlist]
fruit_count

newfruitlist = list(zip(fruit_count, fruitlist))
newfruitlist

max(newfruitlist)


# Least most common favorite fruit
min(newfruitlist)


# Total number of unread messages for all users
greetinglist = [profile['greeting'] for profile in profiles]
greetinglist

def get_digits(string):
    new_string = ''
    for s in string:
        if s.isdigit():
            new_string += s
    return new_string

new = []
for g in greetinglist:
    new.append(int(get_digits(g)))

sum(new)
