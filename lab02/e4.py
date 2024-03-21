import unittest


def f1(lst):
    ret = []
    for obj in lst:
        ret.append(len(str(obj)))
    return ret


def f2(lst):
    ret = []
    for obj in lst:
        ret.append(int(str(obj)[::-1]))
    return ret


def f3(lst):
    ret = []
    s = sum(lst)
    avg = s / len(lst)
    for obj in lst:
        if obj > avg:
            ret.append(obj)
    return ret


def f4(lst):
    ret = []
    for obj in lst:
        ret.append((obj, obj % 2 == 0))
    return ret


class TestComprehensions(unittest.TestCase):
    def test1(self):
        a_list = [56, 37, 771, 90, 16, 11]
        b_list = [len(str(obj)) for obj in a_list]
        self.assertEqual(b_list, [2,2,3,2,2,2])         

    def test2(self):
        a_list = [56, 37, 771, 90, 16, 11]
        b_list = [int(str(obj)[::-1]) for obj in a_list] 
        self.assertEqual(b_list, [65,73,177,9,61,11])         

    def test3(self):
        a_list = [56, 37, 771, 90, 16, 11]
        b_list = [obj for obj in a_list if obj > sum(a_list)/len(a_list)] 
        self.assertEqual(b_list, [771])         

    def test4(self):
        a_list = [56, 37, 771, 90, 16, 11]
        b_list = [(obj, obj%2==0) for obj in a_list]
        self.assertEqual(b_list, [(56,True), (37,False), (771,False), (90, True), (16, True), (11, False)]) 

if __name__ == "__main__":
    unittest.main()
