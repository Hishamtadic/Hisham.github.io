#!/usr/bin/env python
# coding: utf-8

# # Project: Medical Appointment No Shows :-
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Introduction
# 
# ### Dataset Description 
# 
# 110.527 medical appointments its 14 associated variables (characteristics). The most important one if the patient show-up or no-show to the appointment. Variable names are self-explanatory, and i will be investigating this problem furher.
# 
# 
# 
# ### Question(s) for Analysis
# -  what are the reasons of no showing, whom is responsible for this ?

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# Upgrade pandas to use dataframe.explode() function. 
#!pip install --upgrade pandas==0.25.0


# <a id='wrangling'></a>
# ## Data Wrangling:

# In[2]:


df= pd.read_csv('KaggleV2-May-2016.csv')
df.shape


# In[3]:


df.head()


# columns names need to be changed (Hipertension, No-show)

# In[4]:


df.info()


# In[5]:


df.duplicated().sum()


# no null/duplicates values but their is columns can be dropped

# In[6]:


df.describe()


# the Age min value is negative which will be dealt with

# 
# ### Data Cleaning:
# 

# In[7]:


df.columns


# In[11]:


#drop the negative values
df_x = df.query('Age == "-1" ')
df_x
df.drop(index = 99832, inplace = True )


# In[12]:


# rename column 
df.rename({'No-show' : 'No_Show', 'Hipertension' : 'Hypertension'}, axis = 1,  inplace = True)
df.head()


# In[13]:


# remove duplicates of PatientId
df['PatientId'].duplicated().sum()


# In[14]:


df.drop_duplicates(['PatientId', 'No_Show'], inplace = True)
df.shape


# In[15]:


#drop unnecessary columns
df.drop(columns = ['PatientId', 'AppointmentID','ScheduledDay', 'AppointmentDay' ], inplace = True)


# In[16]:


df.columns


# <a id='eda'></a>
# ## Exploratory Data Analysis:
# 
# 
# 
# 
# ### Research Question1 :  what are the reasons of no showing, whom is responsible for this ?!
# 

# In[17]:


df.head()


# In[18]:


df['No_Show'].value_counts()


# In[19]:


# firstly split the data into Appointment No Shows and Shows
Show = df.No_Show == 'No'
NoShow = df.No_Show == 'Yes'


# In[40]:


# i would love to see if the Alcoholism Patient shows or no!
df['Alcoholism'].value_counts()
sns.barplot(x= 'Alcoholism', y= 'No_Show', data = df)
plt.title('Influence of Alcoholism ')


# okay the Alcoholism NoShow Patients is more than the shows as expected

# In[22]:


#lets see if the Gender of the Patient influence the shows 
df['Gender'].value_counts()


# females numbers almost double of males maybe cuz the usually responsible for the kids 

# In[38]:


def shows(df, column, Show, NoShow):
    df[column][Show].value_counts().hist(alpha = 0.5, bins = 20, label = 'Show')
    df[column][NoShow].value_counts().hist(alpha = 0.5, bins = 20, label = 'NoShow')
    plt.legend();
    plt.title('Influence of Gender')
    plt.xlabel('Gender')
    plt.ylabel('No_Show')


# In[39]:


shows(df, 'Gender', Show, NoShow)


# No i don't think Gender matters !

# In[28]:


#for furhter investigation lets see the Handcap effect on shows 
df['Handcap'].value_counts()


# In[29]:


df[Show]['Handcap'].value_counts()


# In[30]:


df[NoShow]['Handcap'].value_counts()


# okay i figuerd out that the Handcap(1,2) Patients Shows Percantage is clearly greater than the NoShow

# In[31]:


# what is the influence of Scholarship on showing?!
df['Scholarship'].value_counts()


# In[32]:


df[NoShow]['Scholarship'].value_counts().plot(kind = 'pie')


# No don't think the Scholarship matters.

# In[33]:


# the mean age of Show
df[Show].Age.mean()


# In[34]:


#the mean age of NoShow
df[NoShow].Age.mean()


# the mean age of Shows is bigger than the Noshow

# In[37]:


df.Age[Show].hist(alpha=0.5, bins=20, label='Show')
df.Age[NoShow].hist(alpha=0.5, bins=20, label='NoShow')
plt.legend();
plt.title('Influence of Age')
plt.xlabel('Age')
plt.ylabel('num_Patients')


# by using hist its looks like vice versa!

# <a id='conclusions'></a>
# ## Conclusions
# 
# - Firstly, i can summarize my Data Wrangling and Data Cleaning : i faced no problem at all assessing the data and clean it as it just contains few errors,like negative Age value and some un porper columns name like(hiper and the - instead of _).
# and some id duplicates that i dropped to make the analysis clear.
# - second the analyzing process was a little bit complicated and i found that :-
#   - The Alcoholism Patient number whom Show is less than the NoShow as expected.
#   - Then we investigated through the Gender and found that it didn't influence the Patients shows.
#   - For furhter investigation we checked the influence of the Handcap on showing and found that Handcap(1,2) Patients Shows    
#     Percantage is clearly greater than the NoShow.
#   - Then what is the influence of Scholarship on showing?! i found that its almost has no influence on shows.
#   - And the mean age of Shows is bigger than the Noshow but the hist illustrates its vice versa.
# - Finally i think we do need more Awareness campaigns to encourage the Patients not to hesitate to go to the doctor
#   and also we need to reconsider the appointment schedule of the Patients.
# 
# limitations :-
# it was the (PatientId, AppointmentID, ScheduledDay, AppointmentDay) data.
#   
# 
# 
# ## Submitting your Project 
# 
# 

# In[41]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

