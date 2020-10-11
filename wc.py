#!/usr/bin/python
import argparse
import re
#argparse模组说明
# dest：如果提供dest，例如dest="a"，那么可以通过args.a访问该参数
# ""内是参数，可用-+参数名（短参）或者用--+参数名（长参）
#type：将数据类型转换为规定的。（此处不需要）
#help：参数命令的介绍
parser = argparse.ArgumentParser()
#()内加上description=“”是对文件的描述。可写可不写。
parser.add_argument("-c", dest="char",help="add up")
parser.add_argument("-w", dest="word",help="add up")
parser.add_argument("-l", dest="line",help="add up")
args = parser.parse_args()

#行数
def Line_count(args):
    file=open(args, 'r', encoding='utf-8')
    lines =len(file .readlines() )
    return lines
#len（）函数可以直接统计行数

def Word_count(args):  # 统计单词数

    with open(args, 'r', encoding='utf-8') as f:
        dictResult = {}

        for line in f.readlines():
            listMatch = re.findall('[a-zA-Z]+', line.lower())
            # Count
            for eachLetter in listMatch:
                eachLetterCount = len(re.findall(eachLetter, line.lower()))
                dictResult[eachLetter] = dictResult.get(eachLetter, 0) + eachLetterCount
        result = sorted(dictResult.items(), key=lambda d: d[1], reverse=True)
    return result



def Character_count(args):  # 统计字符数
    file=open(args, 'r', encoding='utf-8')
    characters=str(len(file .read()))
    return characters
#包含换行符号


# 调用函数输出
if args.line:  # 行数
    print('line：',  Line_count(args.line))
if args.word:  # 单词出现数目
    print('word：', Word_count(args.word))
if args.char:  ##字符数
    print('char：', Character_count(args.char))
