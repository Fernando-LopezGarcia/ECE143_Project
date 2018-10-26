#
# ECE 143 Group Project
# 
# Simple script that counts the occurance frequencies of 
# the words in a specific file. (UNIX Ver)
#
# by Renjie Zhu on 10/24/2018
#
# modified: Daoyu, Ambareesh
# 

# be careful of the location of this file, if moved, be sure to rethink about the file paths
# this is for unix (RZ)
from pathlib import Path

parent_dir = str(Path().resolve().parent)
file_data = parent_dir + '/raw_data/' + input('What is the data file name? (make sure it is in the "raw_data" folder)')
file_out = parent_dir + '/processed_data/' + input('What is the output file name? ') + '.txt'

# keeping track of a common words list, this is a list of words that we
# don't want in our data.
common_words = [
    '',
    'and',
    'ece',
    'of',
    'prerequisites',
    'prerequisite',
    'hours',
    'lecture',
    'three',
    'one',
    'discussion',
    'hour',
    'in',
    'or',
    'the',
    'to',
    'for',
    'graduate',
    'standing',
    'with',
    'will',
    'be',
    'course',
    'topics',
    'may',
    'on',
    'students',
    'better',
    'at',
    'credit',
    'not',
    'by',
    'taken',
    'grade',
    'is',
    'are',
    'ii',
    'recommended',
    'c-',
    'c–',
    'an',
    'and/or',
    'equivalent',
    'this',
    'both',
    'from',
    'only',
    'faculty',
    's/u',
    'which',
    'than',
    'weekly',
    'have',
]
common_words.extend(list(map(chr, range(97, 123))))

with open(file_data, 'r') as f:
    lines = f.read()

# Get rid of unwanted chars and splitting the string into a list of words
origlist = lines.lower().split()
wordlist = [i.strip(".:,();$-1234567890") for i in origlist]
wordfreq = [wordlist.count(j) for j in wordlist]
freqdict = dict(zip(wordlist, wordfreq))

newfreq = {}
for key, value in freqdict.items():
    if value < 2:
        continue
    elif key in common_words:
        continue
    else:
        newfreq[key] = value

with open(file_out, 'w') as f:
    for key, value in reversed(sorted(newfreq.items(), key=lambda x: x[1])):
        f.write(f'{key}: {value}\n')
