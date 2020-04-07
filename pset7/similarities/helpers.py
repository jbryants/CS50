from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    lines0 = set(a.split('\n'))
    lines1 = set(b.split('\n'))

    # matching similar lines
    sim_lines = [l0 for l0 in lines0 if l0 in lines1]

    return sim_lines


def sentences(a, b):
    """Return sentences in both a and b"""
    sent0 = set(sent_tokenize(a))
    sent1 = set(sent_tokenize(b))

    # matching similar sentences
    sim_sent = [s0 for s0 in sent0 if s0 in sent1]

    return sim_sent


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    substrs_0 = get_substrs(a, n)
    substrs_1 = get_substrs(b, n)

    # matching similar substrings
    sim_substrs = [s0 for s0 in substrs_0 if s0 in substrs_1]

    return sim_substrs


def get_substrs(string, n):
    """Return substrings of length n in string"""
    # setting i to 0 and j to n
    i = 0
    j = n

    # length of string
    length = len(string)
    substrs = set()

    # adding the all the substrings to substr set.
    while (j <= length):
        substrs.add(string[i:j])
        i += 1
        j += 1

    return substrs