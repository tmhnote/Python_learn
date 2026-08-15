# format()
print(format(3.141592653589793, '.3f'))
print(format(3.1415, '20')) # 数值型默认右对齐
print(format('hello world', '20')) # 字符串默认左对齐
print(format('hello world', '*<20')) # <表示左对齐 , *表示填充符号 , 20表示显示的宽度
print(format('hello world', '*>20')) # >表示右对齐
print(format('hello world', '*^20')) # ^表示居中对齐

print(format(3.1415926, '.2f')) # 3.14
print(format(20, 'b')) # 二进制
print(format(20, 'o')) # 八进制
print(format(20, 'x')) # 十六进制
print(format(20, 'X'))

print('-'* 20)
print(len('helloword'))
print(len([10, 20, 30, 40, 50]))

print('-'* 20)
print(id(10)) # 查看对象的内存地址 140735333508168
print(id('helloword'))
print(type('helloword'), type(10))

print('-'* 20)
# eval()函数  去掉字符串左右的符号，去参与计算
print('10 + 30')
print(eval('10 + 30'))
print(eval('10 > 30'))
print(eval('10 < 30'))