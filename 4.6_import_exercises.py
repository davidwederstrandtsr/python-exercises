#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1. Import and test 3 of the functions from your functions exercise file.

#    Your functions exercise are not currently in a file with a name that can be easily imported. 
#    Copy your functions exercise file and name the copy functions_exercises.py.

#    Import each function in a different way:

#         import the module and refer to the function with the . syntax
#         use from to import the function directly
#         use from and give the function a different name


# In[2]:


import functions_exercises


# In[3]:


assert functions_exercises.calculate_tip(10, 100) == 110
assert functions_exercises.calculate_tip(10, 110) != 110


# In[4]:


from functions_exercises import handle_commas


# In[5]:


assert handle_commas('1,111') == 1111
assert handle_commas('1,111') != 1110


# In[6]:


from functions_exercises import get_letter_grade as glg


# In[7]:


assert glg(86) == 'B'
assert glg(86) != 'A'


# In[8]:


# For the following exercises, read about and use the itertools module from the standard library 
# to help you solve the problem.


# In[9]:


# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?


# In[10]:


from itertools import product

list(product("abc", ('123')))


# In[11]:


len(list(product("abc", ('123'))))


# In[12]:


# 2. How many different ways can you combine two of the letters from "abcd"?


# In[13]:


from itertools import permutations

list(permutations("abcd", 2))


# In[14]:


len(list(permutations("abcd", 2)))


# In[15]:


# Save this file as profiles.json inside of your exercises directory. Use the load function from the 
# json module to open this file, it will produce a list of dictionaries. Using this data, write some 
# code that calculates and outputs the following information:


# In[16]:


from json import load


# In[ ]:





# In[17]:


profiles = load(open("profiles.json"))


# In[18]:


# Total number of users


# In[19]:


len(profiles)


# In[20]:


# Number of active users


# In[21]:


len([profile for profile in profiles if profile['isActive'] == True])


# In[22]:


# Number of inactive users


# In[23]:


len([profile for profile in profiles if profile['isActive'] == False])


# In[24]:


# Grand total of balances for all users


# In[25]:


def float_convertor(num):
    return float(num.replace(',','').replace('$',''))


# In[26]:


float_convertor('$12,000')


# In[27]:


profile_balances = [profile['balance'] for profile in profiles]
profile_balances


# In[28]:


newlist = []

for profile in profile_balances:
    newlist.append(float_convertor(profile))
newlist


# In[29]:


total = sum(newlist)


# In[30]:


# Average balance per user


# In[31]:


total / len(newlist)


# In[32]:


# User with the lowest balance


# In[33]:


min(newlist)


# In[34]:


minlist = []
minlist = [x for x in range(len(newlist)) if newlist[x] == min(newlist)]
minlist


# In[35]:


profiles[minlist[0]]['name'], profiles[minlist[0]]['balance']


# In[36]:


# User with the highest balance


# In[37]:


maxlist = []
maxlist = [x for x in range(len(newlist)) if newlist[x] == max(newlist)]
maxlist


# In[38]:


profiles[maxlist[0]]['name'], profiles[maxlist[0]]['balance']


# In[39]:


# Most common favorite fruit


# In[ ]:





# In[40]:


fruitlist = [profile['favoriteFruit'] for profile in profiles]
fruitlist


# In[41]:


fruit_count = [fruitlist.count(fruit) for fruit in fruitlist]
fruit_count


# In[42]:


newfruitlist = list(zip(fruit_count, fruitlist))


# In[43]:


newfruitlist


# In[44]:


max(newfruitlist)


# In[45]:


# Least most common favorite fruit


# In[46]:


min(newfruitlist)


# In[47]:


# Total number of unread messages for all users


# In[48]:


greetinglist = [profile['greeting'] for profile in profiles]
greetinglist


# In[49]:


def get_digits(string):
    new_string = ''
    for s in string:
        if s.isdigit():
            new_string += s
    return new_string


# In[50]:


new = []
for g in greetinglist:
    new.append(int(get_digits(g)))

sum(new)
    


# In[ ]:




