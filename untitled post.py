# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:42:43 2024

@author: Joshu


import pandas as pd
 
file= pd.read_csv('country_data.csv')

print(file)



age = [30, 25, 29, 46, 22]

#print (age)

#print(age[0])

#print(age[1])

#print(len(age))
'''
average = sum(age)/len(age)
average
'''

#age.append(100)
#print(age)

#print(age[0:3])

"""
'''
# giving names to data

#names = ["A", "B", "C"]
#file = pandas.read_csv("housing data.csv")

#Adding a specific number to vector 
age = [30, 25, 29, 46, 22]

age.insert(0,100)

print(age)

'''

#How to create dictionaries

mammals ={"cat": " a cute animal", "lion":"king of the jungle", "elephant":"a gigantic herbivore"}
print (mammals["cat"])


# Creating dataframes

fruits = ["appple", "banna","orange","grape", "kiwi"]
Size_nm = [9.8, 10.1, 13.3, 8.7, 20.5]

fruit_sizes= { 'fruits': fruits,
               'size':Size_nm
               
               }

import pandas as pd 

df=pd.DataFrame(fruit_sizes)

#accessing a specific dataframe
print(df['fruits'])

print (df['size'])
print(df["size"].min())
print(df["size"].max())
print(df[df['size']>10])

print(df[1:3])

prices = [ 10.00, 12.50, 16.00, 23.00, 7.00]
df['prices'] = prices

df.drop(columns=['size'], inplace=True)






