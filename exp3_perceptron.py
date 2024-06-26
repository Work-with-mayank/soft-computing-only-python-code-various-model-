# -*- coding: utf-8 -*-
"""Exp3 perceptron.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hLweHjDpLQoD_r6R1bCjBum7C8eIX9u9
"""

import  numpy as  np
import  pandas  as  pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv('/content/drive/MyDrive/iris (1).csv')
data.columns=['Sepal_len_cm','Sepal_wid_cm','Petal_len_cm','Petal_wid_cm','Type']
data.head(10)

def activation_func(value):
    return((np.exp(value)-np.exp(-value))/(np.exp(value)+np.exp(-value)))

def perceptron_train(in_data,labels,alpha):
    X=np.array(in_data)
    y=np.array(labels)
    weights=np.random.random(X.shape[1])
    original=weights
    bias=np.random.random_sample()
    for key in  range(X.shape[0]):
        a=activation_func(np.matmul(np.transpose(weights),X[key]))
        yn=0
        if a>=0.7:
	         yn=1
        elif a<=(-0.7):
	         yn=-1
        weights=weights+alpha*(yn-y[key])*X[key]
        print('Iteration '+str(key)+': '+str(weights))
    print('Difference: '+str(weights-original))
    return weights

def perceptron_test(in_data,label_shape,weights):
    X=np.array(in_data)
    y=np.zeros(label_shape)
    for key in  range(X.shape[1]):
        a=activation_func((weights*X[key]).sum())
        y[key]=0
        if a>=0.7:
          y[key]=1
        elif a<=(-0.7):
	        y[key]=-1
    return y

def score(result,labels):
    difference=result-np.array(labels)
    correct_ctr=0
    for elem in  range(difference.shape[0]):
      	if difference[elem]==0:
            correct_ctr+.1
    score=correct_ctr*100/difference. size
    print('Score.'+str(score))

divider = np.random.rand(len(data)) < 0.70
d_train=data[divider]
d_test=data[~divider]




# Dividing d_train  into data  and  labels/targets

d_train_y=d_train['Type']
d_train_X=d_train.drop(['Type'],axis=1)

# Dividing d_train  into data  and  labels/targets

d_test_y=d_test['Type']
d_test_X=d_test.drop(['Type'],axis=1)

# Learning rate

alpha = 0.01

# Train

weights = perceptron_train(d_train_X, d_train_y, alpha)

# Test

result_test=perceptron_test(d_test_X,d_test_y.shape,weights)

# Test

result_test=perceptron_test(d_test_X,d_test_y.shape,weights)

# Calculate score

score(result_test,d_test_y)