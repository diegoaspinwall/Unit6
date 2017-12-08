#Diego Aspinwall
#12-8-17
#hw.py

dictionary = open('engmix.txt')

word = input('Word: ')

for l in dictionary:
    if word == l:
        print('Yes')
