#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
from feature_format import featureFormat, targetFeatureSplit
import numpy as np


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("final_project_dataset.pkl", "r") )

# data_dict.pop( "BELFER ROBERT", None )

features = ["salary", "bonus"]
data = featureFormat(data_dict, features, remove_any_zeroes=True)

target, features = targetFeatureSplit( data )

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(features, target)

# predictions = reg.predict(features)
# temp = []

# names =  data_dict.keys()

# for i in range(0,len(predictions)):
#   error = abs(target[i] - predictions[i])
#   # temp.append([names[i],error])
#   temp.append(error)

# # temp.sort(key = lambda x: abs(x[1]), reverse=True)

# a = np.array(temp)
# print a.max()
# print np.where( a == a.max())
# print names[24]

max_salary = 0
max_salary_key = None

for key in data_dict:
  if data_dict[key]["salary"] != 'NaN' and data_dict[key]["salary"] > max_salary:
    max_salary = data_dict[key]["salary"]
    max_salary_key = key

data_dict.pop(max_salary_key, 0)
print "Outlier key: " + max_salary_key

# Who made $6-8 mil bonus and over $1 mil salary
for key in data_dict:
  if data_dict[key]["salary"] != 'NaN' and data_dict[key]["bonus"] != 'NaN':
    if data_dict[key]["salary"] > 1.0e6 and data_dict[key]["bonus"] > 5.5e6:
      print key


### your code below
for point in data:
  salary = point[0]
  bonus = point[1]
  matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.plot( features, reg.predict(features) )
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



