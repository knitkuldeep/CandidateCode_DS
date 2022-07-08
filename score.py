#!/usr/bin/env python
# coding: utf-8

# In[1]:


from locale import normalize
import pandas as pd
import numpy as np
import sys


# In[5]:


def mape(actuals, preds):
    return np.mean(np.abs((actuals - preds)) / actuals) * 100

def score(actual_data,sub_data):
    if actual_data.shape!=sub_data.shape:
        return('Shape Mismatch')
    if actual_data.columns.tolist()!=sub_data.columns.tolist():
        return('Columns Mismatch')
    
    actuals=actual_data['salary'].tolist()
    preds=sub_data['salary'].tolist()
    

    try:
        score = mape(np.array(actuals), np.array(preds))
        if score > 100:
            score = 100
        return score
    except Exception as e:
        print(e)
        return "Error in Evaluation"

def normalize_score(score):
    return (100 - score)

# In[6]:


def read_data(actual_file,submission_file):
    try:
        actual_data=pd.read_csv(actual_file)
        sub_data=pd.read_csv(submission_file)
        
        return actual_data,sub_data
    except:
        print('File Not Found')
        


# In[7]:


try:
    actual_data,submission_data=read_data(sys.argv[1],sys.argv[2])
    score=score(actual_data,submission_data)
    normalize_score = normalize_score(score)     # if normalized score is same as score, set normalized_score = score
    print(score)
    print(normalize_score)

except Exception as e:
    print(e)
    print('Score could not be calculated')

# In[ ]:




