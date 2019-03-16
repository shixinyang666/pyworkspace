if __name__ == '__main__':
    #定义字符串
    mstr = "ab,c,d,e,a,fa,hi,jka"

    #find查找子字符串是否在字符串中  find中第一个参数代表子字符串，
    # 第二个参数代表起始位置，第三个参数代表结束位置
    #找到后返回子字符串的下标否则返回-1
    mindex = mstr.find("a",1,mstr.__len__())
    print(mindex)

    #index查找子字符串是否在字符串中
    #index第一个参数代表子字符串，第二个参数代表起始值，第三个参数代表，结束值
    #找到该子字符串后返回下标否则将报异常
    mindex2 = mstr.index("a",0,mstr.__len__())
    print(mindex2)

    #count统计子字符串在字符串中出现的次数
    #count第一个参数代表子字符串，第二个参数代表起始值下标，第三个参数代表结束下标
    #最后返回子字符串一共出现了多少次
    mnum = mstr.count("a",0,mstr.__len__())
    print(mnum)

    #replace替换字符串中的元素
    #replace中的第一个参数代表要被替换的元素，第二个参数代表要替换的元素，第三个参数代表替换几次
    #最后返回替换过后的字符串
    mstr2 = mstr.replace("a","o",2)
    print(mstr2)

    #split将字符串分割
    #split第一个参数为分隔符 默认空字符串，空格 第二个参数为分割的次数
    #分割后返回一个字符串列表
    mlist = mstr.split(",",5)
    print(mlist)

    #将字符串首字母大写
    mstr3 = mstr.capitalize()
    print(mstr3)

    #startswitf函数 判断子字符串是否在字符串首位 返回值为布尔类型
    #startswith函数 第一个参数为要判断的子字符串，第二个参数为起始下标，第三个参数为结束下标
    mbool  = mstr.startswith("b",0,mstr.__len__())
    print(mbool)

    #endwith函数 判断子字符串是否在字符串结尾 返回值是布尔类型
    #endswith第一个参数是要判断的子字符串，第二个参数为起始下标，第三个参数为结束下标
    mbool2 = mstr.endswith("a",0,mstr.__len__())
    print(mbool2)

    #ljust左对齐 rjust右对齐
    #第一个参数是指定字符串长度，第二个是要填充的字符，默认为空格
    mstr4 = "123"
    #左对齐
    mljust = mstr4.ljust(10,"-")
    #右对齐
    mrjust = mstr4.rjust(10,"-")
    #输出
    print(mljust)
    print(mrjust)