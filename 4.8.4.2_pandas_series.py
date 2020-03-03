#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ## 1 Use pandas to create a Series from the following data:
# 
# ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

# In[2]:


vowels = ['aeiou']


# ##### a. Name the variable that holds the series fruits.

# In[3]:


fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", 
          "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])


# In[4]:


fruits


# ##### b. Run .describe() on the series to see what describe returns for a series of strings.

# In[5]:


fruits.describe()


# ##### c. Run the code necessary to produce only the unique fruit names.

# In[6]:


fruits.unique()


# ##### d. Determine how many times each value occurs in the series.

# In[7]:


fruit_name_count = fruits.value_counts()
fruit_name_count


# ##### e. Determine the most frequently occurring fruit name from the series.

# In[8]:


most_frequent_fruit = fruit_name_count.head(1)
most_frequent_fruit


# ##### f. Determine the least frequently occurring fruit name from the series.

# In[9]:


least_frequent_fruit = fruit_name_count.tail(1)
least_frequent_fruit


# ##### g. Write the code to get the longest string from the fruits series.

# In[10]:


longest_fruit_name = fruits[fruits.str.len() == fruits.str.len().max()]
longest_fruit_name


# ##### h. Find the fruit(s) with 5 or more letters in the name.

# In[11]:


fruits_with_five_or_more = fruits[fruits.str.len() >= 5]
fruits_with_five_or_more


# ##### i. Capitalize all the fruit strings in the series.

# In[12]:


capitalize_fruit_names = fruits.str.capitalize()
capitalize_fruit_names


# ##### j. Count the letter "a" in all the fruits (use string vectorization)

# In[21]:


a_count = fruits.str.count('a').sum()
a_count


# ##### k. Output the number of vowels in each and every fruit.

# In[26]:


fruits.str.count(r'[aeiou]')


# ##### l. Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

# In[33]:


fruits[fruits.apply(lambda s: s.count('o') > 1)]


# ##### m. Write the code to get only the fruits containing "berry" in the name

# In[38]:


fruits[fruits.str.contains('berry')]


# ##### n. Write the code to get only the fruits containing "apple" in the name

# In[39]:


fruits[fruits.str.contains('apple')]


# ##### o. Which fruit has the highest amount of vowels?

# In[46]:


longest_fruit_name = fruits[fruits.str.count(r'[aeiou]') == fruits.str.count(r'[aeiou]').max()]
longest_fruit_name


# ### 3. Use pandas to create a Series from the following data:

# In[47]:


dollar_amounts = pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', 
                            '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', 
                            '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', 
                            '$452,650.23'])
                           
                           
                           


# - What is the data type of the series?

# In[ ]:





# - Use series operations to convert the series to a numeric data type.

# In[ ]:





# - What is the maximum value? The minimum?

# In[ ]:





# - Bin the data into 4 equally sized intervals and show how many values fall into each bin.

# In[ ]:





# - Plot a histogram of the data. Be sure to include a title and axis labels.

# In[ ]:





# ### 4. Use pandas to create a Series from the following exam scores:

# In[ ]:


[60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]


# In[ ]:


get_ipython().set_next_input('What is the minimum exam score? The max, mean, median');get_ipython().run_line_magic('pinfo', 'median')
Plot a histogram of the scores.
Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.
Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.


# ### 5. Use pandas to create a Series from the following string:

# In[ ]:


'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'


# In[ ]:


get_ipython().set_next_input('What is the most frequently occuring letter? Least frequently occuring');get_ipython().run_line_magic('pinfo', 'occuring')
get_ipython().set_next_input('How many vowels are in the list');get_ipython().run_line_magic('pinfo', 'list')
get_ipython().set_next_input('How many consonants are in the list');get_ipython().run_line_magic('pinfo', 'list')
Create a series that has all of the same letters, but uppercased
Create a bar plot of the frequencies of the 6 most frequently occuring letters.

