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
    file_handle1 = open('Exercises.txt','a')#写入题目
    file_handle1.writelines( '四则运算题目.' + str(i) +  '\t'  + expression + '=' + '\n')
    file_handle1.close()
    result = eval(expression)  # 题目答案
    result = Fraction(result).limit_denominator()  #结果转化为近似分数
    w = result.numerator
    r = result.denominator
    if w > r and r != 1:#判断是否为带分数
        result_end = str(str(int(w / r)) + "'" + str(w % r) + "/" + str(r))#转化为带分数形式
    else:
        result_end = str(result)
    file_handle2 = open('Answers.txt','a')#写入答案
    file_handle2.writelines('第' + str(i) + '题的答案：' + '\t' + result_end + '\n')
    file_handle1.close()

    int(i)
