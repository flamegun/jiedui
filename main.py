#coding=utf-8
import random
from fractions import Fraction
#清空上一次的数据
file_handle1 = open('Exercises.txt','w+')
file_handle2 = open('Answers.txt','w+')
#file_handle = open('Exercises.txt','w+')
file_handle1.close( )
file_handle2.close( )

subject_num = int(input('需要生成的题目个数：'))
scope = int(input('需要生成四则运算的数最大为：'))
for i in range(0,subject_num):
    num1 = random.randint(1,scope)
    num2 = random.randint(1,scope) 
    num3 = random.randint(1,scope)
    symbol = ['+', '-', '*', '/']
    n1 = random.randint(0, 3)
    n2 = random.randint(0, 3)

    char_num = random.randint(1,3)#使运算符的个数不大于三个
    if char_num == 1:
        expression = str(num1) + symbol[n1] + str(num2)
    else:
        expression = str(num1) + symbol[n1] + str(num2) + symbol[n2] + str(num3)
