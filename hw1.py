# -*- coding: utf-8 -*-
"""hw1.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AqtWuk2yuQV87xoKlNcPL8JSBdac-cta
"""

def get_radius(prompt):
  r = int(input(prompt))
  return r
def get_circle_area(A):
  a = 3.14 * A * A
  return a

r = get_radius('넓이를 구하고자 하는 원의 반지름은?')
a = get_circle_area(r)
print('반지름',r,'인 원의 넓이 = 3.14 x',r,'x',r,'=',a)
