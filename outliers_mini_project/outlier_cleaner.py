#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
  """
      Clean away the 10% of points that have the largest
      residual errors (difference between the prediction
      and the actual net worth).

      Return a list of tuples named cleaned_data where 
      each tuple is of the form (age, net_worth, error).
  """
  
  cleaned_data = []
  temp = []

  print predictions[0][0]

  ### your code goes here
  for i in range(0,len(predictions)):
    error = net_worths[i][0] - predictions[i][0]
    temp.append([ages[i][0], net_worths[i][0], error])

  temp.sort(key = lambda x: x[2], reverse = True)

  top_ninty = int(len(predictions) * 0.9)
  cleaned_data = temp[0:top_ninty]

  return cleaned_data

