#Diego Aspinwall
#12-7-17
#palindromes.py

dictionary = open('engmix.txt')

for word in dictionary:
    for i in len(word):
        if word[i] == word[i*(-1)-1]:
            
    print(word)
