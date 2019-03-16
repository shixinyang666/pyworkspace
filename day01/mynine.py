if __name__ == '__main__':

    #定义输入变量
    num = input("请输入数字:")
    #定义变量
    i = 1
    c = "*"
    d = "="
    #while循环
    while i <= int(num):
        j = 1
        while j <= i :
             print("{0}{1}{2}{3}{4}".format(i,c,j,d,i*j),end=" ")
             j += 1
        print("\n")
        i+=1
