#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[9]:


J=pd.read_csv("games.csv")
J


# In[5]:


J.head()


# In[6]:


J.tail()


# In[7]:


J.info()


# In[10]:


J.describe()


# In[11]:


len(J)


# In[18]:


J.shape


# In[19]:


J.mean


# In[20]:


J.duplicated().sum()


# In[21]:


J['maxplayers'].unique()


# In[25]:


sns.countplot(J['maxplayers'])


# In[26]:


J.isnull().sum()


# In[30]:


J.replace(np.nan,'0',inplace = True)
J.isnull().sum


# In[32]:


J.dtypes

