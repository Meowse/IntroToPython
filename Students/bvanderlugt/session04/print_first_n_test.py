import unittest
from print_first_n import print_first_nn

class MyFuncTestCase(unittest.TestCase):
    def test_my_fun(self):
        test_vals = (2, 3)
        expected = reduce(lambda x, y: x*y, test_vals)
        actual = my_func(*test_vals)
        self.assertEquals(expected, actual)


if __name__ == '__main__':
    unittest.main()
        
