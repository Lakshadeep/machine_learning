def classify(features_train, labels_train):   
  ### import the sklearn module for GaussianNB
  ### create classifier
  ### fit the classifier on the training features and labels
  ### return the fit classifier
  
      
  ### your code goes here!
  # from sklearn import tree
  from sklearn.ensemble import AdaBoostClassifier
  from sklearn.tree import DecisionTreeClassifier
  clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200)
  classifier = clf.fit(features_train, labels_train)
  print classifier
  return classifier
    

