# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:25:50 2020

@author: 1
"""

import random

def szys():#四则运算的核心功能
    sym = ['＋', '－', '×', '÷']#sym数组存储四则运算的符号
    f= random.randint(0, 3)# 生成0~3随机数赋值给f，用来指定四则运算的符号
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)# 生成100之间的整数，分别赋值给n1，n2
    n3 = 0 # n3用来存放除法运算的余数
    result = 0
    #以上为初始化
    
    if f== 0:#加法
        result  = n1 + n2
        
    elif f == 1:#减法，要先比较大小，防止输出负数
        n1, n2 = max(n1, n2), min(n1, n2)
        result  = n1 - n2
        
    elif f== 2:#乘法
        result  = n1 * n2
        
    elif f == 3:#除法，要比较大小，并计算余数
        n1, n2 = max(n1, n2), min(n1, n2)
        result = int(n1 / n2)
        n3 = n1 - result*n2
        
    print(n1, sym[f], n2, '= ', end='')
    return result,n3


def test():#制作题库
    print('输入所需要的题目数量')
    n=int(input())
    result =[]
    m=0
    while m<=(n-1):
        print(m+1,end='、')
        result .append(szys())#输出题目并保存答案
        print(' ')
        m=m+1
    m=0
    print('对应的答案：')
    while m<=(n-1):
        print(m+1,'、',result[m][0],end = '')
        if result[m][1]!=0:
            print('...',result[m][1])
        else:
            print('')
        m=m+1

print('这是一个小学生100以内整数加减乘除四则运算的小程序，提供一下2种模式：') 
print('1、进行四则运算')
print('   在窗口逐题输入答案，系统会判断正误并给与反馈，加减乘除(无余数)请直接输入结果，结果有余数的除法请先输入商，再输入余数')   
print('2、制作题库')
print('   教师可以根据提示输入题目数量，系统会自动给出题目')
print('选择想要的模式')
print('1、进行四则运算')
print('2、制作题库')
n=int(input())

#当输入1时，进行四则运算，调用函数syzs()
if n==1:
    print('题目数量：')
    num = int(input())
    temp = 0
    while temp < num:
        print('目前第',temp+1,'题，还剩',num-temp-1,'题')
        result,n3  = szys()
        j= int(input())
        if n3 == 0:
            if j== result :
                print('right')
            else:
                print('error.，the answer is', result )
        else:
            y = int(input())
            if j== result and y==n3 :
                print('right')
            else:
                print('error.，the answer is', result,'...',n3 )
        temp+=1

#当输入2时，进行制作题库
if n==2:
    test()
                
                
        
    
        
        
        
        
        
        