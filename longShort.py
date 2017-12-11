#Diego Aspinwall
#12-7-17
#longShort.py

alphabet = 'abcdefghijklmnopqrstuvwxyz'

longest = ['']*26
shortest = ['']*26

dictionary = open('engmix.txt')

for word in dictionary:
    word = word.strip
    if word != '':
        if len(word) > len(longest[alphabet.index(word[0])]):
            longest[alphabet.index(word[0])] = word
        if len(word) < len(shortest[alphabet.index(word[0])]):
            shortest[alphabet.index(word[0])] = word

for i in range(0,26):
    print(shortest[i])
    print(longest[i])
    print('')
