#Diego Aspinwall
#12-6-17
#zzwords.py

dictionary = open('engmix.txt')

for word in dictionary:
    if 'max' in word:
        print(word.strip())
