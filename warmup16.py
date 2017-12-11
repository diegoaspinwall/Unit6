#Diego Aspinwall
#12-11-17
#warmup16.py

dictionary = open('engmix.txt')

ans = []

for word in dictionary:
    if word != '':
        if word.strip()[0] == 'd' and word.strip()[-1] == 'a':
            ans.append(word.strip())

for wrd in ans:
    print(wrd)
