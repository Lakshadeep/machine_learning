def classify(features_train, labels_train):   
  ### import the sklearn module for GaussianNB
  ### create classifier
  ### fit the classifier on the training features and labels
  ### return the fit classifier
  
      
  ### your code goes here!
  from sklearn.svm import SVC
  clf = SVC(kernel='rbf', C = 1000)   # greater the value of c better the accuaracy
  classifier = clf.fit(features_train, labels_train)
  print classifier
  return classifier
    

