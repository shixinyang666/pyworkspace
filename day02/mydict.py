if __name__ == '__main__':
    #创建字典方法一
    mlist = {"name":"张三","password":"321"}
    #创建字典方法二
    mlist2 = dict({"name":"张三","password":"321"})
    #创建字典方法三
    mlist3 = dict(one=1,two=2,three=3)
    #创建字典方法四
    mlist4 = dict([("name","zhangsan"),("password","123")])

    #访问字典 通过键进行访问
    print(mlist3["two"])

    #添加
    mlist["sex"] = "man"
    print(mlist)

    #删除 del
    del mlist3["one"]
    print(mlist3)

    #求字典长度
    mlen = len(mlist)
    print(mlen)

    #把字典变成字符串 type求类型
    mstr = str(mlist)
    print(type(mstr))

    #字典遍历
    for key in mlist :
        print("mlist[{0}] = {0}".format(key,mlist[key]))

    #字典生成式
    nlist = {k:v for k,v in mlist.items()}
    print(nlist)

    #求字典键值对个数
    mlen = len(mlist)
    print(mlen)

    #调用items类型
    miteams = type(mlist.items())
    print(miteams)

    #字典键的类型
    mkey = type(mlist.keys())
    print(mkey)

    #字典值的类型
    mvalue = type(mlist.values())
    print(mvalue)

    #清空
    mclear = mlist3.clear();
    print(mclear)

    #遍历所有字典中的键
    for key in mlist.keys() :
        print(key)

    #遍历字典中的值
    for values in mlist.values() :
        print(values)

    #输出字典中的所有键值对
    for k in mlist :
        print("mlist[{0}] = {1}".format(k,mlist[k]))

    #把键和值添加到字典里
    olist = {}
    key = ["name","password","sex","age"]
    value = ["zhangsan","123","man","18"]

    for k in key :
        olist[k] = value[key.index(k)]

    print(olist)