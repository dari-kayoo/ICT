sentence = "This is the lion in the cage"
words = sentence.split()
for i in words:
    if i != 'the':
        print(i, end = ' ')
