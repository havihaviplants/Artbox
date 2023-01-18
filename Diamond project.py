#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np #상관계수 관련 라이브러리 
import pandas as np
import numpy

from scipy.stats import pearsonr # 피어슨 상관계수 가져오기


# In[47]:


df = pd.read_csv("https://raw.githubusercontent.com/AliHaider20/AIM-5001/main/diamonds.csv").drop("Unnamed: 0", axis=1)
# Checking if the dataframe is correctly loaded.
df.head()


# In[48]:


df.describe().T


# In[49]:


print(len(df))
df.info();


# In[50]:


df.cut.value_counts(normalize=True)


# In[51]:


df.clarity.value_counts(normalize=True)


# In[52]:


df.color.value_counts(normalize=True)


# In[59]:


X = df.carat.values
Y = df.depth.values #carat과 depth 사이의 산점도

#두 변수 간 관련성을 시각적으로 알 수 있다.
#순열 공식에 따르면 기준 점 7개 중 두 개의 연관성을 짝지었을 때 42개의 경우의 수가 존재하는데 일부만 추출

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('carat ~ depth')
plt.xlabel('carat')
plt.ylabel('depth')
plt.show()

correlation = pearsonr(X,Y)
print(correlation)


# In[60]:


X = df.cut.values
Y = df.carat.values #cut과 carat 사이의 산점도

#두 변수 간 관련성을 시각적으로 알 수 있다.
#깎인 정도와 캐럿 사이의 관련수치를 상관계수로 찾아보았다.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('cut ~ carat')
plt.xlabel('cut')
plt.ylabel('carat')
plt.show()


# In[69]:


X = df.color.values
Y = df.clarity.values #color과 clarity 사이의 산점도

#두 변수 간 관련성을 시각적으로 알 수 있다.
#색깔 별로 동일. 색깔과 맑음의 정도는 무관한 것으로 결론.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('color ~ clarity')
plt.xlabel('color')
plt.ylabel('clarity')
plt.show()


# In[68]:


X = df.carat.values
Y = df.table.values #carat과 table 사이의 산점도

#두 변수 간 관련성을 시각적으로 알 수 있다.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('carat ~ table')
plt.xlabel('carat')
plt.ylabel('table')
plt.show()

correlation = pearsonr(X,Y)
print(correlation)


# In[70]:


X = df.carat.values
Y = df.price.values #carat & price

#두 변수 간 관련성을 시각적으로 알 수 있다.
#색깔 별로 동일. 색깔과 맑음의 정도는 무관한 것으로 결론.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('carat ~ price')
plt.xlabel('carat')
plt.ylabel('price')
plt.show()


correlation = pearsonr(X,Y)
print(correlation)


# In[73]:


X = df.color.values
Y = df.table.values #color & table

#두 변수 간 관련성을 시각적으로 알 수 있다.
#색깔 별로 동일. 색깔과 맑음의 정도는 무관한 것으로 결론.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('color ~ table')
plt.xlabel('color')
plt.ylabel('table')
plt.show()


# In[76]:


X = df.color.values
Y = df.price.values #color & price

#두 변수 간 관련성을 시각적으로 알 수 있다.
#색깔 별로 동일. 색깔과 맑음의 정도는 무관한 것으로 결론.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('color ~ price')
plt.xlabel('color')
plt.ylabel('price')
plt.show()


# In[77]:


X = df.clarity.values
Y = df.price.values #clarity & price

#두 변수 간 관련성을 시각적으로 알 수 있다.
#색깔 별로 동일. 색깔과 맑음의 정도는 무관한 것으로 결론.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('clarity ~ price')
plt.xlabel('clarity')
plt.ylabel('price')
plt.show()


# In[78]:


X = df.price.values
Y = df.cut.values # price & cut

#두 변수 간 관련성을 시각적으로 알 수 있다.
#색깔 별로 동일. 색깔과 맑음의 정도는 무관한 것으로 결론.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('price ~ cut')
plt.xlabel('price')
plt.ylabel('cut')
plt.show()


# In[79]:


X = df.price.values
Y = df.color.values # price & color

#두 변수 간 관련성을 시각적으로 알 수 있다.
#색깔 별로 동일. 색깔과 맑음의 정도는 무관한 것으로 결론.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('price ~ color')
plt.xlabel('price')
plt.ylabel('color')
plt.show()


# In[80]:


X = df.price.values
Y = df.clarity.values # price & clarity

#두 변수 간 관련성을 시각적으로 알 수 있다.
#색깔 별로 동일. 색깔과 맑음의 정도는 무관한 것으로 결론.

import matplotlib.pyplot as plt
plt.scatter(X, Y, alpha=0.5)
plt.title('price ~ clarity')
plt.xlabel('price')
plt.ylabel('clarity')
plt.show()


# In[ ]:




