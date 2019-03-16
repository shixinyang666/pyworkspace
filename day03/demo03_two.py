if __name__ == '__main__':
    #1.	编写Python程序判断字符串是否重复

    #创建一个字符串
    mstr = "abcdadbgghefflf"

    #把字符串存入set集合中再比较长度如果长度一致就是不重复的字符串
    if len(mstr) != len(set(mstr)) :
        print("是重复的字符串")
    else:
        print("不是重复的字符串")

    #2.	编写Python程序打印输出字符串中重复的所有字符

    #创建一个子字符串
    nstr = ""
    #循环获取字符在字符串中出现的次数
    for i in mstr :
        #统计字符在字符串出现的次数
        mconunt = mstr.count(i)
        #判断该字符是否在子字符串中
        mfind = nstr.find(i)
        #判断如果不在子字符串中就字符出现的次数并打印
        if mfind < 0 :
            nstr+=i
            #判断出现的次数
            if mconunt > 1 :
                print("重复的字符是:{0} 重复的次数是:{1}".format(i,mconunt))

    # 把下面的klist作为字典的键
    # 同时作为字典的值
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]

    #创建一个列表
    mlist = [i.strip() for i in klist]

    #创建一个set集合
    mset = set(mlist)
    print(mset)

    #创建一个字典
    mdict = {k:k for k in mset}
    print(mdict)

    # 把下面的klist作为字典的键
    # 并统计每个单词的词频

    #创建一个列表
    nlist = [i.strip() for i in klist]
    print(nlist)
    #把列表存入set集合
    nset = {k for k in nlist}
    print(nset)

    #统计每个字母的词频
    ncount = {k:nlist.count(k) for k in nset }
    print(ncount)