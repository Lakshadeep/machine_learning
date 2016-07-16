def classify(features_train, labels_train):   
  ### import the sklearn module for GaussianNB
  ### create classifier
  ### fit the classifier on the training features and labels
  ### return the fit classifier
  
      
  ### your code goes here!
  from sklearn import tree
  clf = tree.DecisionTreeClassifier(min_samples_leaf=20)
  classifier = clf.fit(features_train, labels_train)
  print classifier
  return classifier
    

