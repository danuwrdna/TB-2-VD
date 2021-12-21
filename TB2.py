#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


tugasbesar = pd.read_csv("kreditjerman1.csv")
tugasbesar.head()


# In[4]:


cancer_sur = pd.read_csv("kreditjerman1.csv", header=None, names=["age","opertaion_year","axil_nodes_det","surv_status"])
cancer_sur.head()


# In[5]:


print(cancer_sur.describe())


# In[6]:


sns.barplot(data=cancer_sur)


# In[7]:


sns.FacetGrid(cancer_sur,hue="surv_status",height = 5).map(sns.distplot,"age").add_legend()


# In[8]:


sns.scatterplot(data=cancer_sur)


# In[9]:


sns.kdeplot(data=cancer_sur)


# In[13]:


# Visualizing the data using heatmap
sns.heatmap(tugasbesar.corr(), cmap="YlGnBu", annot = True)
plt.show()


# In[14]:


# Importing naumpy and pandas libraries to read the data

# Supress Warnings
import warnings
warnings.filterwarnings('ignore')

# Import the numpy and pandas package
import numpy as np
import pandas as pd

# Read the given CSV file, and view some sample records
tugasbesar = pd.read_csv("kreditjerman1.csv")
tugasbesar


# In[ ]:




