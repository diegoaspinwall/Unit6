#Diego Aspinwall
#12-11-17
#warmup16.py

dictionary = open('engmix.txt')

ans = []

for word in dictionary:
    if word[0] == 'd' and word[-1] == 'a':
        ans.append(word.strip())

for wrd in ans:
    print(wrd)
