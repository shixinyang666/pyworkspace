if __name__ == '__main__':
    #1.	编写Python程序判断字符串是否重复

    #定义字符串
    mstr = "abcdeabdegghka"
    #判断将字符串存入set集中后再比较长度 如果长度一致 那么就不是重复的字符串 反之如此
    if len(mstr) != len(set(mstr)) :
        print("是重复的字符串")

    #2.	编写Python程序打印输出字符串中重复的所有字符

    #定义子字符串

    nstr = ""
    for i in mstr :
        #获取字符在字符串中出现的次数
        mcount = mstr.count(i)
        #判断字符串是否在子字符串中
        mfind = nstr.find(i)
        if mfind < 0 :
            nstr+=i
            if mcount > 1 :
                print("重复的字符是: {mstr} 重复的次数是: {mcount}".format(mstr=i,mcount=mcount))


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

    #定义set集合
    mset = set()
    #把klist中的元素去空格并存入set集合中去重
    for k in klist :
            mset.add(k.strip())

    #创建一个键列表
    mlist = [k for k in mset]

    #创建一个字典并存入键值对
    mdict = {k:k for k in mlist  }
    print(mdict)

    # 4. 统计每个单词的词频

    #创建一个列表
    nlist = []

    #去掉列表中字符串中的空格
    for i in klist :
        nlist.append(i.strip())

    print(nlist)

    # 创建一个set集合
    nset = set(nlist)
    print(nset)

    #统计每个单词的词频
    for k in nset :
        #统计单词出现的次数
        ncount = nlist.count(k)
        #输出
        print("列表中的单词:{nlist} 出现了{ncount}次 ".format(nlist=k,ncount=ncount))