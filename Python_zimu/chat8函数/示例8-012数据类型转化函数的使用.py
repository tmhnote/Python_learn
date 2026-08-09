print('非空字符串的布尔值：',bool('hello world'))
print('空字符串的布尔值：',bool('')) #
print('空列表的布尔值：',bool([]))
print('空列表的布尔值：',bool(list()))
print('空元组的布尔值：', bool(()))
print('空元组的布尔值：', bool(tuple()))
print('空集合的布尔值：', bool(set()))
print('空字典的布尔值：', bool({}))
print('空字典的布尔值：', bool(dict()))
print('-' * 30)
print('非0整数型的布尔值：', bool(123))
print('整数0的布尔值:', bool(0))
print('浮点数0.0的布尔值：', bool(0.0))

# 将其他类型转成字符串类型
lst = [1,2,3]
print(type(lst), lst)

s = str(lst) # 转成字符串类型
print(type(s), s)

# float类型和str类型转成int类型
print('-' * 20, 'float类型和str类型转成int类型', '-' * 20)
print(int(98.7) + int('90'))
# 注意事项
# print(int('98.7')) # 报错 ValueError: invalid literal for int() with base 10: '98.7'
# print(int('a')) # ValueError: invalid literal for int() with base 10: 'a'

print('-'*20, 'int,str类型转成float类型', '-'*20)
print(float(90) + float('3.14'))

s = 'hello world'
print(list(s))

seq = range(1,11)
print(tuple(seq))
print(list(seq))
print(set(seq))