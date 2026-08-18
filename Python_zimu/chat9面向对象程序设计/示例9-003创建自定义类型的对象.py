# 类
# 编写一个Person 类型
class Person():
    pass

# 编写一个Cat 类型
class Cat():
    pass

# 编写一个Dog 类型
class Dog():
    pass

# 编写一个Student 类型
class Student():
    pass

class StudentPerson(Cat, Dog):
    pass

# 对类名 后面的括号 省略
class Pig:
    pass

# 创建类的对象
# 语法结构  对象名 = 类名()

# 创建一个Person类型的对象
per = Person() # per 就是 Person 类型的对象
c = Cat() # c 就是 Cat 类型的对象
d = Dog() # d 就是 Dog 类型的对象
s = Student() # s 就是 Student 类型的对象
print(type(per)) # <class '__main__.Person'>
print(type(c)) # <class '__main__.Cat'>
print(type(d)) # <class '__main__.Dog'>
print(type(s)) # <class '__main__.Student'>