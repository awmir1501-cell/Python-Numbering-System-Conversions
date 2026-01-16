def binary(num):
    num=int(num)
    list=[]
    n=0
    while(num>0):
        n=num%2
        list.append(str(n))
        num=int(num/2)
    list=list[::-1]
    print("".join(list))
def octal(num):
    num=int(num)
    list=[]
    while(num>0):
        n=num%8
        list.append(str(n))
        num=int(num/8)
    list=list[::-1]
    print("".join(list))
def hexal(num):
    num=int(num)
    list=[]
    while(num>0):
        n=num%16
        if(n==10):
            list.append("A")
        elif(n==11):
            list.append("B")
        elif(n==12):
            list.append("C")
        if(n==13):
            list.append("D")
        elif(n==14):
            list.append("E")
        elif(n==15):
            list.append("F")
        if(n<10):
            list.append(str(n))
        num=int(num/16)
    list=list[::-1]
    print("".join(list))
def binTOdec(num):
    list=[]
    sum=0
    for i in range(len(num)):
        list.append(int(num[i]))
    list=list[::-1]
    for i in range(len(list)):
        n=0
        list[i]=list[i]*(2**i)
        n=list[i]
        sum+=n
    return sum
def binTOoc(num):
    list=[]
    sum=0
    while(len(num)%3!=0):
        num="0"+num
    for i in range(len(num)):
        list.append(int(num[i]))
    for i in range(0,len(list),3):
        temp2=0
        n=0
        n=list[i:3+i]
        n=n[::-1]
        for j in range(len(n)):
            temp=0
            temp=n[j]*(2**j)
            temp2+=temp
        print(temp2,end="")
def binTOhex(num):
    list=[]
    sum=0
    while(len(num)%4!=0):
        num="0"+num
    for i in range(len(num)):
        list.append(int(num[i]))
    for i in range (0,len(list),4):
        temp2=0
        n=list[i:4+i]
        n=n[::-1]
        for j in range(4):
            temp=0
            temp=n[j]*(2**j)
            temp2+=temp
        if(temp2==10):
            print("A",end="")
        elif(temp2==11):
            print("B",end="")
        elif(temp2==12):
            print("C",end="")
        elif(temp2==13):
            print("D",end="")
        elif(temp2==14):
            print("E",end="")
        elif(temp2==15):
           print("F",end="")
        if(temp2<10):
            print(temp2,end="")
def octTodec(num):
    temp=0
    temp2=0
    i=0
    num=int(num)
    while(num>0):
        temp=int(num%10)
        temp2+=int(temp*(8**i))
        num=num/10
        i=i+1
    return temp2
def octTObin(num):
    num=int(num)
    temp=0
    temp2=[]
    while(num>0):
        temp=int(num%10)
        while(temp>0):
            temp2.append(int(temp%2))
            temp=int(temp/2)
        num=int(num/10)
    temp2=temp2[::-1]
    return(temp2)
def hexTodec(num):
    list=[]
    temp=0
    for i in num:
        list.append(i)
    for i in range(len(list)):
        if (list[i]=="A"or list[i]=="a"):
            list[i]=10
        elif (list[i]=="B"or list[i]=="b"):
            list[i]=11
        elif (list[i]=="C"or list[i]=="c"):
            list[i]=12
        elif (list[i]=="D"or list[i]=="d"):
            list[i]=13
        elif (list[i]=="E"or list[i]=="e"):
            list[i]=14
        elif (list[i]=="F"or list[i]=="f"):
            list[i]=15
        else:
            list[i]=int(list[i])
    list=list[::-1]
    for i in range (len(list)):
        temp+=list[i]*(16**i)
    return temp
def hexTObin(num):
    list=[]
    for i in num:
        list.append(i)
    for i in range(len(list)):
        if (list[i]=="A" or list[i]=="a"):
            list[i]=10
        elif (list[i]=="B"or list[i]=="b"):
            list[i]=11
        elif (list[i]=="C"or list[i]=="c"):
            list[i]=12
        elif (list[i]=="D"or list[i]=="d"):
            list[i]=13
        elif (list[i]=="E"or list[i]=="e"):
            list[i]=14
        elif (list[i]=="F"or list[i]=="f"):
            list[i]=15
        else:
            list[i]=int(list[i])
    temp=[]
    list=list[::-1]
    for i in range(len(list)):
        while(list[i]>0):
            temp.append(int(list[i]%2))
            list[i]=int(list[i]/2)
    temp=temp[::-1]
    return(temp)    
ch="y"
while(ch=='y' or ch=="Y"):
    print("1. Decimal")
    print("2. Binary")
    print("3. Octal")
    print("4. HexaDecimal")
    conv=int(input("Enter which number you want to enter: "))
    num=input("Enter your number : ")
    if(conv==1):
        print(num," in Base 2 = ",end="")
        binary(num)
        print(num," in Base 8 = ",end="")
        octal(num)
        print(num," in Base 16 = ",end="")
        hexal(num)
    elif(conv==2):
        print(num," in Base 10 = ",binTOdec(num),end="")
        print()
        print(num," in Base 8 = ",end="")
        binTOoc(num)
        print()
        print(num," in Base 16 = ",end="")
        binTOhex(num)
        print()
    elif(conv==3):
        print(num," in Base 2 = ",octTObin(num))
        print(num," in Base 10 = ",octTodec(num))
        a=octTodec(num)
        b=str(a)
        print(num," in Base 16 = ",end="")
        hexal(b)
        print()
    elif(conv==4):
        print(num," in Base 2 = ", hexTObin(num))
        print(num," in Base 10 = ",hexTodec(num))
        a=hexTodec(num)
        b=str(a)
        print(num," in Base 16 = ",end="")
        octal(b)
        print()
    else:
        print("Wrong choice!")
        print("1. Decimal")
        print("2. Binary")
        print("3. Octal")
        print("4. HexaDecimal")
        conv=int(input("Enter which number you want to convert: "))
    ch=input("Do you want to continue (Y/N): ")
  
