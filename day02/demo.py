if __name__ == '__main__':
    #输出1-100 并对齐
    for i in range(1,101) :
            num = str(i).rjust(3," ")
            print(num, end=" ")
            if i % 10 ==0 :
                print()

    #把重复的字符串挑出来 并统计次数
        #定义字符串
    mstr = "deepdarkfantasies,吼吼吼吼全给党"
    mlist = ""
        #统计字符串重复的次数
    for i in mstr :
        mnum = mstr.count(i)
        mfind = mlist.find(i)

        if mfind < 0 :
            mlist+=i
            if mnum > 1:
                print("重复过的字符为: {0}  出现的次数为: {1}".format(i, mnum))

    #判断闰年还是平年
    myear = int(input("请输入一个年份:"))
    if myear%4==0 and myear%100!=0 or myear%400==0:
        print("是")
    else:
        print("不是")




