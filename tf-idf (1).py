#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Siddharth Vadgama
#1001397508
"""
Library setup
"""
import os
import math
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from collections import Counter
"""
Opening files and tokenizing. 
"""
stemmer = PorterStemmer()
corpusroot = './presidential_debates'
stop_words=stopwords.words('english')
term_freq={}
total_doc=0
docu_freq=Counter()
"""
Function to generate getidf
"""
def getidf(token):
    if docu_freq[token] != 0:
        return math.log10(len(term_freq)/docu_freq[token])
    else:
        return -1
    
def getweight_helper(filename,token):
    return (1+math.log10(term_freq[filename][token]))*getidf(token)
"""
Stemming, tokenizing and calculation TF and DF values.

"""
for filename in os.listdir(corpusroot):
    file = open(os.path.join(corpusroot, filename), "r", encoding='UTF-8')
    doc = file.read()
    file.close() 
    doc = doc.lower()
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    tokens = tokenizer.tokenize(doc)
    #tokens = list(set(tokens)-set(stop_words))
    tokens = [stemmer.stem(x) for x in tokens if x not in stop_words]
    docu_freq=docu_freq+Counter(list(set(tokens)))
    term_freq[filename]=Counter(tokens)
    total_doc+=1
postings_list={} 
weights_vec={}
for d in term_freq:
    weights_single_docu=Counter()
    for t in term_freq[d]:
        weights_single_docu[t]=getweight_helper(d,t)
    weights_vec[d]=norm(weights_single_docu)

for d in weights_vec:
    for t in weights_vec[d]:
        if t not in postings_list:
            postings_list[t]=Counter()
        postings_list[t][d]=weights_vec[d][t]
def getweight(filename,token):
    return weights_vec[filename][token]
def norm(vec1):
    norm_vec={}
    sum_t=0
    for i in vec1:
        sum_t+=vec1[i]**2
    sum_sq=math.sqrt(sum_t)
    for i in vec1:
        norm_vec[i]=vec1[i]/sum_sq
    return norm_vec


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


postings_list={} 
weights_vec={}
for d in term_freq:
    weights_single_docu=Counter()
    for t in term_freq[d]:
        weights_single_docu[t]=getweight_helper(d,t)
    weights_vec[d]=norm(weights_single_docu)

for d in weights_vec:
    for t in weights_vec[d]:
        if t not in postings_list:
            postings_list[t]=Counter()
        postings_list[t][d]=weights_vec[d][t]


# In[ ]:


def getweight(filename,token):
    return weights_vec[filename][token]


# In[ ]:


def norm(vec1):
    norm_vec={}
    sum_t=0
    for i in vec1:
        sum_t+=vec1[i]**2
    sum_sq=math.sqrt(sum_t)
    for i in vec1:
        norm_vec[i]=vec1[i]/sum_sq
    return norm_vec


# In[ ]:





# In[ ]:


postings_list['barack']


# In[ ]:


def query(string):
    tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
    tokens = tokenizer.tokenize(doc)
    tokens = [stemmer.stem(x) for x in tokens if x not in stop_words]
    

