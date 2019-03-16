if __name__ == '__main__':
    #简单列表生成式创建一个列表
    mlist = [i for i in range(1,11)]
    print(mlist)

    #复合列表生成式——1-10的平方
    mnum = [i**2 for i in range(1,11)]
    print(mnum)

    # 复合列表生成式——判断偶数1-10的平方
    mnum1 = [i ** 2 for i in range(1, 11) if i % 2 ==0]
    print(mnum1)

    #复合列表生成式遍历
    nlist = [i for i in mlist if i % 2 ==0]
    print(nlist)

    #复合列表生成式——笛卡尔积
    olist = [1,2,3]
    plist = ["a","b","c"]
    qlist = [str(i)+j for i in olist  for j in plist]
    print(qlist)

    # 复合列表生成式——笛卡尔积加if判断
    olist1 = [1, 2, 3]
    plist1 = ["a", "b", "c"]
    qlist1 = [str(i) + j for i in olist1 for j in plist1 if i % 2 ==1 ]
    print(qlist1)

    #把一个列表中所有的字符串变成小写
    slist = ["Abc","DEF","ghi",123,456,789]
    slower = [i.lower() for i in slist if str==type(i)]
    print(slower)




