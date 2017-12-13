#Diego Aspinwall
#12-13-17
#quiz6.py

#Program 1
'''
dictionary = open('engmix.txt')

wordz = []

for word in dictionary:
    word = word.strip()
    c=0
    p=0
    if 'c' in word:
        c+=1
    if 'p' in word:
        p+=1
    if c==3 and p==2:
        wordz.append(word)
        
print(wordz)
'''

#Program 2
'''
dictionary = open('engmix.txt')

wordCount = 0
for word in dictionary:
    if word != '':
        word = word.strip()
        if word[0] == 'r':
            wordCount += 1

print('There are',wordCount, 'words that start with r in the dictionary')
'''

#Program 3
'''
dictionary = open('engmix.txt')

num = int(input('Number: '))

for word in dictionary:
    if len(word) == num+1:
        print(word)
        break
'''

#Program 4

dictionary = open('engmix.txt')

letter = input('Enter letter: ')

total = 84100

for word in dictionary:
    if letter in word:
        total = total-1

print(total, 'words do not have',letter)

