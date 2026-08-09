def calc(a, b):
    s = a + b
    return s

# print(a, b, s)# 报错 NameError: name 'a' is not defined
'''
a,b 是函数的参数，参数是局部变量
s 是函数中定义的变量，是局部变量
'''
result = calc(2,3)
print(result)