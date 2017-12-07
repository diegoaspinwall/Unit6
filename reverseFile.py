#Diego Aspinwall
#12-7-17
#reverseFile.py

filechoice = open(input('Enter a file: '))

reverse = []

for word in filechoice:
    reverse.append(word.strip())

print(reverse)
