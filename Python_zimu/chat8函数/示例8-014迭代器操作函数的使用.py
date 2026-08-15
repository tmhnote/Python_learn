lst = [54, 55, 4, 77, 34, 89]

# 排序操作(1)
asc_lst = sorted(lst) # 升序
deasc_lst = sorted(lst, reverse=True) # 降序
print('原列表：', lst)
print('升序：', asc_lst)
print('降序：', deasc_lst)

# (2)reversed 反向
new_lst = reversed(lst)
print(type(new_lst)) # <class 'list_reverseiterator'> 迭代器对象
print(list(new_lst)) # 将迭代器对象转成列表 进行输出在控制台显示
print(new_lst)

# (3)zip
x =[ 'a', 'b', 'c', 'd']
y = [10, 20, 30, 40, 50]
zipobj = zip(x, y)
print(type(zipobj)) # <class 'zip'>
# print(list(zipobj)) # 因为后面 调用next函数 才将其进行注释

# (4)enumerate
enmu = enumerate(y, start=1)
print(type(enmu)) # <class 'enumerate'>
print(list(enmu))
print(tuple(enmu)) # 核心原因是：'enumerate' 返回的是迭代器对象，迭代器是「一次性消耗品」，只能遍历一次**。

# (5)all
lst2 = [ 10, 20, '', 30]
print(all(lst2)) # False 空字符串的布尔值是False
print(all(lst)) # True 所以对象的布尔值都为True 结果对象为True

# (6)any
print(any(lst2)) # True 只要有一个结果为True结果就为True, 所有结果都为False结果才为False

# (7)next
print(next(zipobj)) # ('a', 10)
print(next(zipobj)) # ('b', 20)
print(next(zipobj)) # ('c', 30)


def fun(num):
    return num %2 ==1 # 可能是False ,True
# 函数作为参数为 fun , 函数作为调用为 fun()
obj = filter(fun, range(10)) # 将range(10) , 0-9的整数,都执行一次fun操作 将结果为True的放到obj中
print(list(obj))


def upper(x):
    return x.upper()

new_lst2 = ['hello', 'world', 'python']
obj2 = map(upper, new_lst2)
print(list(obj2))