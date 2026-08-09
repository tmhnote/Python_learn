a = 100 # 全局变量

def calc(x, y):
    return a + x + y
print(a)
print(calc(10, 20))
print('-'* 30)

def calc2(x, y):
    a = 200 # 局部变量，局部变量的名称和全局变量的名称可以相同
    return a + x + y # 此处 a 是局部变量还是全局变量？  局部变量
# 当全局变量和局部变量的名称相同时，哪个优先级高呢？ 局部变量

print(calc2(10, 20)) # 230
print(a)
print('-'* 30)
def calc3(x, y):
    global s # s是在函数中定义的变量，但是使用了global关键字声明，这个变量s 变成了全局变量
    s = 300
    return s + x + y

print(calc3(10, 20))
print(s) # 全局变量可以直接打印输出