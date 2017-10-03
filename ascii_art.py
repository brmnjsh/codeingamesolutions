import sys
import math

# ASCII Art
# https://www.codingame.com/ide/puzzle/ascii-art

l = int(input())
h = int(input())
t = input()
letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','?']
letter_map = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[],'I':[],'J':[],'K':[],'L':[],'M':[],'N':[],'O':[],'P':[],'Q':[],'R':[],'S':[],'T':[],'U':[],'V':[],'W':[],'X':[],'Y':[],'Z':[],'?':[]}

for i in range(h):
    row = input()
    lengthCount = 0
    lettersCount = 0
    for r in row:
        letter_map[letters[lettersCount]].append(r)
        if lengthCount == l - 1:
            lengthCount = 0
            lettersCount = lettersCount + 1
        else:
            lengthCount = lengthCount + 1       
            
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
lengthCount = 0
word = ''
totalCount = 0

for i in range(h):
    word = ''
    for letter in t:
        wordCount = 0
        while wordCount < l:
            if letter.upper() not in letter_map:
                word = word + letter_map['?'][wordCount + totalCount]
            else:
                word = word + letter_map[letter.upper()][wordCount + totalCount]
            wordCount = wordCount + 1
    totalCount = totalCount + l
    print(word)