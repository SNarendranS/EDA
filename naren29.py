#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
df=pd.read_csv('D:/insurance.csv')
df.head()


# In[15]:


df.columns


# In[14]:


df.describe


# In[88]:


df.tail()
df.info()


# In[97]:


x=df.age
y=df.charges
plt.scatter(x,y,c='g')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Graph in 2D')
plt.savefig('Test.png')


# In[98]:


plt.plot(x,y,'r--',linestyle='dashed',linewidth=2, markersize=12)
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('2d Diagram')


# In[99]:


plt.subplot(2,2,1)
plt.plot(x,y,'r--')
plt.subplot(2,2,2)
plt.plot(x,y,'g*--')
plt.subplot(2,2,3)
plt.plot(x,y,'bo')
plt.subplot(2,2,4)
plt.plot(x,y,'go')


# In[146]:


x=df.sex
y=df.age
x2 = df.children
y2 =df.charges
plt.bar(x, y) 
plt.bar(x2, y2, color = 'r') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  
plt.show()


# In[143]:


a = df.charges
plt.hist(a) 
plt.title("histogram") 
plt.show()


# In[142]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="children",y="age",data=df)


# In[139]:


sns.countplot(x="children",data=df,palette=['blue','red','orange','yellow','green','green'])


# In[137]:


sns.boxplot(data=df, x="age", y="sex") 


# In[112]:


df['age'].unique()


# In[113]:


df.isnull().sum()


# In[119]:


labels = 'age', 'children', 'bmi', 'charges'
sizes = [215, 130, 245, 210]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.4, 0, 0, 0)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=False)
plt.axis('equal')
plt.show()


# In[120]:


df.corr()
sns.heatmap(df.corr())


# In[125]:


sns.violinplot(x=df["age"])


# In[130]:


sns.set_theme(style="whitegrid")
sns.countplot(x=df["age"])


# In[132]:


sns.countplot(data=df, x="age", hue="sex")


# In[149]:


sns.jointplot(data=df, x="age", y="children", hue="sex")


# In[ ]:




