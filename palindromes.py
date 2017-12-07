#Diego Aspinwall
#12-7-17
#palindromes.py

dictionary = open('engmix.txt')

for word in dictionary:
    total = 0
    word = word.strip()
    for i in range(0,len(word)):
        if word[i] == word[i*(-1)-1]:
            total += 1
    if total == len(word):
        print(word)
