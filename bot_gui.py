# In[19]:

import sys
from os import path
import nltk
# nltk.download('punkt')
# nltk.download('wordnet')


# In[20]:


from nltk.stem import WordNetLemmatizer
lemmitizer = WordNetLemmatizer()


# In[21]:


import pickle


# In[22]:


import numpy as np


# In[23]:


from tensorflow.keras.models import load_model


# In[24]:


bundle_dir =getattr(sys,"_MEIPASS",path.abspath(path.dirname(__file__)))

path_to_model =path.join(bundle_dir,"data","chatbot_model.h5")
model = load_model(path_to_model)


# In[25]:


import json


# In[26]:


import random


# In[27]:


import pandas as pd


# In[28]:

path_to_data =path.join(bundle_dir,"data","new_dataset.json")
data = pd.read_json(path_to_data)
path_to_words =path.join(bundle_dir,"data","words.pkl")
words = pickle.load(open(path_to_words,'rb'))
path_to_classes =path.join(bundle_dir,"data","classes.pkl")
classes = pickle.load(open(path_to_classes,'rb'))


# In[29]:


def clean_up_sentence(sentence):
    # tokenize the pattern - splitting words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stemming every word - reducing to base form
    sentence_words = [lemmitizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# In[30]:


# return bag of words array: 0 or 1 for words that exist in sentence
def bag_of_words(sentence, words, show_details=True):
    # tokenizing patterns
    sentence_words = clean_up_sentence(sentence)
    # bag of words - vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,word in enumerate(words):
            if word == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % word)
    return(np.array(bag))


# In[31]:


def predict_class(sentence):
    # filter below  threshold predictions
    p = bag_of_words(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sorting strength probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


# In[32]:


def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = (i['answer'])
            break
    return result


# In[33]:


def chat_bot(msg):
    msg =msg.strip()
    person = "You : "+msg
    ints = predict_class(msg)
    res = getResponse(ints, data)
    bot ='bot : '+res+'\n\n' 
    results=[person,bot]
    return results


# In[34]:


"""
while True:
    msg = input('You : ').strip()
    if(msg.lower() != "exit"):
        ans = chat_bot(msg)
        print(ans[0])
        print(ans[1])
    else:
        break
"""        


# In[ ]:




