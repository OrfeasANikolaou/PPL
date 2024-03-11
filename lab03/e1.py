import unittest
import random

def e_approx(n): 
    times = 0;
    for i in range(n):
        x = 0
        while x <= 1:
            times += 1
            x = x + random.random()
    return round(times/n, 7)
#    return times/n 

# Mην αλλάξετε κάτι από εδώ και κάτω
class Test(unittest.TestCase):
    def test_e_approximation(self):
        self.assertAlmostEqual(e_approx(1_000_000), 2.7182818, delta=0.001)


if __name__ == "__main__":
    unittest.main()
