#导入随机序列
import  random
if __name__ == '__main__':
    ###
    # 列表排序、反选
    # ///

    # 创建一个列表
    mlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    #打乱列表
    random.shuffle(mlist)
        #输出
    print(mlist)

    #第一种排序方法 sort() 此方法排序是永久排序直接对数据源做出改变
    # 在sort括号中 可添加reverse=True 进行反转完成降序排列 如果不写默认reverse=false 为升序
    mlist.sort(reverse=True)
        #输出
    print(mlist)

    # 第二种排序方法 sorted() sorted是临时排列 仅对数据源进行一次排序不会对数据源做出永久修改

    #打乱列表
    random.shuffle(mlist)
        #输出
    print(mlist)

    #用sorted方法排序
        #输出
    print(sorted(mlist,reverse=True))


