#!/usr/bin/env python
# coding: utf-8

# In[19]:


# 파이썬 라이브러리
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


# In[28]:


pip show kaggle


# In[29]:


kaggle config view


# In[ ]:




