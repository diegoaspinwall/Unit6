#Diego Aspinwall
#12-6-17
#longestDictionaryWord.py

dictionary = open('engmix.txt')

highword = 'a'
for word in dictionary:
    highnum = 0
    if highnum < len(word):
        highnum = len(word)
        highword = word
print(highword)
