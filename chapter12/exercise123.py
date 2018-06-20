#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 12.3
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "metathesis_pairs" should find all of the metathesis pairs in 
# the dictionary and return them in a list of tuples. 
#
# 1. Two words form a "metathesis pair" if you can transform one into the other 
# by swapping two letters; for example, "converse" and "conserve". Write a 
# function named "metathesis_pairs" that takes in "words.txt" and finds all 
# of the metathesis pairs in the dictionary and returns them in a list of tuples. 
#
# Hint: don't test all pairs of words, and don't test all possible swaps. You
# may use the file anagram_sets.py which is the answer to the book problem 12.2
# or the code from 12.2 that we went over in class.
#
#if sort letters equal

import anagram_sets


def metathesis_pairs(file):
    d = anagram_sets.all_anagrams(file)
    li = []
    for anagrams in d.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1, word2) == 2:
                    li.append((word1,word2))
    return li


def word_distance(word1, word2):
    assert len(word1) == len(word2)

    count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            count += 1
    return count
    