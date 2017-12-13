#Diego Aspinwall
#12-13-17
#quiz6.py

#Program 1
dictionary = open('engmix.txt')

wordz = []

for word in dictionary:
    c=0
    p=0
    if 'c' in word:
        c+=1
    if 'p' in word:
        p+=1
    if c==3 and p==2:
        wordz.append(word.strip())

print(wordz)
