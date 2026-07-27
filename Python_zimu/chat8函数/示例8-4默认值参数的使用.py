def happy_birthday(name = 'minghuitang', age = 24):
    print('Happy birthday, {}!'.format(name))
    print('{}岁生日快乐！'.format(age))


# 调用
happy_birthday() # 不用传参

happy_birthday('chenmeimei') # 位置传参

happy_birthday(age= 19) # 关键字传参， name 采用默认值

# happy_birthday(19) # 19 使用位置参数，传给了 name

def fun(a, b=20):
    pass

# def fun2(a=20, b):
#     pass
# 报错

# 当位置参数和关键字参数同时存在的时候，应该遵循 位置参数在前，默认值参数在后