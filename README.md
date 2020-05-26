# TF-IDF-weighing
Python Search Engine over presidential debates using tf-idf weighing
## getidf(token): 
return the inverse document frequency of a token. If the token doesn't exist in the corpus, return -1. The parameter 'token' is already stemmed. (It means you should not perform stemming inside this function.) Note the differences between getidf("hispan") and getidf("hispanic"). 
## getweight(filename,token): 
return the TF-IDF weight of a token in the document named 'filename'. If the token doesn't exist in the document, return 0. The parameter 'token' is already stemmed. (It means you should not perform stemming inside this function.) Note that both getweight("1960-10-21.txt","reason") and getweight("2012-10-16.txt","hispanic") return 0, but for different reasons. 
## query(qstring): 
return a tuple in the form of (filename of the document, score), where the document is the query answer with respect to "qstring" . If no document contains any token in the query, return ("None",0). If we need more than 10 elements from each posting list, return ("fetch more",0).
