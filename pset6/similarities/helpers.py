# import from Natural Language Toolkit
from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""
    asplit = a.splitlines()
    bsplit = b.splitlines()
    # use a set
    same = {x for x in asplit if x in bsplit}
    return list(same)


def sentences(a, b):
    """Return sentences in both a and b"""
    asplit = sent_tokenize(a)
    bsplit = sent_tokenize(b)
    # use set again
    same = {x for x in asplit if x in bsplit}
    return list(same)


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    asplit = []
    bsplit = []
    for i in range(len(a) - n + 1):
        asplit.append(a[i:i + n])
    for i in range(len(b) - n + 1):
        bsplit.append(b[i:i + n])
    same = {x for x in asplit if x in bsplit}
    # TODO
    return list(same)