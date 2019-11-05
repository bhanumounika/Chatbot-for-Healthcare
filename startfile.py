# -*- coding: utf-8 -*-
"""
Created on Sun 6th Oct 2019

@author: Geethika Joshi
         P Bhanu Mounika
"""
import string
import nltk
nltk.download()
from nltk.corpus import wordnet
import re
import string
import sqlite3
from collections import Counter
from string import punctuation
from math import sqrt
import Codefile as cs
import Training_system as ty
import Search as sc
import mysql.connector
connection=mysql.connector.connect(host="localhost",database="test")
cursor=connection.cursor()
cursor.execute("create table IF NOT EXISTS work(question VARCHAR(1000) NOT NULL,answer VARCHAR(1000) NOT NULL,id int auto_increment primary key)")
connection.commit();
connection.close();

print("Hello User I'm DOCTOR-BOT Your chatbot")
class mdict(dict):
    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)



            
            
if __name__=="__main__":
         
   
    valid_response=""
    while True:
    
        print("Do you want to train or search")
        valid_response=input("User:")
        valid_response=valid_response.strip()
        valid_response=valid_response.lower()
        
        if(valid_response=="train"):
            ty.train_system()
        else:
            if(valid_response=="search"):
                sc.start()
            else:
                if(cs.greeting(valid_response)!=None):
                   print("DOCTOR-BOT: "+cs.greeting(valid_response))
                else:
                    print("DOCTOR-BOT: Bye")
                    break
    
    
                    