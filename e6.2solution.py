#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:58:29 2018

@author: Samuel_Clarin
"""
import pandas as pd
iris=pd.read_csv('iris.csv', header=0, sep=',')
#print last 2 rows and last 2 columns




last=iris.iloc[148:150,3:5]
print last


#get number of observations for each species

iris['Species'].value_counts()


#get rows with Sepal width > 3.5

iris[iris['Sepal.Width']>3.5]


#write the data for the species 'setosa' into a file 'setosa.csv'

setosa=iris[iris.Species.str.contains('setosa')]
f= open("setosa.csv","w+")
setosa.to_csv('setosa.csv')

#calculate the mean, minimum and maximum of Petal.length for virginica

virginica = iris [iris.Species.str.contains('virginica')]
virginica['Petal.Length'].mean()
virginica['Petal.Length'].min()
virginica['Petal.Length'].max()
    
    
