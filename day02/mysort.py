import random
if __name__ == '__main__':
    # #定义列表
    mnum = [1,2,3,4,5,6,7,8,9]
    #打乱列表
    random.shuffle(mnum)
    print(mnum)
    #sort排序  加上reverse=True 就是倒序 默认False升序
    mnum.sort(reverse=True)
    #输出
    print(mnum)

    #定义列表
    mstu = ["张学友", "刘德华", "成龙", "洪金宝"]
    mstu.sort()
    print(mstu)

    #定义列表
    mnum = [1,2,3,4,5,6,7,8,9,10]
    #打乱
    random.shuffle(mnum)
    print(mnum)
    #sorted排序 是临时排序不会对原数据源做出改变，
    #只改变这一次 可以通过返回排序后的数据源查看结果
    print(sorted(mnum,reverse=True))
    #清空表
    mnum.clear()
    print(mnum)

