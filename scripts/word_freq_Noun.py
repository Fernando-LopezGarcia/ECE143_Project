#
# ECE 143 Group Project
# 
# Simple script that counts the occurance frequencies of 
# the words in a specific file.
#
# by Renjie Zhu on 10/24/2018
#
# modified: Daoyu, Ambareesh
# 

# be careful of the location of this file, if moved, be sure to rethink about the file paths

#import nltk
import os
import nltk
from collections import Counter


# parent dir for mac or linux 
parent_dir = os.getcwd()
# parent dir for windows machine (uncomment if on windows, leave commented if elsewise)
# parent_dir = os.path.dirname(parent_dir)
# os.path.join joins all the arguments given in the function call
file_data = os.path.join(parent_dir,'raw_data',input('What is the data file name? (Make sure the file is in "raw_data" folder, give file name with extension)'))
file_out = os.path.join(parent_dir,'processed_data',input('What is the output file name? (Make sure to provide the .txt/.csv extension) '))

# keeping track of a common words list, this is a list of words that we
# don't want in our data.
common_words = [
    '','hours of', 'of lecture','instructor','c-','consent of','consent', 'prerequisite ece','lecture prerequisite',
    'and', 'of instructor',
    'ece', 'prerequisites ece', 'lecture one','grades of','with grades',
    'of', 'three hours',
    'grading',
    'study',
    'outside',
    'four',
    'letter',
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
    'a',
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
]  #need better algo to remove common words, I think they should't be collected in the wordlist at all, can be removed with a condition in line 91, wordlist = 
common_words.extend(list(map(chr, range(97, 123))))

with open(file_data, 'r') as f:
    lines = f.read()

# Get rid of unwanted chars and splitting the string into a list of words
origlist = lines.lower().split()
wordlist = [i.strip(".:,();$-1234567890") for i in origlist]
# wordfreq = [wordlist.count(j) for j in wordlist]
# freqdict = dict(zip(wordlist, wordfreq))
freqdict = Counter(wordlist)
newfreq = {}
for key, value in freqdict.items():
    if value < 2:
        continue
    elif key in common_words:
        continue
    else:
        newfreq[key] = value
posFreq = nltk.pos_tag(list(newfreq.keys()))
#Convert the list created by nltk to dict
posDict = {word: pos for word, pos in posFreq}
nnfreq = {}
#Download nltk resources
nltk.download("wordnet")
lemmatizer = nltk.WordNetLemmatizer()
for key, value in newfreq.items(): 
    if posDict[key] == 'NN' or posDict[key] == 'NNS':
        key = lemmatizer.lemmatize(key)
        if key in nnfreq.keys():
            nnfreq[key] = nnfreq[key] + value
        else:
            nnfreq[key] = value
with open(file_out, 'w') as f:
    for key, value in reversed(sorted(nnfreq.items(), key=lambda x: x[1])):
        f.write(f'{key}: {value}\n')