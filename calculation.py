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
