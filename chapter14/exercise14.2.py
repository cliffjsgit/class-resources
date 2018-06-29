#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 14.2
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "store_anagrams" should take in a dictionary file specified in 
# the arguments, pass it to the function in "anagram_sets" that will generate
# an anagram dictiontionary, and then write it to a shelve.
# - Function "read_anagrams" should take in a shelve file as well as a word
# and then returns a list of anagrams.
# 
# 1. If you download the solution to Exercise 12-2 from 
# http://thinkpython2.com/code/anagram_sets.py, you'll see that it creates a 
# dictionary that maps from a sorted string of letters to the list of words that
# can be spelled with those letters. For example, 'opst' maps to the list 
# ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
#
# Write a module that imports anagram_sets and provides two new functions: 
# store_anagrams should store the anagram dictionary in a "shelf"; read_anagrams
# should look up a word and return a list of its anagrams.
# 

import anagram_sets
import shelve

def store_anagrams(dictFile,shelveFile):
    anagram_dict = anagram_sets.all_anagrams(dictFile)
    with shelve.open(shelveFile) as db:
        db.update(anagram_dict)

def read_anagrams(shelveFile,word):
    with shelve.open(shelveFile) as db:
        return db[anagram_sets.signature(word)]

store_anagrams("words.txt","myShelve.db")
print(read_anagrams("myShelve.db","example"))