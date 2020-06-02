#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"C:\Users\SAI\Downloads\Survey_Resp.csv")


# In[5]:


df.head() # print first 5 rows of data set


# In[7]:


df.shape #no.of rows & columns in the given data set


# In[8]:


a = df.tail(4) # Assigned last 4 rows of dataset through tail to variable a


# In[9]:


a # printing the values that are passed into a


# In[10]:


df.columns


# In[18]:


pd.unique(df['COUNTRY_CODE']) # printing all the Unique values of the column COUNTRY_CODE to a list
pd.unique(df['COUNTRY_CODE'].tolist()) # this command this all the below diplayed values as list


# In[16]:


numOfRows = len(df.index) # displaying row count of dataframe by finding the length of index labels
print (numOfRows)


# In[22]:


# display the values of the First column that has country code as US
RespVal = df[df['COUNTRY_CODE'] == 'US']
RespVal['RESP_ID']


# In[ ]:




