# dict.py
#
# This file is the basis for an Artificial Intelligence system for
# guessing words in hangman. It can, within the standard eleven
# guesses, guess the word "oxymoron", which is the most difficult word
# I have found to try it against.
#
# Copyright (c) 2012 by Christopher J. Wald
#
# Usage:
#    dict.py <dictionary file> <word length> [-e chars to disallow from words] [-i chars to require in words]
#
# The dictionary file and word length are required.
# The dictionary file must be formatted as all lower case, \n
#    seperated words.
# Chars to disallow and require are optional and should be modified as
#    the game is played to reflect new knowledge about the word.
# For the -i argument, repeating chars the number of times they appear
# in the word greatly increases accuracy.
#
# Tested on Python 2.6.2 and 3.2.2 but should work on other versions
# with only minor text formatting differences.
#
# Version 0.4b

import sys

def checked_occurances_match(string, line):
    characters = 'abcdefghijklmnopqrstuvwxyz'

    count_string = 26*[0]
    for s in string:
        count_string[ord(s) - ord('a')] += 1

    count_line = 26*[0]
    for l in line:
        if ord('a') <= ord(l) <= ord('z'):
            count_line[ord(l) - ord('a')] += 1

    for i in range(len(count_string)):
        if count_string[i] != 0 and count_string[i] != count_line[i]:
            return False

    return True



words_file = open(sys.argv[1], 'r')
lines = words_file.readlines()[:-1]
words_file.close()
chars = int(sys.argv[2])
characters = 'abcdefghijklmnopqrstuvwxyz'
exclude = ''
include = characters

if len(sys.argv) > 3:
    if '-e' in sys.argv:
        exclude = sys.argv[sys.argv.index('-e') + 1]
    if '-i' in sys.argv:
        include = sys.argv[sys.argv.index('-i') + 1]

# Remove trailing \n
for i in range(len(lines)):
    lines[i] = lines[i][:-1]

# Remove all words not the right length
sys.stdout.write('Resize...')
sys.stdout.flush()
tmp = []
for line in lines:
    if len(line) == chars:
        tmp.append(line)
lines = tmp
sys.stdout.write('Done\n')
sys.stdout.flush()


# Remove words with excluded letters
if len(exclude) > 0:
    sys.stdout.write('Excludes...')
    sys.stdout.flush()
    tmp = []
    for line in lines:
        includable = True
        for e in exclude:
            if e.lower() in line or e.upper() in line:
                includable = False
                break
        if includable:
            tmp.append(line)
    lines = tmp
    del tmp
    sys.stdout.write('Done\n')
    sys.stdout.flush()

# Remove words without included letters
if len(include) < len(characters):
    sys.stdout.write('Includes...')
    sys.stdout.flush()
    tmp = []
    for line in lines:
        if checked_occurances_match(include, line):
            tmp.append(line)
    lines = tmp
    del tmp
    sys.stdout.write('Done\n')
    sys.stdout.flush()

# Remove all include letters from characters
# We don't need to check those
    tmp = ''
    for c in characters:
        if not c in include:
            tmp += c
    characters = tmp

# How many words do we have left?
print('Number of words: ' + str(len(lines)))

if len(lines) <= 10:
    for line in lines:
        print(line)

# Find out how many words each letter is in
counts = 26*[0]
for line in lines:
    for c in characters:
        if c.lower() in line or c.upper() in line:
            counts[ord(c) - ord('a')] += 1

lines = []

# Format the list
for i in range(len(counts)):
    lines.append(chr(ord('A') + i) + ': ' + str(counts[i]))
    
# Sort the list
top_index = len(lines) - 1
for i in range(len(lines)):
    for j in range(top_index):
        toks0 = lines[j].split()
        toks1 = lines[j+1].split()
        if int(toks0[1]) < int(toks1[1]):
            tmp = lines[j]
            lines[j] = lines[j+1]
            lines[j+1] = tmp
    top_index -= 1

# Print the list
for line in lines:
    if int(line.split()[1]) != 0:
        print(line)
