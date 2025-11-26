ph=''
pm=''
s=input()
c=[]
if len(s)==5:
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
                ph=str(h)+"час"
            elif h%10>1 and h%10<5:
                ph=str(h)+"часа"
            else:
                ph=str(h)+"часов"
            if m%10==0:
                pm="ровно"
            elif m%10==1:
                pm=str(m)+"минута"
            elif m%10>1 and m%10<5:
                ph=str(m)+"минуты"
            else:
                ph=str(m)+"минуты"
