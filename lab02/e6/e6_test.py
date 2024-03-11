import pytest

def hamming_distance(s, t):
    if len(s) != len(t):
        return -1
    sz = len(s)
    cnt = 0
    for i in range(sz):
        if s[i] != t[i]:
            cnt += 1
    return cnt

def test_answer():
    assert hamming_distance("G", "") == -1
    assert hamming_distance("", "G") == -1
    assert hamming_distance("G", "A") == 1
    assert hamming_distance("G", "G") == 0
    assert hamming_distance("GA", "GA") == 0
    assert hamming_distance("GA", "AG") == 2
    assert hamming_distance("AGCT", "AGCT") == 0
    assert hamming_distance("AGCT", "TCGA") == 4
    assert hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7
