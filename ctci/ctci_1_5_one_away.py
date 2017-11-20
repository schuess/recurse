#usr/bin/env python3

# Given two strings, write a function to check if they are 0 or 1 edit(s) away

def one_away(s1, s2):

    longer = len(s1) - len(s2)
    diff = abs(longer)

    if diff == 1:
        # Reduce extra letter case to equals case
        extra_letter = set(s1).symmetric_difference(s2).pop()
        if longer == 1:
            s1 = s1.replace(extra_letter, '')
        else:
            s2 = s2.replace(extra_letter, '')

    # Two cases if lengths are the same (diff == 0)
    if s1 == s2:
        return True
    s = set(s1)
    ss = set(s2)
    if len(s - ss) == 1 and len(ss - s) == 1:
        return True

    return False
