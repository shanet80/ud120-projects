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

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of persons in dataset: {}".format(len(enron_data))

print "Number of features per person in dataset: {}".format(set(len(v) for v in enron_data.values()))

poi = 0
for person in enron_data:
    if enron_data[person]["poi"] == 1:
        poi += 1
print "Number of persons of interest in dataset: {}".format(poi)

print "Total stock value for James Prentice: {}".format(enron_data['PRENTICE JAMES']['total_stock_value'])

print "Total emailed from Wesley Colwell to persons of interest: {}".format(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])

print "Exercised stock opertions for Jeffrey Skilling: {}".format(enron_data['SKILLING JEFFREY K'] ['exercised_stock_options'])

print "Total payments to Ken Lay: {}".format(enron_data['LAY KENNETH L']['total_payments'])

print "Total payments to Andrew Fastow: {}".format(enron_data['FASTOW ANDREW S']['total_payments'])

print "Total payments to Jeffrey Skilling: {}".format(enron_data['SKILLING JEFFREY K']['total_payments'])

salary = 0
for x in enron_data.values():
    if x['salary'] != 'NaN':
        salary += 1

print "Number of persons with salary in dataset salary {}".format(salary)

email = 0
for x in enron_data.values():
    if x['email_address'] != 'NaN':
        email += 1

print "Number of persons with salary information: {}".format(email)

missing_payments = 0
for x in enron_data.values():
    if x['total_payments'] == 'NaN':
        missing_payments += 1

print "Percentage of people missing total payments : {}".format(missing_payments / 146.0)
 
poi_array = []
for x in enron_data.values():
    if x['poi'] == True:
        poi_array.append(x)
        
poi_missing_payments = 0
for x in poi_array:
    if x['total_payments'] =='NaN':
        poi_missing_payments += 1
        
print "Percentage of Pois missing total payments: {}".format(poi_missing_payments / len(poi_array))