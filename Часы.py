ph=''
pm=''
vr=""
s=input()
c=[]
if len(s)==5 or len(s)==4:
    for x in s.split():
        c.append(int(x))
    h=c[0]
    m=c[1]
    if h>23 or h<0 or m>59 or m<0:
        print("неправильный ввод")
    else:
        if h==12 and m==0:
            print("полдень")
        elif h==0 and m==0:
            print("полночь")
        else:
            if h%10==1:
                ph=str((h-1)%12+1)+" час "
            elif h%10>1 and h%10<5:
                ph=str((h-1)%12+1)+" часа "
            else:
                ph=str((h-1)%12+1)+" часов "
            if m%10==0:
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
