# 个数可变的位置参数
def fun(*prva):
    print(type(prva))
    for item in prva:
        print(item)

# 调用
fun(10, 20, 30, 40)
fun(10)
fun(20, 30)
fun([11, 22, 33, 44]) # 实际上传递的是一个参数 ，整个列表

# 在调用时，参数前加一颗星，分将列表将进行解包
fun(*[10, 20, 30, 40])


# 个数可变的关键字参数
def fun2(**kwpra):
    print(type(kwpra))
    for key,value in kwpra.items():
        print(key,'-----',  value)

# 调用
fun2(a=1, b=2, c=3)
fun2(name='John', age=23, height=170)

d = {'a': 1, 'b': 2, 'c': 3}
d2 = {'name': 'John', 'age': 23, 'height': 170}

# fun2(d) # 报错  TypeError: fun2() takes 0 positional arguments but 1 was given
fun2(**d)
fun2(**d2)