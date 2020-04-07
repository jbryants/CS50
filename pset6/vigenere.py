from sys import argv


def main():
    # Accept argv only if argv[1] is present and it is a positive int.
    if len(argv) != 2 or not argv[1].isalpha():
        print("Usage: python vigenere.py k")
        exit(1)
    else:
        key = argv[1]

    plaintxt = input('plaintext: ')

    # uppercase letters and lowercase letters list.
    uc_alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lc_alp = 'abcdefghijklmnopqrstuvwxyz'

    # generate and print out ciphertext.
    print("ciphertext: ", end='')
    j = 0
    for p in plaintxt:
        # check if alpha then proceed, else just print char.
        if p.isalpha():
            j %= len(key)
            # if plaintext character is upper and key character is upper.
            if p.isupper() and key[j].isupper():
                idx = get_ciph_idx(uc_alp.index(p), uc_alp.index(key[j]))
                print(uc_alp[idx], end='')
                j += 1
            # if plaintext character is upper and key character is lower.
            elif p.isupper() and not key[j].isupper():
                idx = get_ciph_idx(uc_alp.index(p), lc_alp.index(key[j]))
                print(uc_alp[idx], end='')
                j += 1
            # if plaintext character is lower and key character is upper.
            elif not p.isupper() and key[j].isupper():
                idx = get_ciph_idx(lc_alp.index(p), uc_alp.index(key[j]))
                print(lc_alp[idx], end='')
                j += 1
            # if plaintext character is lower and key character is lower.
            else:
                idx = get_ciph_idx(lc_alp.index(p), lc_alp.index(key[j]))
                print(lc_alp[idx], end='')
                j += 1
        else:
            print(p, end='')
    print()


def get_ciph_idx(p_idx, key_idx):
    """ Returns cipher index """
    return (p_idx + key_idx) % 26


if __name__ == '__main__':
    main()