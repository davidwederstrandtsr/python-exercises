#!/usr/bin/env python
# coding: utf-8

# **Use matplotlib to plot the following equation using LaTex:**
# 
# You'll need to write the code that generates the x and y points.
# 
# Add an anotation for the point **0, 0** , the origin.

# In[59]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import math


# Problem 1 - 
# Use matplotlib to plot the following equation:

# In[72]:


x = range(10)
y = [x**2 - x + 2 for x in x]

plt.plot(x, y)
plt.annotate('origin', xy=(0, 2), xytext=(0,  10),
            arrowprops={'facecolor': 'cyan'})
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = x^2 - x + 2$')
plt.show()


# Problem 2 - 
# Create and label 4 separate charts for the following equations (choose a range for x that makes sense):

# In[74]:


x = range(10)
y = [math.sqrt(x) for x in x]

plt.plot(x, y)
plt.annotate('origin', xy=(0, .2), xytext=(0,  1),
            arrowprops={'facecolor': 'cyan'})
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = \\sqrt{x}$')
plt.show()


# In[75]:


x = range(6)
y = [x**3 for x in x]

plt.plot(x, y)
plt.annotate('origin', xy=(0, 5), xytext=(0,  20),
            arrowprops={'facecolor': 'cyan'})
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = x^3$')
plt.show()


# In[76]:


x = range(1000)
y = [math.tan(x) for x in x]

plt.plot(x, y)
plt.title('$y = \\tan(x)$')
plt.show()


# In[77]:


x = range(5)
y = [2**x for x in x]

plt.plot(x, y)
plt.annotate('origin', xy=(0, 1), xytext=(0,  4),
            arrowprops={'facecolor': 'cyan'})
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = 2^x$')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




