#!/usr/bin/env python
# coding: utf-8

# **Use matplotlib to plot the following equation using LaTex:**
# 
# You'll need to write the code that generates the x and y points.
# 
# Add an anotation for the point **0, 0** , the origin.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt
import math


# Problem 1 - 
# Use matplotlib to plot the following equation:

# In[2]:


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

# In[3]:


x = range(10)
y = [math.sqrt(x) for x in x]

plt.plot(x, y)
plt.annotate('origin', xy=(0, .2), xytext=(0,  1),
            arrowprops={'facecolor': 'cyan'})
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = \\sqrt{x}$')
plt.show()


# In[4]:


x = range(6)
y = [x**3 for x in x]

plt.plot(x, y)
plt.annotate('origin', xy=(0, 5), xytext=(0,  20),
            arrowprops={'facecolor': 'cyan'})
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = x^3$')
plt.show()


# In[5]:


x = range(1000)
y = [math.tan(x) for x in x]

plt.plot(x, y)
plt.title('$y = \\tan(x)$')
plt.show()


# In[6]:


x = range(5)
y = [2**x for x in x]

plt.plot(x, y)
plt.annotate('origin', xy=(0, 1), xytext=(0,  4),
            arrowprops={'facecolor': 'cyan'})
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = 2^x$')
plt.show()


# ### Problem 3 
# Combine the figures you created in the last step into one large figure with 4 subplots.

# In[57]:


# y = x^2 - x + 2
x1 = range(15)
y1 = [x1**2 - x1 + 2 for x1 in x1]

# y = sqrt(x)
x2 = range(200)
y2 = [math.sqrt(x2) for x2 in x2]

# y = x^3
x3 = range(8)
y3 = [x3**3 for x3 in x3]

# y = tan(x)
x4 = range(1000)
y4 = [math.tan(x4) for x4 in x4]

# y = 2^x
x5 = range(10)
y5 = [2**x5 for x5 in x5]


# In[64]:


plt.figure(figsize=(18, 18))
plt.suptitle('5 plots condensed to one')

# Figure 1
plt.subplot(3, 2, 1)
plt.plot(x1, y1)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = x^2 - x + 2$')

# Figure 2
plt.subplot(3, 2, 2)
plt.plot(x2, y2)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = \\sqrt{x}$')

# Figure 3
plt.subplot(3, 2, 3)
plt.plot(x3, y3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = x^3$')

# Figure 4
plt. subplot(3, 2, 4)
plt.plot(x4, y4)
plt.title('$y = \\tan(x)$')

# Figure 5
plt.subplot(3, 2, 5)
plt.plot(x5, y5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('$y = 2^x$')
plt.show()


# ### Problem 4
# 
# Combine the figures you created in the last step into one figure where each of the 4 equations
# 
# has a different color for the points. Be sure to include a legend.

# In[61]:


plt.figure(figsize=(16, 8))
plt.suptitle('5 plots condensed to one')

# Figure 1
plt.plot(x1, y1, c='red', label='$y = x^2 - x + 2$')
plt.xlabel('x')
plt.ylabel('y')

# Figure 2
plt.plot(x2, y2, c='green', label='$y = \\sqrt{x}$')
plt.xlabel('x')
plt.ylabel('y')

# Figure 3
plt.plot(x3, y3, c='orange', label='$y = x^3$')
plt.xlabel('x')
plt.ylabel('y')

# Figure 4
plt.plot(x4, y4, c='pink', ls='--', label='$y = \\tan(x)$')

# Figure 5
plt.plot(x5, y5, label='$y = 2^x$')
plt.xlabel('x')
plt.ylabel('y')

# 
plt.ylim(-250, 350)
plt.xlim(0, 16)
plt.legend()
plt.show()

