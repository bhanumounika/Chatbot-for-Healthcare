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

def train_system():
    flag=True;
    question=""
    answer=""
    while(flag==True):
        question=input("Admin Question:")
        question=question.strip()
        question=question.lower()
        if(question!="" and question!="bye" and question!="exit"):
            answer=input("Admin Answer:")
            answer=answer.strip()
#            punctuation_removed_question=cs.remove_punctuation(question)
#            cs.get_synonyms(punctuation_removed_question)
#            synonyms=mdict()
#            synonyms=cs.get_synonyms(punctuation_removed_question)
#            cs.generate_sentence_from_question(synonyms)
#            lemmantized_question=cs.sentence_lemmmantizer(punctuation_removed_question)
            cs.save_responses_to_database(question,answer)
            print("Responses saved successfully")
            
        else:
            print("DOCTOR-BOT: Wrong Responses Sir")
            return