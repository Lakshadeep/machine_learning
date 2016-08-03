from sklearn.feature_extraction.text import CountVectorizer
vectoriser = CountVectorizer()
string1 = "I love  coldplay"
string2 = "Fix you is the best song by coldplay"
string_list = [string1, string2]
vectoriser.fit(string_list)
bag_of_words = vectoriser.transform(string_list) 
print bag_of_words

print vectoriser.vocabulary_.get("coldplay") #return the number assigned to given word

analyze = vectoriser.build_analyzer()  #displays the words sentence is splitted into
print analyze("I love  Coldplay")
print analyze("Fix you is the best song by Coldplay")