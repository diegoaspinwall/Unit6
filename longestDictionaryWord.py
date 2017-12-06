#Diego Aspinwall
#12-6-17
#longestDictionaryWord.py

dictionary = open('engmix.txt')

highword = 'a'
highnum = 0
for word in dictionary:
    if highnum < len(word):
        highnum = len(word)
        highword = word
print(highword)
