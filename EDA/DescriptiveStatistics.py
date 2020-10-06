#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import datetime
from datetime import date
import calendar


# In[128]:


df = pd.read_csv(r"\CallHistory.csv")
df.head(5)


# In[130]:


# Data Preprocessing
cols = list(df.columns)
# print(cols)
## Select columns and filter
selCols = ['Call Type','Campaign', 'Call Date', 'Call Time', 'Time Connect', 'Time ACW', 'Time Hold']
dfSel = df[selCols]
## filtering conditions: "Call_Type" is "Inb.Normal" and "Campaign" is CSRV and SPAN
dfSelFil = dfSel.loc[(dfSel['Call Type'] == "Inb.Normal") 
                     & (dfSel['Campaign'].isin(["CSRV", "SPAN"]))]


# In[132]:


print(dfSelFil.head())
# print(dfSelFil.dtypes)
dfSelFil.describe(include = 'all')

## the tablue below indicates that no missing values in the processed dataset


# ### New variables to be created
# 1. Average Handling Time (= Time Connect + Time ACW)(in seconds)
# 2. Month
# 3. WorkDay
# 4. Hour
# 5. Holding Time (may not need for now)

# In[133]:


## Function to convert time in seconds
def toSeconds(test):
    return int(test[2:4]) * 60 + int(test[5:7])


# In[134]:


## Averaging Handling Time
temp1 = []
for c in dfSelFil['Time Connect']:
    temp1.append(toSeconds(c))
temp2 = []
for c in dfSelFil['Time ACW']:
    temp2.append(toSeconds(c))
dfSelFil['AHT'] = [temp1[i] + temp2[i] for i in range(len(temp1))]


# In[135]:


## Month
dfSelFil['Month'] = [int(c.split('/')[0]) for c in dfSelFil['Call Date']]


# In[136]:


## Weekday
def findDay(c):
    m, d, y = (int(i) for i in c.split('/'))
    born = datetime.date(y, m, d)
    return born.strftime('%A')

ls = []
for c in dfSelFil['Call Date']:
    ls.append(findDay(c))
dfSelFil['Weekday'] = ls


# In[137]:


## Hour
dfSelFil['Hour'] = [int(c.split(':')[0]) for c in dfSelFil['Call Time']]


# In[138]:


ls = []
for c in dfSelFil['Time Hold']:
    ls.append(toSeconds(c))
dfSelFil["Holding"] = ls


# In[139]:


print(list(dfSelFil.columns))


# In[152]:


## select the precessed cols for analysis
modelCols = ['Campaign', 'Call Date', 'AHT', 'Month', 'Weekday', 'Hour', 'Holding']
modelDf = dfSelFil[modelCols]


# ### Insights

# In[153]:


modelDf.groupby('Campaign').count()


# In[154]:


modDfCSRV = modelDf.loc[(modelDf['Campaign'] == 'CSRV')]
modDfSPAN = modelDf.loc[(modelDf['Campaign'] == 'SPAN')]


# In[155]:


modDfCSRV.groupby(['Month','Weekday', 'Hour'])['AHT'].count()


# In[156]:


modDfCSRV.groupby(['Month'])['AHT'].count()


# Since there are only records for half year, month cannot play an indicator in this model

# In[157]:


modDfCSRV.groupby(['Weekday'])['AHT'].count().plot()


# In[159]:


modDfCSRV.to_csv(r"C:\Users\yyang\Dropbox\callCenterProject\CallHistory\proCSRV.csv")


# In[ ]:




