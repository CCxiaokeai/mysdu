# 声明一个int_demo 方法
def int_demo():
    # 声明aint变量，并赋值 1
    aint = 1
    # 打印aint的值
    print(aint)
    # 打印aint 的类型；type(aint):获取aint的类型
    print(type(aint))

# 声明一个 str_demo 方法
def str_demo():
    # 声明astr变量，并赋值 1
    astr = '1'
    # 打印astr 的值
    print(astr)
    # 打印satr 的值
    print(type(astr))

# 声明一个带参数的int_add 方法
def int_add(x,y):
    return x + y;




if __name__ == '__main__':
    # str_demo()
    # int_demo()
    # int_demo()
    print(int_add(343,5435))

    add = int_add(343, 5435)
    print(add)
    pass