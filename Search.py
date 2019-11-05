# -*- coding: utf-8 -*-
"""
Created on Sun 6th Oct 2019

@author: Geethika Joshi
         P Bhanu Mounika
"""

import string
import nltk
from nltk.corpus import wordnet
import re
import string
import sqlite3
from collections import Counter
from string import punctuation
from math import sqrt
import Codefile as cs

import mysql.connector

class mdict(dict):
    def __setitem__(self, key, value):
        """add the given value to the list of values for this key"""
        self.setdefault(key, []).append(value)


def start():
    flag=True;
    question=""
    
    answer_of_query=""
    while(flag==True):
        question=input("User Query:")
        question=question.strip()
        question=question.lower()
        if(question!="bye" and cs.greeting(question)==None and question!="exit"):
#            punctuation_removed_question=cs.remove_punctuation(question)
            most_favourable_item_id=int(cs.find_most_favourable_answer(question))
            if(most_favourable_item_id!=0):
                answer_of_query=cs.finding_answer(most_favourable_item_id)
                print("DOCTOR-BOT: "+answer_of_query)
            else:
                print("DOCTOR-BOT: Unable to Find the answer, will get back to you soon")
        else:
            if(cs.greeting(question)!=None):
                print("DOCTOR-BOT: "+cs.greeting(question))
            else:
                print("DOCTOR-BOT: bye, Take care")
                flag=False