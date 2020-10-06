#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import sys
get_ipython().system(' {sys.executable} -m pip install holidays')


# In[4]:


from datetime import date
import holidays


# In[5]:


df = pd.read_csv(r"xxxxx.csv")
df.head(5)


# In[19]:


for d in holidays.US(years = [2017,2018]).items():
    print(d)


# In[13]:


us_holidays = holidays.US()
ls = []
for c in df['Call Date']:
    ls.append(c in us_holidays)
df['Holidays'] = ls


# In[15]:


df.to_csv(r"xxxxxx.csv")


# In[ ]:




