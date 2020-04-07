from sys import argv
from crypt import crypt


def cmpHash(string):
    """Compares hashes and exits if match found"""
    if crypt(string, salt) == hash_val:
        print(string)
        exit(0)


def main():
    """
    Generating all permutations of alphabets
    starting from n=1 (e.g:- 'a') upto n=5 (e.g:- 'abcde')
    and comparing their hash with given hash.
    """
    for a in alpha:
        cmpHash(a)
        for l in alpha:
            cmpHash(a + l)
            for p in alpha:
                cmpHash(a + l + p)
                for h in alpha:
                    cmpHash(a + l + p + h)
                    for al in alpha:
                        cmpHash(a + l + p + h + al)


if __name__ == '__main__':
    # Accept argv only if argv[1] is present and no more.
    if len(argv) != 2:
        print("Usage: python crack.py hash")
        exit(1)
    else:
        # set hash_val and salt as first two characters of hash.
        hash_val = argv[1]
        salt = argv[1][:2]

    # all alphabets
    alpha = "ETAOINSHRDLCUMWFGYPBVKJXQZetaoinshrdlcumwfgypbvkjxqz"
    main()