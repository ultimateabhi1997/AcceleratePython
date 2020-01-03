#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
df1=pd.read_excel(r'C:\\Users\\Abhishek\\Desktop\\2 JMPSheetCreation\\Input\\FG_Worker_list3.xls')
df2=pd.read_excel(r'C:\\Users\\Abhishek\\Desktop\\2 JMPSheetCreation\\Input\\SOW_Mapping2.xlsx')
df1
df2


# In[14]:


result=pd.merge(df1,df2,on='SOW ID')


# In[15]:


excel_FG_SOW=result.to_excel(r'C:\\Users\\Abhishek\\Desktop\\2 JMPSheetCreation\\Input\\FG_SOW3.xlsx')


# In[16]:


df3=pd.read_excel(r'C:\\Users\\Abhishek\\Desktop\\2 JMPSheetCreation\\Input\\FG_SOW3.xlsx')
df3


# In[17]:


df4=pd.read_excel(r'C:\\Users\\Abhishek\\Desktop\\2 JMPSheetCreation\\Input\\JML_Blank.xlsx')
df4


# In[20]:


finalmerge=pd.merge(df3,df4,how='outer',on='SOW ID')


# In[21]:


finalExcel=finalmerge.to_excel(r'C:\\Users\\Abhishek\\Desktop\\2 JMPSheetCreation\\Input\\FG_SOW_JML.xlsx')


# In[ ]:




