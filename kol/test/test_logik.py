from unittest import TestCase
from kol.logik import operation
class LogicTest(TestCase):
    def plus(self):
        result=operation(2,2,'+')
        self.assertEqual(result,4)
    def minus(self):
        result=operation(10,2,'-')
        self.assertEqual(result,8)
    def multiplication(self):
        result=operation(2,3,'*')
        self.assertEqual(result,6)
    def division(self):
        result=operation(10,5,'/')
        self.assertEqual(result,2)
