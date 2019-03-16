#定义九九乘法表函数
def nine() :
    for i in range(1,10) :
        for j in range(1,i+1) :
            print("{0} * {1} = {2}".format(i,j,i*j),end="  ")
        print()

#定义1-100对齐
def num() :
    for i in range(1,101) :
        num = str(i).rjust(3," ")
        print(num,end="")

        if i % 10 ==0 :
            print()

#定义菱形函数
def rhombus(row) :
    b=row
    c=row
    for i in range(1,row+1) :
        print(" "*(c-1),"*"*(2*i-1))
        c-=1
    if i == row :
        for j in range(1,row) :
            print(" "*j,"*"*(2*b-3))
            b-=1

#定义等边三角形函数
def triangle(row) :
    for i in range(row+1):
        print(" " * (row - i), end="")
        print(" *" * i)

