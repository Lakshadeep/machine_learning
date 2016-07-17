def classify(features_train, labels_train):   
  ### import the sklearn module for GaussianNB
  ### create classifier
  ### fit the classifier on the training features and labels
  ### return the fit classifier
  
      
  ### your code goes here!
  from sklearn import neighbors
  n_neighbors = 20
  clf = neighbors.KNeighborsClassifier(n_neighbors, weights = 'distance')  
  # The default value, weights = 'uniform', assigns uniform weights to each neighbor. 
  #weights = 'distance' assigns weights proportional to the inverse of the distance 
  #from the query point.
  classifier = clf.fit(features_train, labels_train)
  print classifier
  return classifier
    

