if __name__ == '__main__':
    #1.判断字符串是否是重复的
    mstr = "abcdeffgabcaabbeeffgahhl"
    nstr = ""
    #判断字符串长度 和 存入set集合后的长度 是否相等
    if len(mstr) != len(set(mstr)) :
        print("字符串是重复的!")

    #2.把重复的字符打印出来
        for i in mstr :
            #统计当前元素在字符串中出现了多少次
            mcount = mstr.count(i)
            #判断字符串是否在子字符串中 如果不在返回-1
            mfind = nstr.find(i)
            #判断下标是否小于0 ，假如小于0就把这个字符存入子字符串中
            if mfind < 0 :
                nstr+=i
                #判断字符在字符串中是否出现1次以上
                if mcount > 1 :
                    print("重复的字符是: {0}  重复的次数是: {1}".format(i,mcount))

    #3.把下面的klist作为字典的键，并统计每个单词的词频
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

    #定义一个新列表
    mlist = []
    #循环把空格去除并存入新列表
    for i in klist :
        mlist.append(i.strip())

    #把新列表存入set集合中去重 获取键
    mset = set(mlist)

    mdict = dict()
    #循环统计键在列表中出现的次数 并存入字典
    for k in mset :
        #统计出现的次数
        mnum = mlist.count(k)
        #存入字典中
        mdict[k] = mnum

    print(mdict)

