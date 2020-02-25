#!/usr/bin/env python
# coding: utf-8

# In[83]:


filename = "data/import_exercises.py"


# In[84]:


with open(filename, "r") as f:
    contents = f.readlines()


# In[90]:


with open(filename, "r") as f:
    contents = f.readlines()
    for i, line in enumerate(contents, 1):
        print(i, ": ", line)


# In[157]:


# Write some python code to create a grocery list.
# Create a variable named grocery_list. It should be a list, and the elements in the list 
# should be a least 3 things that you need to buy from the grocery store.

grocery_list = ['Milk', 'Cheese', 'Eggs', 'Bacon']


# In[158]:


# Create a function named make_grocery_list. When run, this function should write the 
# contents of the grocery_list variable to a file named my_grocery_list.txt.

def make_grocery_list(grocery_list):
    file_name = "my_grocery_list.txt"
    with open(file_name, "w") as f:
        for item in grocery_list:
            f.writelines(item + "\n")


# In[159]:


make_grocery_list(grocery_list)


# In[160]:


# Create a function named show_grocery_list. When run, it should read the items from 
# the text file and show each item on the grocery list.
def show_grocery_list():
    file_name = "my_grocery_list.txt"
    with open(file_name, "r") as f:
        contents = f.readlines()
        for item in contents:
            print(item)


# In[161]:


show_grocery_list()


# In[162]:


# Create a function named buy_item. It should accept the name of an item on the grocery list, 
# and remove that item from the list.
def buy_item(item, grocery_list):
    grocery_list.remove(item)
    make_grocery_list(grocery_list)
        
    


# In[163]:


buy_item('Bacon', grocery_list)


# In[164]:


show_grocery_list()

