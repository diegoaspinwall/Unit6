#Diego Aspinwall
#12-8-17
#hw.py

dictionary = open('engmix.txt')
'''
word = input('Word: ')

yes = False

for l in dictionary:
    if l.strip() == word:
        yes = True

if yes == True:
    print(word,'is in the dictionary')
else:
    print(word, 'is not in the dictionary')


diclist = []

for word in dictionary:
    diclist.append(word.strip())

num = int(input('Enter a number: '))

print(diclist[num-1])


file = open('reverseFile.py')

for word in file:
    print(word.strip(), '!')
'''

letter = input('Enter a letter')

highword = ''
highnum = 0
for word in dictionary:
    for let in word:
        
    if highnum < len(word):
        highnum = len(word)
        highword = word
print(highword.strip())
print(len(highword))
