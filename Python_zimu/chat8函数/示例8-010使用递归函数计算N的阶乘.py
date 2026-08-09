def fac(n): # n的阶乘 N!= N* (N-1)!......1!=1
    if n==1: # 递归终止条件
        return 1

    # 递归的调用
    else:
        return n*fac(n-1) # 阶乘计算公式, 自己调用自己

print(fac(5)) # 5! = 5*4*3*2*1 = 120