# -*- coding:utf-8 -*-
import math

# from XXX import xxx 从同级目录下引入py文件中的函数
# 例子：
# from test import XXX  从test.py文件中引入xxx()函数


# tuple_a=(1,24,5)
# b={2,3,tuple_a}
# print(b[2])
# a={1,2,3,[23,4,5]}
# print (a[1])
# d={'a':'test'}
set_a = set([1, 2, 3, 4])
print(set_a)

# set_b={1,2,3,[5,6]}
# print(set_b) TypeError: unhashable type: 'list'

print(hex(255))
print(hex(1000))


# key='b'
# d[key]='value_test'
# print(d)
# print(d['a'])
# print(d['b'])

# 定义函数
def my_abs(x):
    # 判断传参是否是允许的类型，如果不是，则抛出异常
    if not isinstance(x, (int, float)):
        raise TypeError("xxxxxxxx")
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(9))
print(my_abs(-100))


# print((my_abs('A')))
# dfsdf

# asdfdfadfasdfadsf
#
# asdf
# dasf


# 定义空函数
# pass 做占位符
def nop():
    pass


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(3, 4, 1, 60)
print(move(10, 9, 2, 90))
print(x, y)
r = move(3, 4, 1, 60)
print(type(r))  # <class 'tuple'>


# 关键字参数
def person(name, age, **kwargs):
    print("name:", name, "age:", age, "other:", kwargs)


person('bob', 30, city="beijing", address="xss_sd_sdf")
person('sum', 23)
