#!/usr/bin/env python
# coding: utf-8

# > **Tip**: Welcome to the Investigate a Dataset project! You will find tips in quoted sections like this to help organize your approach to your investigation. Once you complete this project, remove these **Tip** sections from your report before submission. First things first, you might want to double-click this Markdown cell and change the title so that it reflects your dataset and investigation.
# 
# # Project: No show appointments 
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
# This dataset collects information
# from 100k medical appointments in
# Brazil - where i will be analyzing why and the factors affecting the Patient NO show to the appointments dilemma  
# 
# 
# 
# 
# ### Question(s) for Analysis
# - What factors allows us to predict whether the patient will show up for their appointment ?
# 
# > **Tip**: Once you start coding, use NumPy arrays, Pandas Series, and DataFrames where appropriate rather than Python lists and dictionaries. Also, **use good coding practices**, such as, define and use functions to avoid repetitive code. Use appropriate comments within the code cells, explanation in the mark-down cells, and meaningful variable names. 

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sna
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:


# Upgrade pandas to use dataframe.explode() function. 
get_ipython().system('pip install --upgrade pandas==0.25.0')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# > **Tip**: In this section of the report, you will load in the data, check for cleanliness, and then trim and clean your dataset for analysis. Make sure that you **document your data cleaning steps in mark-down cells precisely and justify your cleaning decisions.**
# 
# 
# ### General Properties
# > **Tip**: You should _not_ perform too many operations in each cell. Create cells freely to explore your data. One option that you can take with this project is to do a lot of explorations in an initial notebook. These don't have to be organized, but make sure you use enough comments to understand the purpose of each code cell. Then, after you're done with your analysis, create a duplicate notebook where you will trim the excess and organize your steps so that you have a flowing, cohesive report.

# In[3]:


df = pd.read_csv('KaggleV2-May-2016.csv')
df.shape


# In[4]:


df.head()


# Alert column name error Hipertension 

# In[5]:


df.info()


#  - No null values 

# In[6]:


df.describe()


# Alert - number at the min age 

# In[7]:


df.duplicated().sum()


# No duplicates Rows

# 
# ### Data Cleaning
# > **Tip**: Make sure that you keep your reader informed on the steps that you are taking in your investigation. Follow every code cell, or every set of related code cells, with a markdown cell to describe to the reader what was found in the preceding cell(s). Try to make it so that the reader can then understand what they will be seeing in the following cell(s).
#  

# In[8]:


#drop the - Age value
df_1 = df.query('Age == "-1"')
df_1

df.drop(index =99832, inplace=True)


# In[9]:


# rename column 
df.rename({'Hipertension' : 'Hypertension'}, axis = 1,  inplace = True)
df.rename({'No-show' : 'No_show'}, axis = 1, inplace = True)
df.head()


# In[10]:


# check if there duplicated id and their attendance and drop them
df['PatientId'].duplicated().sum()
df.drop_duplicates(['PatientId', 'No_show' ], inplace = True)
df.shape


# In[11]:


#drop unnecessary columns
df.drop(columns = ['PatientId', 'AppointmentID', 'ScheduledDay', 'AppointmentDay'], inplace = True)
df.head()


# In[16]:


# we can split Data into two according to the NO-show column
df['No_show'].value_counts()
NoShow = df.No_show == 'Yes'
Show = df.No_show == 'No'
# see the count of show and no show
df[NoShow].count(), df[Show].count()


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > **Tip**: Now that you've trimmed and cleaned your data, you're ready to move on to exploration. **Compute statistics** and **create visualizations** with the goal of addressing the research questions that you posed in the Introduction section. You should compute the relevant statistics throughout the analysis when an inference is made about the data. Note that at least two or more kinds of plots should be created as part of the exploration, and you must  compare and show trends in the varied visualizations. 
# 
# 
# 
# > **Tip**: - Investigate the stated question(s) from multiple angles. It is recommended that you be systematic with your approach. Look at one variable at a time, and then follow it up by looking at relationships between variables. You should explore at least three variables in relation to the primary question. This can be an exploratory relationship between three variables of interest, or looking at how two independent variables relate to a single dependent variable of interest. Lastly, you  should perform both single-variable (1d) and multiple-variable (2d) explorations.
# 
# 
# ### Research Question1 What factors allows us to predict whether the patient will show up for their appointment ?
# 

