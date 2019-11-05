# -*- coding: utf-8 -*-
"""
Created on Sun 6th Oct 2019

@author: Geethika Joshi
         P Bhanu Mounika
"""

import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
from nltk.corpus import wordnet
import string
from nltk.tokenize import word_tokenize
import Codefile as cse
stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(string.punctuation)
stopwords.append('')

def get_wordnet_pos(pos_tag):
    if pos_tag[1].startswith('J'):
        return (pos_tag[0], wordnet.ADJ)
    elif pos_tag[1].startswith('V'):
        return (pos_tag[0], wordnet.VERB)
    elif pos_tag[1].startswith('N'):
        return (pos_tag[0], wordnet.NOUN)
    elif pos_tag[1].startswith('R'):
        return (pos_tag[0], wordnet.ADV)
    else:
        return (pos_tag[0], wordnet.NOUN)

# Create tokenizer and stemmer

lemmatizer =  nltk.stem.WordNetLemmatizer()

def is_ci_lemma_stopword_set_match(a, b, threshold=0.5):
    """Check if a and b are matches."""
    pos_a = map(get_wordnet_pos, nltk.pos_tag(word_tokenize(a)))
    pos_b = map(get_wordnet_pos, nltk.pos_tag(word_tokenize(b)))
    lemmae_a = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    lemmae_b = [lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_b \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    
   
    
    # Calculate Jaccard similarity
    if(float(len(set(lemmae_a).union(lemmae_b)))!=0):
        ratio = len(set(lemmae_a).intersection(lemmae_b)) / float(len(set(lemmae_a).union(lemmae_b)))
    else:
        ratio=0.0
    
    return ratio*100
