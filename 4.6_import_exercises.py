#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 1. Import and test 3 of the functions from your functions exercise file.

#    Your functions exercise are not currently in a file with a name that can be easily imported. 
#    Copy your functions exercise file and name the copy functions_exercises.py.

#    Import each function in a different way:

#         import the module and refer to the function with the . syntax
#         use from to import the function directly
#         use from and give the function a different name


# In[1]:


import functions_exercises


# In[2]:


assert functions_exercises.calculate_tip(10, 100) == 110
assert functions_exercises.calculate_tip(10, 110) != 110


# In[3]:


from functions_exercises import handle_commas


# In[4]:


assert handle_commas('1,111') == 1111
assert handle_commas('1,111') != 1110


# In[5]:


from functions_exercises import get_letter_grade as glg


# In[6]:


assert glg(86) == 'B'
assert glg(86) != 'A'


# In[ ]:


# For the following exercises, read about and use the itertools module from the standard library 
# to help you solve the problem.


# In[ ]:


# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?


# In[10]:


from itertools import product

list(product("abc", ('123')))


# In[11]:


len(list(product("abc", ('123'))))


# In[ ]:


# 2. How many different ways can you combine two of the letters from "abcd"?


# In[13]:


from itertools import permutations

list(permutations("abcd", 2))


# In[14]:


len(list(permutations("abcd", 2)))


# In[ ]:


# Save this file as profiles.json inside of your exercises directory. Use the load function from the 
# json module to open this file, it will produce a list of dictionaries. Using this data, write some 
# code that calculates and outputs the following information:


# In[15]:


from json import load


# In[ ]:





# In[19]:


profiles = load(open("profiles.json"))


# In[ ]:


# Total number of users


# In[20]:


len(profiles)


# In[ ]:


# Number of active users


# In[25]:


len([profile for profile in profiles if profile['isActive'] == True])


# In[ ]:


# Number of inactive users


# In[27]:


len([profile for profile in profiles if profile['isActive'] == False])


# In[ ]:


# Grand total of balances for all users


# In[58]:


def only_number(string):
    new_string = string.replace(',','')
    new_string = new_string.replace('$', '')
    return float(new_string)


# In[64]:


profile_balances = [profile['balance'] for profile in profiles]
profile_balances


# In[83]:


newlist = []

for profile in profile_balances:
    newlist.append(only_number(profile))
newlist


# In[84]:


total = sum(newlist)


# In[85]:


# Average balance per user


# In[86]:


total / len(newlist)


# In[87]:


# User with the lowest balance


# In[88]:


min(newlist)


# In[96]:


minlist = []
minlist = [x for x in range(len(newlist)) if newlist[x] == min(new_list)]
minlist


# In[103]:


profiles[minlist[0]]['name'], profiles[minlist[0]]['balance']


# In[ ]:


# User with the highest balance


# In[99]:


maxlist = []
maxlist = [x for x in range(len(newlist)) if newlist[x] == max(new_list)]
maxlist


# In[104]:


profiles[maxlist[0]]['name'], profiles[maxlist[0]]['balance']


# In[ ]:


# Most common favorite fruit


# In[ ]:





# In[106]:


fruitlist = [profile['favoriteFruit'] for profile in profiles]
fruitlist


# In[112]:


fruit_count = [fruitlist.count(fruit) for fruit in fruitlist]
fruit_count


# In[118]:


newfruitlist = list(zip(fruit_count, fruitlist))


# In[122]:


newfruitlist


# In[119]:


max(newfruitlist)


# In[ ]:


# Least most common favorite fruit


# In[120]:


min(newfruitlist)


# In[ ]:


# Total number of unread messages for all users


# In[125]:


greetinglist = [profile['greeting'] for profile in profiles]
greetinglist


# In[128]:


def get_digits(string):
    new_string = ''
    for s in string:
        if s.isdigit():
            new_string += s
    return new_string


# In[132]:


new = []
for g in greetinglist:
    new.append(int(get_digits(g)))

sum(new)
    


# In[ ]:




