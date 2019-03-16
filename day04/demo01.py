#导入随机序列
import random
#输入某年某月某日，判断这一天是这一年的第几天
def myyear(yaer) :
    #字符串切割 年份
    myear = int(yaer[0:4])
    #字符串切割 月份
    mmonth = int(yaer[4:6])
    #字符串切割 日期
    mdate = int(yaer[6:8])
    mnum = 0
    #判断是平年还是闰年
    if myear % 4 ==0 and myear % 100 !=100 or myear % 400 ==0 :
        #循环统计日期
        for i in range(1,mmonth) :
            if i==1 or i==3 or i==5 or i==7 or i==8 or i==10 or i==12 :
                mnum+=31
            elif(mmonth==2) :
                mnum+=29
            else:
                mnum+=30
    else:
        # 循环统计日期
        for i in range(1, mmonth):
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                mnum += 31
            elif (mmonth == 2):
                mnum += 28
            else:
                mnum += 30

    print("这是{0}年的第{1}天".format(myear,mnum+mdate))


#输入两个人的出生月份，来计算两个人的缘分
def mymonth(month1,month2) :
    #首先判断两个人的出生月份谁的更大
    if month1 > month2 :
        #取余计算两个人的缘分
        mnum =month1 % month2

        if  mnum ==1 :
            print("非常有缘")
        elif (mnum == 2) :
            print("比较有缘")
        elif (mnum == 3):
            print("缘分一般")
        elif (mnum == 4):
            print("有仇")
        else:
            print("无缘")
    else:
        # 取余计算两个人的缘分
        mnum = month2 % month1
        if mnum == 1:
            print("非常有缘")
        elif (mnum == 2):
            print("比较有缘")
        elif (mnum == 3):
            print("缘分一般")
        elif (mnum == 4):
            print("有仇")
        else:
            print("无缘")

#随机生成一个序列，再次生成一个整数，查看这个整数有没有在序列中
def randomnum() :
    #随机生成一个序列
    mlist = [random.randint(1,10) for i in range(1,10)]
    print("随机生成一个序列——>{0}".format(mlist))
    #随机生成一个整数
    mnum = random.randint(1,10)
    print("随机生成一个整数——>{0}".format(mnum))
    #判断生成的整数是否在这个序列中
    if mnum in mlist :
        print("在这个序列中")
    else:
        print("不在这个序列中")

#随机生成一个序列，10个元素，并对序列进行升序排序
def listsort() :
    #列表随机生成10个元素
    mlist = [random.randint(1,10) for i in range(1,10)]
    #对列表进行升序排序
    mlist.sort()
    #输出
    print("列表按升序排列——>{0}".format(mlist))


#测试函数
# if __name__ == '__main__':
#     myyear("20120201")
#     mymonth(12,11)
#     randomnum()
#     listsort()