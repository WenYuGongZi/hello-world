#!/usr/bin/env python3.6
# Author:zzy

print("hello,world !!!")
name = "zzy"
age = 18
this_year = 2017
print(name, age)
name2 = input("please input your name: ")#在2.7中input 输入的是字符串非字符串，而是一个变量
age2 = int(input("please input your age :"))
print("so you are born in ",this_year - age2)
print("\n")
name3 = "zzyy"
name4 = name3
print(name3,name4)
name3 = "yyyyyz"
print(name3,name4)
