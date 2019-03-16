if __name__ == '__main__':
    #定义列表
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

    #去掉空格并存入set集合中
    for i in klist :
        mset.add(i.strip())

    # 列表表达式把set集合中的值循环赋给值列表
    mkey = [i for i in mset]

    #列表表达式把set集合中的值循环赋给值列表
    mvalue = [i for i in mset]

    #定义字典 使用列表表达式 把键和值存入字典 方法一
    mdict = {k:v for k in mkey for v in mvalue}

    #循环把建和值存入字典 方法二
    for k in mkey :
         mdict[k] = mvalue[mvalue.index(k)]

    #输出
    print(mdict)