# In[13]:


df[NoShow].mean()


# In[14]:


df[Show].mean()


# The mean age is almost equal in each category  /  
# nothing else can be recognized but the SMS_received its almost double at NoShow !

# In[26]:


# how age affect the showing def
def showing(df, column, show, noshow):
    
    plt.figure(figsize=(14,6))
    df[column][Show].hist(alpha=0.5, bins =20, label= 'Show')
    df[column][NoShow].hist(alpha=0.5, bins =20, label= 'NOshow')
    plt.legend();
    plt.xlabel('Age')
    plt.ylabel('Patients number')
    
showing(df, 'Age', Show, NoShow)   


# its clear that younger patients (children) is the most attendance due to their parents !      
# and the least attendance is the eldest patients
# 

# In[40]:


#dose  age with diseases effect the showing ?
df[Show].groupby(['Hypertension','Diabetes' ]).Age.mean().plot(kind = 'bar', color = 'red', label = 'Show')
df[NoShow].groupby(['Hypertension','Diabetes']).Age.mean().plot(kind = 'bar', color = 'blue', label = 'NoShow')
plt.legend()


# No the diseases dosn't affect the showing !

# In[46]:


# the effect of sending SMS to the Patient on the showing
def showing_2(df, column, show, noshow):
    plt.figure(figsize=(14,6))
    df[column][Show].hist(alpha = 0.5, bins = 20, label = 'Show')
    df[column][NoShow].hist(alpha = 0.5, bins = 20, label = 'NoShow')
    plt.legend();
    plt.title('effect of sending SMS')
    plt.xlabel('SMS_received')
    plt.ylabel('num of Pateint')

showing_2(df, 'SMS_received', Show, NoShow)    


# according to this hist the % of showing Patients whom didn't received the SMS is bigger than the % of whom received SMS !!

# In[48]:


# dose the Gender has an effect on the num of showing ?!
df['Gender'].value_counts()


# In[55]:


df[Show]['Gender'].value_counts().plot(kind = 'pie')


# In[56]:


df[NoShow]['Gender'].value_counts().plot(kind= 'pie')


# the % of Show and NoShow of males and females almost identical so i don't think Gender affect the showing.

# In[62]:


plt.figure(figsize=(18,6))
df[Show]['Neighbourhood'].value_counts().plot(kind = 'bar', color= 'red', label = 'Show')
df[NoShow]["Neighbourhood"].value_counts().plot(kind = 'bar', color = 'blue', label = 'NoShow')
plt.legend()


# yes the Neighbourhood affected the showing of Patients.

# <a id='conclusions'></a>
# ## Conclusions
# 
# - Firstly, i can summarize my Data Wrangling and Data Cleaning : i faced no problem at all assessing the data and clean it as it just contains few errors,like one age cell was negative and some un porper columns name like(hiper and the - instead of _).
# - second the analyzing process was a little bit complicated and i found that :-
#   - The Age has a big effect on the showing of the patient as the children are often showing than the least showing the elder.
#   - Then we tested the Age once more but with the diseases this time and we found out that the diseases dosen't effect the         showing.
#   - Third step was checking whether sending SMS was crucial for showing Patient or not but iam surprised that its vice verca as     the percantage of Showing Patients whom didn't receive an SMS is much higher than whom received,we can conclude that there     is a problem at the content and context of the SMS needed to be checked well.
#   - Then i checked the effect of the Gender on the showing and i found that it has no strong effect on the showing.
#   - Lastly i check the effect of the Neighbourhood on the Patients showing and yes as expected it affected the showing.
# 
# ## Submitting your Project 
# 
# > **Tip**: Before you submit your project, you need to create a .html or .pdf version of this notebook in the workspace here. To do that, run the code cell below. If it worked correctly, you should get a return code of 0, and you should see the generated .html file in the workspace directory (click on the orange Jupyter icon in the upper left).
# 
# > **Tip**: Alternatively, you can download this report as .html via the **File** > **Download as** submenu, and then manually upload it into the workspace directory by clicking on the orange Jupyter icon in the upper left, then using the Upload button.
# 
# > **Tip**: Once you've done this, you can submit your project by clicking on the "Submit Project" button in the lower right here. This will create and submit a zip file with this .ipynb doc and the .html or .pdf version you created. Congratulations!

# In[63]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

