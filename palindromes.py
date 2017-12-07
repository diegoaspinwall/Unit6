#Diego Aspinwall
#12-7-17
#palindromes.py

dictionary = open('engmix.txt')

diclist = []

for word in dictionary:
    diclist.append(word.strip())

for word in dictionary:
    if word == word.reverse():
        print(word)
