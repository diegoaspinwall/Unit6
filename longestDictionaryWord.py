#Diego Aspinwall
#12-6-17
#longestDictionaryWord.py

dictionary = open('engmix.txt')
high = 'a'
for word in dictionary:
    l = 0
    for w in word:
        if l < len(w):
            l = len(w)
            high = w
print(high)
