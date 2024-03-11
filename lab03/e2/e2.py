# Θεωρήστε ως λέξεις τις συμβολοσειρές που περιέχουν μόνο χαρακτήρες του αγγλικού αλφαβήτου.

import re
import unittest

# text with commas and dots
text1 = """One morning, when Gregor Samsa woke from troubled dreams, he found
himself transformed in his bed into a horrible vermin. He lay on his
armour-like back, and if he lifted his head a little he could see his
brown belly, slightly domed and divided by arches into stiff sections.
The bedding was hardly able to cover it and seemed ready to slide off
any moment. His many legs, pitifully thin compared with the size of the
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
    return len(set(words2))

# Πλήθος των λέξεων που ξεκινούν με τον χαρακτήρα 'h' και τελειώνουν με τον χαρακτήρα 'e'
def q2():
    ...


# Πλήθος των λέξεων του κειμένου με 5 χαρακτήρες
def q3():
    words = text2.split()
    cnt = 0
    for word in words:
        if len(word) == 5:
            cnt += 1
    return cnt


# Πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 'a', 's'
def q4():
    ...


# πλήθος λέξεων του κειμένου που περιέχουν συνεχόμενους τους χαρακτήρες 'a', 's' σε οποιαδήποτε σειρά
def q5():
    ...


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τον ίδιο χαρακτήρα
def q6():
    ...


# πλήθος λέξεων του κειμένου που ξεκινούν και τελειώνουν με τους 2 ίδιους χαρακτήρες
def q7():
    ...


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
