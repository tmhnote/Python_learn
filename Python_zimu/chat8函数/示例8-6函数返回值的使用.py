# 函数的返回值
def calc(a,b):
    print(a+b)

calc(1,2)
print(calc(3,4))

'''
执行流程：
1. `calc(a=1,b=2)` → 函数内执行 `print(1+2)` → 输出 `3`
2. `print(calc(a=3,b=4))`
   - 先运行 `calc(3,4)`：函数内部打印 `7`
   - `calc` 执行完毕返回默认值 `None`
   - 外层 `print()` 打印这个返回值 → 输出 `None`
'''

def calc2(a,b):
    s=a+b
    return s # 将s返回给函数的调用处去处理

print('-' *20)

calc2(1,2)
'''
这里没有变量接收、没有print()
返回值3没有任何容器存放 → 直接被系统回收丢弃
该行执行完毕，控制台无任何输出
'''
get_s = calc2(3,4)
print(get_s)

get_s2 = calc2(calc2(2, 2), 4)
print(get_s2)

get_s3 = calc2(calc2(1,2),calc2(3,4))
print(get_s3)


# 返回值是多个
def get_sum(num):
    s = 0
    odd_sum = 0 # 奇数和
    even_sum = 0 # 偶数和
    for i in range(1, num+1):
        if i % 2 != 0: # 判断是奇数
            odd_sum += i
        else:
            even_sum += i
        s += i
    return s, odd_sum, even_sum

result = get_sum(10)
print(type(result)) # <class 'tuple'>
print(result)


# 解包赋值
a, b, c = get_sum(10)
print(a, b, c) # 输出结果 55 25 30