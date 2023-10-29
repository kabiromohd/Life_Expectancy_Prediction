#!/usr/bin/env python
# coding: utf-8

# In[38]:


import pandas as pd
import numpy as np
import pickle

from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import mean_squared_error
from sklearn.tree import export_text
get_ipython().run_line_magic('matplotlib', 'inline')


df = pd.read_csv("train.csv")

# Remove space and convert to lower case for columns names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Dropping observations where the values are missing for the target variable
df.dropna(subset = ["life_expectancy"], inplace = True)


def prepare_data_split(df, test_size, random_state, target_feature):
    '''
    Fuunction Split a dataset(df) in the ratio 60%/20%/20% == Train/Validation/Test
    
    return the train, Validation and Test dataset with their corresponding targer variable
    '''
    df_full_train, df_test = train_test_split(df, test_size= test_size, random_state=random_state)
    df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=random_state)
    
    df_train = df_train.reset_index(drop=True)
    df_val = df_val.reset_index(drop=True)
    df_test = df_test.reset_index(drop=True)
    df_full_train = df_full_train.reset_index(drop=True)
    
    y_train = np.log1p(df_train[target_feature].values)
    y_val = np.log1p(df_val[target_feature].values)
    y_test = np.log1p(df_test[target_feature].values)
    y_full_train = np.log1p(df_full_train[target_feature].values)
    
    del df_train[target_feature]
    del df_val[target_feature]
    del df_test[target_feature]
    del df_full_train[target_feature]
    
    return df_train, y_train, df_val, y_val, df_test, y_test, df_full_train, y_full_train


# Setup Validation framework for logistic regression for dataset df_final
test_size = 0.2
random_state = 1
target = "life_expectancy"
df_train, y_train, df_val, y_val, df_test, y_test, df_full_train, y_full_train = prepare_data_split(df,
                                                                                                    test_size,
                                                                                                    random_state, 
                                                                                                    target)



train_dicts = df_train.fillna(0).to_dict(orient='records')

dv = DictVectorizer(sparse = False)
X_train = dv.fit_transform(train_dicts)

val_dicts = df_val.fillna(0).to_dict(orient='records')
X_val = dv.transform(val_dicts)

test_dicts = df_test.fillna(0).to_dict(orient='records')
X_test = dv.transform(test_dicts)

train_full_dicts = df_full_train.fillna(0).to_dict(orient='records')
X_full_train = dv.transform(train_full_dicts)


# Final Random forest model with full train
rf_final_full = RandomForestRegressor(n_estimators=375, random_state=1, max_depth = 20, n_jobs=-1)
rf_final_full.fit(X_full_train, y_full_train)

# Save your model as `"model_rf_1.pkl"`
with open("model_rf_1.pkl", "wb") as f:
    pickle.dump(rf_final_full, f)
    
with open("model_dv.pkl", "wb") as f:
    pickle.dump(dv, f)
