import string

def is_pangram(s):
    nStr = s.upper()
    alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for l in alp:
        if l not in nStr:
            return False
    return True

is_pangram("The quick brown fox jumps over the lazy dog")