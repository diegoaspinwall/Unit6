#Diego Aspinwall
#12-7-17
#reverseFile.py

filechoice = open(input('Enter a file: '))

newlist = []

for word in filechoice:
    newlist.append(word.strip())

newlist.reverse()

for line in filechoice:
    print(line.strip())
