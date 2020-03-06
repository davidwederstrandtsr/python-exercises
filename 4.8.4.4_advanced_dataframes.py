#!/usr/bin/env python
# coding: utf-8

# In[1]:


from env import host, user, password
import pandas as pd
import numpy as np
import math


# In[2]:


db_name = "employees"


# In[3]:


url = f'mysql+pymysql://{user}:{password}@{host}/employees'


# In[4]:


query ='SELECT * FROM employees LIMIT 5 OFFSET 50'


# In[5]:


pd.read_sql(query, url)


# In[6]:


pd.read_sql('SHOW TABLES', url)


# ## 1. Load the mpg dataset. Read the documentation for it, and use the data to answer these questions:

# In[7]:


from pydataset import data
mpg = data('mpg')
data('mpg', show_doc=True)


# - On average, which manufacturer has the best miles per gallon?

# In[8]:


mpg.groupby('manufacturer').hwy.agg(['median']).nlargest(n=1, columns="median")


# - How many different manufacturers are there?

# In[9]:


mpg.manufacturer.nunique()


# - How many different models are there?

# In[10]:


mpg.model.nunique()


# In[11]:


print(mpg)


# - Do automatic or manual cars have better miles per gallon?

# In[12]:


(mpg
 .assign(trans_mode=mpg.trans.apply(lambda n: 'automatic' if 'auto' in n else 'manual'))
        .groupby(['trans_mode'])
        .hwy.agg(['median']))


# ## 2. Joining and Merging

# - Copy the users and roles dataframes from the examples above.

# In[13]:


users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users


# In[14]:


roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles


# - What do you think a right join would look like? An outer join? 

# In[15]:


pd.merge(users, roles, left_on='role_id', right_on='id', how='right')


# In[16]:


pd.merge(users, roles, left_on='role_id', right_on='id', how='outer')


# #### - What happens if you drop the foreign keys from the dataframes and try to merge them?
# 
# we would not be able to join the table because the lack of indexes

# ## 3. Getting data from SQL databases

# #### a. Create a function named get_db_url. It should accept a username, hostname, password, and database name and return a url formatted like in the examples in this lesson.

# In[17]:


def get_db_url(database):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'


# In[ ]:





# #### b. Use your function to obtain a connection to the employees database.

# In[18]:


url2 = get_db_url(db_name)
pd.read_sql(query, url2)


# #### c. Once you have successfully run a query:

# - Intentionally make a typo in the database url. What kind of error message do you see?

# In[19]:


url3 = f'mysql+pymysql://{users}:{password}@{host}/employees/'
# pd.read_sql(query, url3)


# OperationalError: (pymysql.err.OperationalError) (1045, "Access denied for user '   
# id   name  role_id\n0   1    bob      1.0\n1   '@'97.105.19.58' (using password: YES)"

# - Intentionally make an error in your SQL query. What does the error message look like?

# In[20]:


#query2 ='SELECT * FROM employes'
#pd.read_sql(query2, url)


# ProgrammingError: (pymysql.err.ProgrammingError) (1146, "Table 'chipotle.employes' doesn't exist")
# [SQL: SELECT * FROM employes]

# In[21]:


query2 ='SELECT * FROM employees'
query3 ='SELECT * FROM titles'
query4 ='SELECT * FROM departments'
query5 ='SELECT * FROM dept_emp'


# ProgrammingError: (pymysql.err.ProgrammingError) (1146, "Table 'employees.employes' doesn't exist")
# [SQL: SELECT * FROM employes LIMIT 5 OFFSET 50]

# #### d. Read the employees and titles tables into two separate dataframes

# In[22]:


employees = pd.read_sql(query2, url)
titles = pd.read_sql(query3, url)
departments = pd.read_sql(query4, url)
dept_emp = pd.read_sql(query5, url)
employees


# In[23]:


titles


# #### e. Visualize the number of employees with each title.

# In[24]:


titles.groupby('title').emp_no.agg(['count']).plot.bar()


# #### f. Join the employees and titles dataframes together.

# In[25]:


et = pd.merge(
    employees, 
    titles,
    left_on='emp_no',
    right_on='emp_no',
    how='left'
)

et


# #### g. Visualize how frequently employees change titles.

# In[26]:


et.groupby('emp_no').title.agg(['count']).plot.hist()


# #### h. For each title, find the hire date of the employee that was hired most recently with that title.

# In[27]:


et.groupby('title').hire_date.agg(['max'])


# #### i. Write the code necessary to create a cross tabulation of the number of titles by department. 
# (Hint: this will involve a combination of SQL and python/pandas code)

# In[28]:


de = pd.merge( 
    dept_emp,
    departments,
    left_on='dept_no',
    right_on='dept_no',
    how='left'
)

de


# In[29]:


det = pd.merge( 
    et,
    de,
    left_on='emp_no',
    right_on='emp_no',
    how='left'
)

det


# In[30]:


et


# In[43]:


titles_by_departments = pd.crosstab(det.dept_name, det.title)
titles_by_departments


# In[50]:


#titles_by_departments.plot.bar()


# ## 4. Use your get_db_url function to help you explore the data from the chipotle database. Use the data to answer the following questions:

# In[33]:


db_name = "chipotle"
db_table = "orders"
url = get_db_url(db_name)
url
query ='SELECT * FROM orders'
chipotle = pd.read_sql(query, url)
chipotle


# #### - What is the total price for each order?

# In[34]:


def convert_to_float(str):
    return float(str.strip('$'))
    


# In[39]:


# chipolte['item_price'] = chipotle['item_price'].replace('[\$]', '', regex=True).astype(float)
chipotle["item_total"] = chipotle.item_price.apply(convert_to_float)
chipotle


# In[40]:


chipotle.groupby('order_id').item_total.sum()


# In[ ]:





# #### - What are the most popular 3 items?

# In[41]:


chipotle.groupby('item_name').quantity.agg(['count']).nlargest(n=3, columns="count")


# #### - Which item has produced the most revenue?

# In[42]:


chipotle.groupby('item_name').item_total.agg(['sum']).nlargest(n=1, columns="sum")


# In[ ]:




