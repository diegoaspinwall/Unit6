#Diego Aspinwall
#12-7-17
#longShort.py

alphabet = 'abcdefghijklmnopqrstuvwxyz'

longest = ['']*26
shortest = ['']*26

dictionary = open('engmix.txt')

for word in dictionary:
    alphabet.index(word[0])
    

print(alphabet.index('b'))