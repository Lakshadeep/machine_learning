#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("final_project_dataset.pkl", "r"))

print "Answer 1: " + str(enron_data["PRENTICE JAMES"]["total_stock_value"])


print "Answer 2: " + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

print "Answer 3: " + str(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])

print "Lay (total payments): " + str(enron_data["LAY KENNETH L"]["total_payments"])
print "Skilling (total payments): " + str(enron_data["SKILLING JEFFREY K"]["total_payments"])
print "Fastow (total payments): " + str(enron_data["FASTOW ANDREW S"]["total_payments"])

# for i in range(0,len(enron_data)):
# 	print enron_data[i]["salary"]

print enron_data[""]["salary"]
