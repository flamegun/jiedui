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
