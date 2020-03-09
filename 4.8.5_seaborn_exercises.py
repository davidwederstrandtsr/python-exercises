#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pydataset import data

get_ipython().run_line_magic('matplotlib', 'inline')
pd.options.display.max_rows = 99


# In[2]:


pd.DataFrame(data())


# In[3]:


def get_db_url(dbname) -> str:
    url = 'mysql+pymysql://{}:{}@{}/{}'
    return url.format(env.user, env.password, env.host,dbname)


# In[4]:


iris = sns.load_dataset('iris')
iris.dtypes


# In[5]:


iris


# # Use the iris database to answer the following quesitons:

# - What does the distribution of petal lengths look like?

# In[6]:


plt.figure(figsize=(10, 8))
sns.distplot(iris.petal_length, kde=False)


# - Is there a correlation between petal length and petal width?

# In[7]:


plt.figure(figsize=(10, 8))
iris_data = pd.crosstab(iris.petal_width, iris.petal_length)
sns.heatmap(iris_data.corr(), cmap=plt.cm.Greens)


# - Would it be reasonable to predict species based on sepal width and sepal length?

# In[8]:


plt.figure(figsize=(10, 8))
sns.lmplot(data=iris, y='sepal_length', x='sepal_width', hue='species')


# - Which features would be best used to predict species?

# In[9]:


sns.pairplot(iris, hue='species')


# ### 1. Using the lesson as an example, use seaborn's load_dataset function to load the anscombe data set. Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. What do you notice?

# In[10]:


anscombe = sns.load_dataset('anscombe')
anscombe.dtypes


# In[11]:


anscombe.groupby('dataset').describe()


# ###### Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

# In[12]:


sns.relplot(x='x', y='y', col='dataset', data=anscombe)


# In[13]:


sns.lmplot(data=anscombe, y='y', x='x', col='dataset')


# ## 2. Load the InsectSprays dataset and read it's documentation. 

# In[14]:


insect_sprays = data('InsectSprays')
insect_sprays.head(10)


# In[15]:


data('InsectSprays', show_doc=True)


# - Create a boxplot that shows the effectiveness of the different insect sprays.

# In[16]:


plt.figure(figsize=(10, 8))

sns.boxplot(data=insect_sprays, y='count', x='spray')
plt.suptitle('Insect Spray Effectiveness')
plt.ylabel("Count of insects treated")
plt.xlabel("Type of Spray")


# ## 3. Load the swiss dataset and read it's documentation. 
# -- Create visualizations to answer the following questions:

# In[17]:


swiss = data('swiss')


# In[18]:


swiss


# - Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)

# In[19]:


# provinces with greater than 75.0% are considered Catholic
def is_catholic(num):
    return num >= 60.0


# In[20]:


swiss['Is_Catholic'] = swiss.Catholic.apply(is_catholic)


# - Does whether or not a province is Catholic influence fertility?

# In[21]:


sns.pairplot(x_vars=['Catholic', 'Agriculture', 'Examination', 'Infant.Mortality'], y_vars='Fertility', data=swiss)


# - What measure correlates most strongly with fertility?

# In[22]:


swiss.corr().Fertility


# ANSWER: is_catholic has the strongest correlation when considered for fertility

# ## 4. Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.

# In[23]:


def get_db_url(database):
    from env import host, user, password
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'


# In[24]:


db_name = "chipotle"
db_table = "orders"
url = get_db_url(db_name)
url
query ='SELECT * FROM orders'
chipotle = pd.read_sql(query, url)


# In[25]:


def convert_to_float(str):
    return float(str.strip('$'))

chipotle["item_total"] = chipotle.item_price.apply(convert_to_float)
chipotle
# orders.item_price = orders.item_price.str.replace('$', '').str.replace(',', '').astype('float')


# In[26]:


most_popular = chipotle.groupby('item_name').quantity.agg(['count'])


# In[27]:


most_popular = chipotle.groupby('item_name').item_total.agg([sum]).nlargest(n=4, columns='sum')
most_popular


# In[28]:


plt.figure(figsize=(10, 8))

sns.barplot(data=most_popular, x=most_popular.index, y='sum')

plt.suptitle('Chipotle Most Popular Item by Revenue', fontsize=16)
plt.ylabel("")
plt.xlabel("\nMenu Item", fontsize=14)

plt.show()


# 

# ## 5. Load the sleepstudy data and read it's documentation. 
# #### - Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.

# In[29]:


sleep = data('sleepstudy')
sleep.Subject = 'subject_' + sleep.Subject.astype(str)
sleep.head()


# In[30]:


plt.figure(figsize=(12, 8))
plt.title("Days to Reaction Time")
sns.lineplot(data=sleep, y='Reaction', x='Days', hue='Subject', alpha=.4)
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 0.8), shadow=False, ncol=1)


# In[31]:



plt.figure(figsize=(12, 8))
sns.lineplot(data=sleep, y='Reaction', x='Days', color='navy')


# In[32]:


plt.figure(figsize=(12, 8))

sns.lineplot(data=sleep, y='Reaction', x='Days', hue='Subject', alpha=.4)
sns.lineplot(data=sleep, y='Reaction', x='Days', color='navy')

plt.legend(loc='upper center', bbox_to_anchor=(1.1, 0.8), shadow=False, ncol=1)


# In[ ]:




