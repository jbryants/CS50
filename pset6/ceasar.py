from sys import argv

# Accept argv only if argv[1] is present and it is a positive int.
if len(argv) != 2 or (int(argv[1]) <= 0):
    print("Usage: python caesar.py k")
    exit(1)
else:
    k = int(argv[1])

plaintxt = input('plaintext: ')

# uppercase letters and lowercase letters list.
uc_alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lc_alp = 'abcdefghijklmnopqrstuvwxyz'

# generate and print out ciphertext.
print("ciphertext: ", end='')
for p in plaintxt:
    # check if alpha then proceed, else just print char.
    if p.isalpha():
        # if uppercase letter then cipher and index uc_alp list.
        if p.isupper():
            idx = ((uc_alp.index(p) + k) % 26)
            print(uc_alp[idx], end='')
        # else cipher and index lc_alp list.
        else:
            idx = ((lc_alp.index(p) + k) % 26)
            print(lc_alp[idx], end='')
    else:
        print(p, end='')
print()