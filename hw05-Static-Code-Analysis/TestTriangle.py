# -*- coding: utf-8 -*-
"""
You will run a static code analyzer on your code, e.g. Pylint, 
identify and fix any problems reported by the static code analyzer;
You will run a code coverage tool on your code, e.g. Coverage.py,
and extend your test cases to demonstrate at least 80% code coverage;

C is for convention, R is refactor, W is warning and E is error. 

@author: Jiayin Huang
"""
# pylint: disable=missing-docstring

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
              
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
          
    def test_negative_triangles(self):
        self.assertEqual(classifyTriangle(-1, 2, 2), 'InvalidInput','-1,2,2 should be invalidInput')
         
    def test_zero_length_triangles(self):
        self.assertEqual(classifyTriangle(0, 2, 2), 'InvalidInput','0,2,2 should be invalidInput')
          
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a right triangle')
        
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5,5,7),'Isosceles','5,5,7 is a Isosceles triangle')
         
    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(8,8,10),'Isosceles','8,8,10 is a Isosceles triangle')
         
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(8,15,20),'Scalene','8,15,20 is a Scalene triangle')
        
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(12,17,26),'Scalene','12,17,26 is a Scalene triangle')
        
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(12,3,20),'NotATriangle','12,3,20 is NotATriangle')
         
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(6,7,18),'NotATriangle','6,7,18 is NotATriangle')
         
    def test_Greater_200(self):
        self.assertEqual(classifyTriangle(230,7,18),'InvalidInput','230,7,18 is greater than 200')
           
    def test_Not_Int(self):
      self.assertEqual(classifyTriangle('a','b','c'),'InvalidInput','a,b,c is not legal triangle')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()