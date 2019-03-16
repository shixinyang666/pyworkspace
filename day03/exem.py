import  random
if __name__ == '__main__':
    #1. 输入某年某月某日，判断这一天是这一年的第几天？
    mdate = input("请输入年月日:")
    year = int(mdate[0:4])
    moth = int(mdate[4:6])
    day = int(mdate[6:8])
    mday = 0
    #循环判断这是一年中的多少天31+29+8
    for i in range(1,moth) :
        #判断是闰年还是平年
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if(i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12) :
                mday+=31
            elif(i==2) :
                mday+=29
            else :
                mday+=30
        else:
            if (i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12):
                mday += 31
            elif (i == 2):
                mday += 28
            else:
                mday += 30

    #输出
    print("这是{0}年的第{1}天".format(year,mday+day))

    #输入两个人的出生月份，来计算两个人的缘分
    mbrithday1 = int(input("请输入第一个人的出生月份:"))
    mbrithday2 = int(input("请输入第二个人的出生月份:"))

    #先判断两个人谁的出生月份更大
    if mbrithday1 > mbrithday2 :
        #开始取模算缘分
        if mbrithday1 % mbrithday2 == 1:
            print("非常有缘")
        elif mbrithday1 % mbrithday2 == 2:
            print("比较有缘")
        elif mbrithday1 % mbrithday2 == 3:
            print("缘分一般")
        elif mbrithday1 % mbrithday2 == 4:
            print("有仇")
        else:
            print("没有缘分")
    else:
        if mbrithday2 % mbrithday1 == 1:
            print("非常有缘")
        elif mbrithday2 % mbrithday1 == 2:
            print("比较有缘")
        elif mbrithday2 % mbrithday1 == 3:
            print("缘分一般")
        elif mbrithday2 % mbrithday1 == 4:
            print("有仇")
        else:
            print("没有缘分")

    #随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中
    mnum = [random.randint(1,10) for i in range(1,10)]
    print(mnum)
    mnum2 = random.randint(1,10)
    print(mnum2)
    if mnum2 in mnum :
        print("在序列中")
    else:
        print("不在序列中")

    #4.随机生成一个序列，10个元素，并对序列进行升序排序
    mnum3 = [random.randint(1,10) for  i in range(1,10)]
    mnum3.sort()
    print(mnum3)