#Diego Aspinwall
#12-13-17
#quiz6.py

#Program 1

dictionary = open('engmix.txt')

wordz = []

for word in dictionary:
    word = word.strip()
    clet=0
    plet=0
    for let in word:
        if let == 'c':
            clet+=1
        if let == 'p':
            plet+=1
    if clet==3 and plet==2:
        wordz.append(word)

for thing in wordz:
    print(thing)


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
'''
dictionary = open('engmix.txt')

letter = input('Enter letter: ')

total = 84100

for word in dictionary:
    if letter in word:
        total = total-1

print(total, 'words do not have',letter)
'''

#Program 5
'''
dictionary = open('engmix.txt')

diclist = []

for word in dictionary:
    diclist.append(word.strip())

print(diclist[84100/2-1])
'''
