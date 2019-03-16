if __name__ == '__main__':
    #创建set集合的第一种方法 在用大括号创建时 括号内至少写一位元素否则创建的是一个字典
    mset1 = {1}
    #创建set集合的第二种方法
    mset2 = set()
        #输出
    print(type(mset1))
    print(type(mset2))

    #成员检测 in not in
    nset = {1,2,3,4,5,6,1,2,4,6}
    nset2 = {2,3,4}
    if nset2 in nset :
        print("子集合在集合里")

    if nset2 not in nset :
        print("子集合不在集合里")

    #排除重复
    nset3 = {i for i in nset }
    print(nset3)


    # 或运算 | 求两个集合中的并集
    mnum = {1, 2, 3, 3, 5, 5, 6}
    nnum = {4, 7, 8, 0, 9, 9, 4}

    snum = mnum | nnum
    print(snum)

    # 与运算 & 求两个集合中的交集
    mnum1 = {1, 2, 3, 3, 5, 5, 6}
    nnum1 = {4, 7, 8, 9,3,6}

    snum1 = mnum1 & nnum1
    print(snum1)

    # 差运算 - 求两个集合中的差集
    mnum2 = {1, 2, 3, 3,4, 4, 5}
    nnum2 = {7,9,8,3,4}

    snum2 = nnum2 - mnum2
    print(snum2)

    # 将连个集合中的并集中的交集部分去掉
    mnum3 = {1, 2, 3, 3, 4, 4, 5}
    nnum3 = {7, 9, 8, 3, 4}

    snum3 = nnum3 ^ mnum3
    print(snum3)

    #len方法 求长度
    mlen = len(mnum3)
    print(mlen)

    #max()方法 求集合中的最大值
    mmax = max(mnum3)
    print(mmax)

    #min()方法 求集合中的最大值
    mmin = min(mnum3)
    print(mmin)

    #add方法 向集合添加元素
    mnum3.add(0)
    print(mnum3)

    #update方法 修改集合中的元素
    mnum3.update({99,88,77})
    print(mnum3)

    #copy复制 将一个集合复制到另一个集合
    ostr = {1,4,7,8,5,2,3,6,9,4,7,1,9,6,3}
    pstr = ostr.copy()
    print(pstr)

    #清空
    mnum2.clear()
    print(mnum2)


    lnum1 = {1, 2, 3, 3, 5, 5, 6}
    lnum2 = {4, 7, 8, 9, 3, 6}
    # 集合中的并集 第一种方法
    lunion = lnum1.union(lnum2)
    print(lunion)
    # 集合中的并集 第二种方法
    lunion2 = lnum1 | lnum2
    print(lunion2)

    #集合中交集 第一种方法
    lintersection = lnum1.intersection(lnum2)
    print(lintersection)

    # 集合中交集 第二种方法
    lintersection2 = lnum1 & lnum2
    print(lintersection2)

    #集合中的差集 第一种方法
    ldifference = lnum1.difference(lnum2)
    print(ldifference)

    # 集合中的差集 第二种方法
    ldifference2 = lnum1 - lnum2
    print(ldifference2)