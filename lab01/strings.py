strings = ['This', 'list', 'is', 'now', 'all', 'together']
sentence = ''
for x in strings:
   sentence += x
   sentence += " "
sentence = sentence[:-1]
print(sentence)
print(' '.join(strings))
