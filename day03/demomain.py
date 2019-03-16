#函数模块
import day03.demodef
if __name__ == '__main__':
    # #调用九九乘法表函数
     day03.demodef.nine()
    # #调用1-100对齐函数
     day03.demodef.num()
    # #调用菱形函数
     row = int(input("请输入菱形的行数:"))
     day03.demodef.rhombus(row)
    # #调用等边三角形函数
     row2 = int(input("请输入等边三角形的函数:"))
     day03.demodef.triangle(row2)

     m = "abc"
     print(m,sep="-")

