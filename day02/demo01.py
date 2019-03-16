if __name__ == '__main__':
    #创建列表的两种方法
    mlist = []
    mlist2 = list()
    #输出列表类型
    print(type(mlist))
    print(type(mlist2))

    #第一种添加方式
    mlist.append("张三")
    print(mlist)
    #第二种添加方法
    mlist.insert(0,"李四")
    print(mlist)
    #insert添加 如指定索引不存在就在列表的最后面添加元素
    mlist.insert(5,"赵六")
    print(mlist)
    #列表删除 pop删除 通过下标索引
    print(mlist.pop(2))
    print(mlist)

    #列表删除 del删除 可以通过下标索引删除元素 也可以不写下标删除列表
    del mlist[0]
    print(mlist)

    #列表删除 remove删除 指定元素
    mlist.remove("张三")
    print(mlist)

    arr = range(1,101)
    for i in arr :

        print(str(i).rjust(4),end=" ")

        if i % 10 ==0 :
            print()
