#Diego Aspinwall
#12-6-17
#howManyWords.py

dictionary = open('engmix.txt')

for i in range(2,23):
    num = 0
    for word in dictionary:
        if len(word) == i:
            num+=1
    print('There are', num, i-1, 'letter words')
