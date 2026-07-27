def get_sum(num): # num 是形式参数
    s = 0
    for i in range(1, num+1):
        s += i
    print(f'1到{num}之间的累加和为：{s}')

# 函数的调用
get_sum(10) # 1-10 之间的累加和   10 是实际参数值
get_sum(100) # 1-100 之间的累加和   100 是实际参数值
get_sum(1000) # 1-1000 之间的累加和  1000 是实际参数值

# 一次编写，多次调用