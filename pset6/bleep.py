from sys import argv

# Accept argv only if argv[1] is present and no more.
if len(argv) != 2:
    print("Usage: python bleep.py dictionary")
    exit(1)
else:
    fobj = open(argv[1], 'r')
    # generating the dictionary of banned words.
    dictionary = set([l.rstrip('\n') for l in fobj.readlines()])

sentence = input("What message would you like to censor?\n")

# splitting the sentence based on space into words/tokens.
tokens = sentence.split(' ')

# bleeping the banned words if present in dictionary.
for token in tokens:
    if token.lower() in dictionary:
        print('*' * len(token), end=' ')
    else:
        print(token, end=' ')