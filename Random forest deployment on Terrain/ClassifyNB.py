def classify(features_train, labels_train):   
  ### import the sklearn module for GaussianNB
  ### create classifier
  ### fit the classifier on the training features and labels
  ### return the fit classifier
  
      
  ### your code goes here!
  from sklearn.ensemble import RandomForestClassifier 
  clf = RandomForestClassifier(n_estimators = 10)  
  classifier = clf.fit(features_train, labels_train)
  print classifier
  return classifier
    

