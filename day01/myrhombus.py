if __name__ == '__main__':
    i = 1
    while i <= 5 :
        j = 1
        while j <= i :

            print("*", end="")
            j += 1

        print("\n")
        i+=1

    i = 5
    while i >= 1:
        j = 1
        while j <= i:
            print("*", end="")
            j += 1
        print("\n")
        i -= 1


    a = int(input(">>>"))
    c=a
    b=a
    for i in range(1,a+1):
        print(" "*(c-1),"*"*(2*i-1))
        c=c-1
    if(i==a):
        for y in range(1,a):
            print(" "*y,"*"*(2*b-3))
            b = b -1

