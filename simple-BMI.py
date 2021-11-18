#!/usr/bin/env python
w = input("enter your weight: ")
h = input("enter yout height: ")
weight = int(w)
height = int(h)

BMI = weight  / ((height/100)* (height/100))

print("{:.1f}".format(BMI))




