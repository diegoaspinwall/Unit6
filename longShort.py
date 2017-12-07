#Diego Aspinwall
#12-7-17
#longShort.py

alphabet = 'abcdefghijklmnopqrstuvwxyz'

dictionary = open('engmix.txt')

for word in dictionary:
    alphabet.index(word[0])
