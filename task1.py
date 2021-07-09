#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import pandas as pd
import numpy as np
import seaborn as sns                       #visualisation
import matplotlib.pyplot as plt             #visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[6]:


os.chdir('C:/Users/Saranya/Desktop/taskno1')


# In[7]:


df=pd.read_csv('books.csv')


# In[8]:


df.head()


# In[11]:


df.isnull()


# In[12]:


df.isnull().sum()


# In[15]:


df.shape


# In[17]:


df.dtypes


# In[18]:


df.publication_date.unique()


# In[26]:


df.info()


# In[28]:


duplicate=df.duplicated()
print(duplicate.sum())
df[duplicate]


# In[11]:


df_rate = df.groupby('title')['average_rating']
df_rate.columns = ['title','average_rating']
df_rate.head(20)


# In[12]:


df.head()


# In[18]:


sns.distplot(df['ratings_count'])


# In[22]:


sf = df['ratings_count'].value_counts()[0:20]
sns.barplot(x=sf,y=sf.index)


# In[27]:


tf = df['title'].value_counts()[0:20]
sns.barplot(x=tf,y=tf.index)
plt.title('Most famous books')


# In[28]:


xf=df['text_reviews_count'].value_counts()
xf


# In[31]:


import plotly.express as px


# In[48]:


px.pie(df,values = 'publisher' , title='Publisher Pie Chart')


# In[45]:


nf=pd.DataFrame(df.groupby('isbn13')['ratings_count'].count())
nf.sort_values('ratings_count',ascending=False).head()


# In[ ]:




