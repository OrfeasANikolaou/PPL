# Θεωρήστε ως λέξεις τις συμβολοσειρές που περιέχουν μόνο χαρακτήρες του αγγλικού αλφαβήτου.

import re
import unittest

# text with commas and dots
text1 = """one morning, when gregor samsa woke from troubled dreams, he found
himself transformed in his bed into a horrible vermin. he lay on his
armour-like back, and if he lifted his head a little he could see his
brown belly, slightly domed and divided by arches into stiff sections.
the bedding was hardly able to cover it and seemed ready to slide off
any moment. his many legs, pitifully thin compared with the size of the
rest of him, waved about helplessly as he looked."""

# text without commas or dots
text2 = """one morning when gregor samsa woke from troubled dreams he found
himself transformed in his bed into a horrible vermin he lay on his
armour-like back and if he lifted his head a little he could see his
brown belly slightly domed and divided by arches into stiff sections
the bedding was hardly able to cover it and seemed ready to slide off
any moment his many legs pitifully thin compared with the size of the
rest of him waved about helplessly as he looked"""

# Πλήθος των λέξεων του κειμένου
def q1():
    words1 = text1.split()
    words2 = text2.split()
    words2 = set(words2)
    return len(words2)

# Πλήθος των λέξεων που ξεκινούν με τον χαρακτήρα 'h' και τελειώνουν με τον χαρακτήρα 'e'
def q2():
    words = text2.split()
    words = set(words)
    cnt = 0
    for word in words:
        if re.search(r"\b^h\w*e$\b", word) != None:
            cnt += 1
    return cnt

# Πλήθος των λέξεων του κειμένου με 5 χαρακτήρες
def q3():
    words = text2.split()
    words = set(words)
    cnt = 0
    for word in words:
        if re.search(r"\b\w{5}\b", word) != None:
            cnt += 1
    return cnt


# Πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 'a', 's'
def q4():
    words = text2.split()
    words = set(words)
    cnt = 0
    for word in words:
        if re.search(r"\b\w*as\w*\b", word) != None:
            cnt += 1
    return cnt


# πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 'a', 's' σε οποιαδήποτε σειρά
def q5():
    words = text2.split()
    cnt = 0
    for word in words:
        if re.search(r"\b\w*as\w*|\w*sa\w*\b", word) != None:
            cnt += 1
    return cnt


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τον ίδιο χαρακτήρα
def q6():
    words = text2.split()
    words = set(words)
    cnt = 0
    for word in words:
        if re.search(r"\b(\w)\w*\1\b", word) != None:
            cnt += 1
    return cnt


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τους 2 ίδιους χαρακτήρες
def q7():
    words = text2.split()
    words = set(words)
    cnt = 0
    for word in words:
        if re.search(r"\b(\w\w)\w*\1\b", word) != None:
            cnt += 1
    return cnt 


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestReExamples(unittest.TestCase):
    text1 = text1.lower()
    text2 = text2.lower()
    def test_q1(self):
        self.assertEqual(q1(), 70)

    def test_q2(self):
        self.assertEqual(q2(), 2)

    def test_q3(self):
        self.assertEqual(q3(), 12)

    def test_q4(self):
        self.assertEqual(q4(), 2)

    def test_q5(self):
        self.assertEqual(q5(), 3)

    def test_q6(self):
        self.assertEqual(q6(), 3)

    def test_q7(self):
        self.assertEqual(q7(), 1)


if __name__ == "__main__":
    unittest.main()
