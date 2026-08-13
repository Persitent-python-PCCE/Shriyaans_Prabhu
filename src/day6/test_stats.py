import unittest 
from unittest import TestCase
from functions import factorial
class TestClass(TestCase):
    def test_fact(self):
        result=factorial(5)
        self.assertEqual(result,120)
unittest.main()
