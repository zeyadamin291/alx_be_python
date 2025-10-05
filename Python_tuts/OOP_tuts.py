import unittest


def is_greater_or_equal_120(num):
    return num >= 120

class Mytestcase(unittest.TestCase):
    def testOne(self):
        num = int(input("enter a number"))  
        self.assertTrue(is_greater_or_equal_120(num), 
        f"should be true, {num} is not greater than or equal to 120")
    def testTwo(self):
        num = int(input("\nenter a number"))  
        self.assertTrue(is_greater_or_equal_120(num), 
        f"should be true, {num} is not greater than or equal to 120")
    def testThree(self):
        num = int(input("\nenter a number"))  
        self.assertTrue(is_greater_or_equal_120(num), 
        f"should be true, {num} is not greater than or equal to 120")

if __name__ == "__main__":
    unittest.main()