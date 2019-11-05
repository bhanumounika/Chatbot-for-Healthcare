# -*- coding: utf-8 -*-
"""
Created on Sun 6th Oct 2019

@author: Geethika Joshi
         P Bhanu Mounika
"""
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import nltk 
from nltk.corpus import stopwords 
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import random
import mysql.connector
import sqlite3
import trying_matching as tm
class mdict(dict):

    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)
def tokenize_sentence(question):
    return sent_tokenize(question)

def tokenize_words(question):
    return word_tokenize(question)

def remove_punctuation(question):
    
    tokens = [t for t in question.split()] 
    clean_tokens=tokens[:]
    for token in tokens:
        if token in stopwords.words('english'):
             clean_tokens.remove(token)
    string_of_words=""
    for words in clean_tokens:
        string_of_words=string_of_words+' '+words
    return string_of_words

def get_synonyms(question):
    words=tokenize_words(question) 
    synonyms=mdict();
    for word in words:
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms[word]=lemma.name()
                  
    return synonyms
#def generate_sentence_from_question(synonyms):
#    list1=list(synonyms.keys())
#    length1=len(list1)
#    list3=[""]
#    str1=""
#    for word  in list1:
#           list2=list(synonyms[word])
#           i=0
#           for word2 in list2:
#               str1=list3[i]+word2+" "
#               list3[i]=str1
#               i=i+1
#    print(list3)
#    sentences=[""]
#    for word in list1:
#        for word1 in synonyms.values(word):
#            print(word1)    

def sentence_lemmmantizer(question):
    lemmer = nltk.stem.WordNetLemmatizer()
    tokens=tokenize_words(question)
    
    str1=""
    wording=""
    for tok in tokens:
        wording=lemmer.lemmatize(tok)
        str1=str1+' '+wording
        
    return(str1)
    
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "hi there", "hello", "I am glad! You are talking to me"]
def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def save_responses_to_database(question,answer):
    
    insert_stmt = ("INSERT INTO work (question,answer) " "VALUES (%s, %s)")
    data=(question,answer)
    connection=mysql.connector.connect(host="localhost",database="test")
    cursor=connection.cursor()
    
    cursor.execute(insert_stmt,data)
    connection.commit()
    connection.close()
    return
    
def find_most_favourable_answer(question):
    itemming=dict()
    itemming1=dict()
    most_favourable_item_id=0
    insert_stmt = ("select question,id from work")
    connection=mysql.connector.connect(host="localhost",database="test")
    cursor=connection.cursor()
    cursor.execute(insert_stmt)
    question_list=cursor.fetchall()
    for row in question_list:
        itemming1[row[0]]=row[1]
    
    
    connection.close()
    string=""
    for list1 in question_list:
        string=str(list1[0])
        
        
        ratio=tm.is_ci_lemma_stopword_set_match(question,string)
        itemming[string]=float(ratio)
    list_of_keys=itemming.keys()
    most_favourable_item=0.0
    for name1 in list_of_keys:
        if(most_favourable_item<=float(itemming[name1])):
            most_favourable_item=float(itemming[name1])
            most_favourable_item_name=name1
   
    for list2 in question_list:
        if(most_favourable_item_name==list2[0]):
            if(most_favourable_item>10.0 and most_favourable_item<=100.0):
                most_favourable_item_id=int(list2[1])
            else:
                most_favourable_item_id=0
            
    
    return most_favourable_item_id
    
def finding_answer(most_favourable_item_id):
    connection=mysql.connector.connect(host="localhost",database="test")
    cursor=connection.cursor()
    insert_stmt = ()
    cursor.execute("select answer from work where id = %s"% (most_favourable_item_id))
    answer=cursor.fetchone()
    for ans in answer:
        correct_ans=str(ans)
    connection.close()
    return correct_ans
        
    
    