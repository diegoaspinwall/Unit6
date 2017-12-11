#Diego Aspinwall
#12-7-17
#longShort.py

alphabet = 'abcdefghijklmnopqrstuvwxyz'

longest = ['']*26
shortest = ['']*26

dictionary = open('engmix.txt')

for word in dictionary:
    if word != '':
        if len(word.strip()) > len(longest[alphabet.index[word.strip()[0]]]):
            longest.append(word.strip())
        if len(word.strip()) < len(shortest[alphabet.index[word.strip()[0]]]):
            shortest.append(word.strip())

print(longest)
print(shortest)
