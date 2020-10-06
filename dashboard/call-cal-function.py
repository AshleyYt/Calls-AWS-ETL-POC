#!/usr/bin/env python
# coding: utf-8

# In[22]:


def calAgents(Calls, AHT, SL, TAT, Shrinkage):
    if AHT < 1 or AHT > 30000 or SL < 0.00001 or SL > 0.9998 or TAT < 1 or TAT > 30000 or Shrinkage < 0.00001 or Shrinkage > 0.9998:
        return -1
    
    Intensity = (Calls/(60*60))*AHT
    
    minagents = int(Intensity)
    agents = minagents
    
    while serviceLevel(Calls, AHT, TAT, agents) < SL:
        agents = agents + 1
    
    if Shrinkage < 0:
        Shrinkage = 0 
    elif Shrinkage > 1:
        Shrinkage = 0.99
    
    calAgents = agents / (1-Shrinkage)
    
    if Calls == 0:
        calAgents = 0
    
    return calAgents


# In[28]:


import math
def serviceLevel(Calls, AHT, TAT, agents):
    if AHT < 1 or AHT > 30000 or SL < 0.00001 or SL > 0.9998 or TAT < 1 or TAT > 30000:
        return -1
    
    Intensity = (Calls/(60*60))*AHT
    serviceLevel = 1 - (erlangC(Intensity, agents) * math.exp(-(agents-Intensity)*TAT/AHT))
    
    if serviceLevel > 1:
        serviceLevel = 1
    elif serviceLevel < 0:
        serviceLevel = 0
        
    return serviceLevel


# In[29]:


def erlangC(Intensity, agents):
    erlangC = (top_row(Intensity, agents)) / ((top_row(Intensity, agents)) + ((1 - utilisation(Intensity, agents)) * bottom_row(Intensity, agents)))
    
    if erlangC < 0:
        erlangC = 0
    elif erlangC > 1:
        erlangC = 1
    return erlangC


# In[30]:


import math
def top_row(Intensity, agents):
    return (Intensity**agents)/ math.factorial(agents)

def bottom_row(Intensity, agents):
    k = 0
    mx = agents
    answer = 0
    
    for k in range(0, mx):
        answer = answer + ((Intensity**k))/math.factorial(k)
    
    return answer


# In[31]:


def utilisation(Intensity, agents):
    utilisation = Intensity / agents
    
    if utilisation < 0:
        utilisation = 0
    elif utilisation > 1:
        utilisation = 1
    return utilisation


# In[32]:


AHT = 480
SL = 0.95
TAT = 60
Shrinkage = 0.15
Calls = 21
calAgents(Calls, AHT, SL, TAT, Shrinkage)


# In[ ]:




