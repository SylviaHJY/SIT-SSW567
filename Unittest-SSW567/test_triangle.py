#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   test_triangle.py
@Time    :   2023/02/03 18:12:49
@Author  :   Jiayin Huang 
@ID      :   10477088
@Version :   1.0
@Desc    :   write a program in Python to classify triangles and use an automated test platform, e.g. UnitTest
equilateral triangles have all three sides with the same length
isosceles triangles have two sides with the same length
scalene triangles have three sides with different lengths
right triangles have three sides with lengths, a, b, and c where a2 + b2 = c2
'''

import unittest #The test framework

def classify_triangle(a,b,c):
  if(a <= 0 or b <= 0 or c <= 0):
    return "Invalid triangle";
  
  if (a + b <= c or a + c <= b or b + c <= a):
    return "Invalid triangle";
  
  if (a == b == c):
    return "Equilateral triangle";
  
  if (a == b or a == c or b == c):
      return "Isosceles triangle";
    
  if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
    return "Scalene right triangle";
  
  return "Scalene triangle";
  
  
class TestTriangleClassification(unittest.TestCase):
  def test_valid_triangles(self):
    self.assertEqual(classify_triangle(3, 4, 5), "Scalene right triangle");
    self.assertEqual(classify_triangle(3, 3, 3), "Equilateral triangle");
    self.assertEqual(classify_triangle(2, 2, 3), "Isosceles triangle");
    self.assertEqual(classify_triangle(2, 2, 2 ** 0.5), "Isosceles triangle");
   
      
  def test_negative_triangles(self):
    self.assertEqual(classify_triangle(-1, 2, 2), "Invalid triangle");
    
  def test_zero_length_triangles(self):
    self.assertEqual(classify_triangle(0, 2, 2), "Invalid triangle");
      
      
if __name__ == '__main__':
    unittest.main()
  
#try:
  #a = float(input("Enter the first side length: "))
  #b = float(input("Enter the second side length: "))
  #c = float(input("Enter the third side length: "))
  #result = classify_triangle(a, b, c)
  #print("Result:", result)
#except ValueError:
  #print("Error: Invalid input, sides must be numbers.")