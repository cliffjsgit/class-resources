#!/usr/bin/env python3

__author__ = "Your Name"

###############################################################################
#
# Exercise 14.3
#
#
# Grading Guidelines:
# - No answer variable is needed. Grading script will call function.
# - Function "find_duplicates" should take a string reprensentation of a
# directory to search, find all the duplicates, and returns a list of complete 
# paths for any duplicates in the form of tuples.
# 
# In a large collection of MP3 files, there may be more than one copy of the 
# same song, stored in different directories or with different file names. The 
# goal of this exercise is to search for duplicates.
# 
# 1. Write a function named "find_duplicates" that takes a string 
# reprensentation of a directory to search, searches that directory and 
# all of its subdirectories, recursively, and returns a list of complete 
# paths for any duplicates in the form of tuples.
# 
# 2. To recognize duplicates, you can use md5sum to compute a "checksum" for 
# each files. If two files have the same checksum, they probably have the same 
# contents.
#

import os


def walk(dirname):
    names = []
    if '__pycache__' in dirname:
        return names

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    cmd = 'md5sum ' + filename
    return pipe(cmd)


def check_diff(name1, name2):
    cmd = 'diff %s %s' % (name1, name2)
    return pipe(cmd)


def pipe(cmd):
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum, _ = res.split()

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def find_duplicates(dirname):
    dlist = []
    d = compute_checksums(dirname, suffix='.mp3')
    for key, names in d.items():
        if len(names) > 1:
            rlist = []
            if check_pairs(names):
                for name in names:
                    rlist.append(name)
            dlist.append(tuple(rlist))
    return dlist
    
print(find_duplicates('mp3'))