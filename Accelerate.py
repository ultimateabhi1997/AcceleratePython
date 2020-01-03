#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
df=pd.read_excel(r'C:\Users\Abhishek\Desktop\2 JMPSheetCreation\Input\FG_Worker_list.xls')
print(df)


# In[4]:


df.drop_duplicates(subset="Worker ID", keep="first",inplace=True)


# In[5]:


print(df)


# In[6]:


df_filtered=df[df['Worker End Date']>=df['Worker Start Date']]


# In[7]:


print(df_filtered)


# In[8]:


from pandas import DataFrame
export_excel=df.to_excel(r'C:\\Users\\Abhishek\\Desktop\\2 JMPSheetCreation\\Input\\FG_Worker_list2.xls')
print(df)


# In[ ]:




