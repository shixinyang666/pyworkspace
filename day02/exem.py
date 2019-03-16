#导入math数学包
import  math
if __name__ == '__main__':
    ###
    #写Python程序判断字符串是否重复
    # ///

    #定义字符串
    mstr = "abcdeabbeadggeghj"
    mlist = ""

    #判断字符串中字母是否重复
        #方法一
    for i in mstr :
        mnum = mlist.find(i)

        if mnum < 0 :
           mlist += i
        else:
            print("字符串是重复的")
            break
        #方法二
    if len(mstr) != len(set(mstr)) :
        print("字符串是重复的")


    #分割线
    print("----------------------------------------------")

    ###
    #编写Python程序打印输出字符串中重复的所有字符
    # ///
    # 定义字符串
    nstr = "abcdeabbeadggeghj"
    nlist = ""

    # 判断字符串中字母是否重复
    for i in nstr:
        ncount = nstr.count(i)
        nnum = nlist.find(i)

        if nnum < 0:
            nlist += i
            if ncount > 1 :
                print("重复的字母为: {0}  重复的次数为: {1}".format(i,ncount))




    #计算平方根
    num2 = math.sqrt(32)
    print(num2)

    print(16**1)
