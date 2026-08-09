def happy_birthday(name, age):
    print('Happy birthday, {}!'.format(name))
    print('{}岁生日快乐！'.format(age))

# 关键字传参
happy_birthday(age=24, name= 'minghuitang') # 定义处的形参为 name

happy_birthday('chenmeimei', age= 18)

# happy_birthday(name='chenmeimei', 18) # SyntaxError: positional argument follows keyword argument


# 位置参数在前，关键字传参在后 ，否则程序报错