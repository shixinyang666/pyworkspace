#导入随机序列
import  random
#定义判断性别输出函数
def checkSex (name,sex) :
    #判断性别并输出
    if sex=="man" or sex=="男" :
        print("{0}先生您好!".format(name))
    else:
        print("{0}女士您好!".format(name))

#随机生成两个分别包含10和15个整数的列表，并计算输出两个列表的并集
def randomNum() :
    #随机生成连个分别包含10个和15个整数的列表
    mlist = [random.randint(1,10) for i in range(1,10)]
    mlist2 = [random.randint(1,15) for i in range(1,15)]
    #把两个列表存入集合
    mset1 = set(mlist)
    mset2 = set(mlist2)
    #求两个列表中的并集 并存入列表
    minter = mset1 | mset2
    mlist3 = [i for i in minter]
    print("两个列表中的并集为:{0}".format(mlist3))

#注意一个用户信息，包含EMAIL号，判断信息是否合法，如果合法则输出相关信息（姓名长度不能少于6位，邮件中包含@）
def email(myemail) :
    #先判断长度
    if len(myemail) > 6:
        #判断输入的email号中是否有@符号
        if str(myemail).find("@") > -1 :
            print("email邮箱格式正确")
        else:
            print("email邮箱格式不正确")
    else:
        print("email长度必须大于6位")
#从键盘输入一行字符串，判断是否是回文数
def huistr(mystr) :
    print(type(mystr))
    #判断字符串的长度是奇数还是偶数
    if len(mystr) % 2 == 0 :
        #分割字符串
        mlstr = mystr[0:len(mystr)//2]
        mrstr = mystr[len(mystr)//2:]
        mrstr2 = mrstr[::-1]

        #判断是否是回文字符串
        if mlstr == mrstr2 :
            print("是回文字符串")
        else:
            print("不是回文字符串")
    else :
        # 分割字符串
        mlstr = mystr[0:len(mystr) // 2]
        mrstr = mystr[len(mystr) // 2+1:]
        mrstr2 = mrstr[::-1]

        # 判断是否是回文字符串
        if mlstr == mrstr2:
            print("是回文字符串")
        else:
            print("不是回文字符串")

