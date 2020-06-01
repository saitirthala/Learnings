#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[5]:


pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 200)


# In[10]:


survey = pd.read_csv(r'C:\Users\SAI\Downloads\Survey_Resp.csv')


# In[11]:


print(survey)


# In[15]:


survey.head()


# In[13]:


survey.columns


# In[16]:


headers = ["RESPONSE_ID","SURVEY_SCORE", "MASKED_IP", "SURVEY_DATE", "COUNTRY_CODE", "REGION"]
survey.columns = headers


# In[ ]:




