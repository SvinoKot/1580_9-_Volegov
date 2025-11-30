ph=''
pm=''
vr=""
s=input()
c=[]
danger=False
do=""
if len(s)==5:
    for i in range(len(s)):
        if i==2:
            if s[2]!=":" and s[2]!=" ":
                danger=True
        else:
            if not s[i].isdigit():
                danger=True
elif len(s)==3:
    for i in range(len(s)):
        if i==1:
            if s[1]!=":" and s[1]!=" ":
                danger=True
        else:
            if not s[i].isdigit():
                danger=True   
elif len(s)==4:
    for i in range(len(s)):
        if s[1].isdigit():
            do=False
        elif s[1]==" " or s[1]==":":
            do=True
        else:
            danger=True
        if do==True:
            if i!=1 and not s[1].isdigit():
                danger=True
        else:
            if i==2:
                if s[2]!=":" and s[2]!=" ":
                    danger=True
            else:
                if not s[i].isdigit():
                    danger=True
s=s.replace(":", " ")            
if (len(s)==5 or len(s)==4 or len(s)==3) and danger==False:
    for x in s.split():
        c.append(int(x))
    h=c[0]
    m=c[1]
    if h>23 or h<0:
        print("Введены некорректные данные, часы должны быть от 0 до 23 включительно")
    elif m>59 or m<0:
        print("Введены некорректные данные, минуты должны быть от 0 до 59 включительно")
    else:
        if h==12 and m==0:
            print("полдень")
        elif h==0 and m==0:
            print("полночь")
        else:
            if h%12==1:
                ph=str((h-1)%12+1)+" час "
            elif h%12>1 and h%12<5:
                ph=str((h-1)%12+1)+" часа "
            else:
                ph=str((h-1)%12+1)+" часов "
            if m==0:
                pm=" ровно "
            elif m%10==1 and m//10!=1:
                pm=str(m)+" минута "
            elif m%10>1 and m%10<5 and m//10!=1:
                pm=str(m)+" минуты "
            else:
                pm=str(m)+" минут "
            if h//6==0:
                vr="ночи "
            elif h//6==1:
                vr="утра "
            elif h//6==2:
                vr="дня "
            else:
                vr="вечера"
        print(ph+pm+vr)
else:
    print("Введены некорректные данные, данные должны быть в формате: <число от 0 до 23> <пробел или двоеточие> <число от 0 до 59>")
