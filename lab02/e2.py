import unittest


def is_pangram(s):
    greekletters = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    n_letters = len(greekletters)
    appears = n_letters * [False]
    for letter in s:
        for i in range(n_letters):
            if letter == greekletters[i]:
                appears[i] = True
    for i in range(n_letters):
        if not appears[i]:
            return False
    return True


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestPantogram(unittest.TestCase):
    def test(self):
        self.assertEqual(is_pangram("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"), True)
        self.assertEqual(is_pangram("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"[::-1]), True)
        self.assertEqual(is_pangram("ΞΕΣΚΕΠΑΖΩ ΤΗΝ ΨΥΧΟΦΘΟΡΟ ΒΔΕΛΥΓΜΙΑ"), True)
        self.assertEqual(
            is_pangram(
                "Ο ΚΑΛΥΜΝΙΟΣ ΣΦΟΥΓΓΑΡΑΣ ΨΙΘΥΡΙΣΕ ΠΩΣ ΘΑ ΒΟΥΤΗΞΕΙ ΧΩΡΙΣ ΝΑ ΔΙΣΤΑΖΕΙ"
            ),
            True,
        )
        self.assertEqual(is_pangram(""), False)
        self.assertEqual(is_pangram("A" * 24), False)
        self.assertEqual(is_pangram("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨA"), False)


if __name__ == "__main__":
    unittest.main()
