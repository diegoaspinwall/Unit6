#Diego Aspinwall
#12-8-17
#hw.py

dictionary = open('engmix.txt')

word = input('Word: ')

for l in dictionary:
    if l == word:
        print('Yes')
