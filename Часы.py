#Проверка правилности ввода в зависимости от длины
#Если ввод неверный
#    Запоминаем это
#Иначе
#    Идем дальше
#Если длина неверная или при верной длине неверный ввод
#    Выводим сообщение об ошибке
#Иначе
#    Идем дальше
#Разбиваем ввод на часы и минуты, проверяя верность значений
#    Если часы больше 23 или меньше 0 или минуты больше 59 или меньше 0
#        Выводим ошибку
#Проверяем является ли время полночью или полднем
#    Если минуты равны 0 и часы равны 0 или 12
#        Выводим полночь или полдень соотвецтвенно
#    Иначе
#        Определяем как нужно склонять часы и минуты
#            Если кол-во минут == 0
#                В конце вывода пишем "ровно"
#            Если остаток от деления числа на 10 == 0 или >4 или число делить на 10 == 1
#                Часов или минут
#            Если остаток от деления числа на 10 == 1 
#                Час или минута
#            Если остаток от деления числа на 10 >= 2 и <=4
#                Часа или минуты
#        Определяем часть суток
#            Если часы делить на 6 == 0, 1, 2 или 3
#                Запоминаем время суток как ночь, утро, день или вечер
#    Если колво минут не == 0
#        Выводим часы и минуты, с правильным склонением, и часть суток
#    Иначе
#        Выводим часы, с правильным склонением, часть суток и "ровно"
def antiError(string):
    danger=False
    isSpaceBefore=""
    if len(string)==5:
        for i in range(len(string)):
            if i==2:
                if string[2]!=":" and string[2]!=" ":
                    danger=True
            else:
                if not string[i].isdigit():
                    danger=True
    elif len(string)==3:
        for i in range(len(string)):
            if i==1:
                if string[1]!=":" and string[1]!=" ":
                    danger=True
            else:
                if not string[i].isdigit():
                    danger=True
    elif len(string)==4:
        for i in range(len(string)):
            if string[1].isdigit():
                isSpaceBefore=False
            elif string[1]==" " or string[1]==":":
                isSpaceBefore=True
            else:
                danger=True
            if isSpaceBefore==True:
                if i!=1 and not string[i].isdigit():
                    danger=True
            elif isSpaceBefore==False:
                if i==2:
                    if string[2]!=":" and string[2]!=" ":
                        danger=True
                else:
                    if not string[i].isdigit():
                        danger=True
    return(danger)

def timeIdentification(hours, minutes):
    printHours=""
    printMinute=""
    time=""
    
    if hours%12==1:
        printHours=str((hours-1)%12+1)+" час "
    elif hours%12>1 and hours%12<5:
        printHours=str((hours-1)%12+1)+" часа "
    else:
        printHours=str((hours-1)%12+1)+" часов "
    
    if minutes==0:
        printMinute=" ровно"
    elif minutes%10==1 and minutes//10!=1:
        printMinute=str(minutes)+" минута "
    elif minutes%10>1 and minutes%10<5 and minutes//10!=1:
        printMinute=str(minutes)+" минуты "
    else:
        printMinute=str(minutes)+" минут "
    
    if hours//6==0:
        time="ночи"
    elif hours//6==1:
        time="утра"
    elif hours//6==2:
        time="дня"
    else:
        time="вечера"
    
    if printMinute==" ровно":
        return(printHours+time+printMinute)
    else:
        return(printHours+printMinute+time)

string=input("Введите время: ")
emptyList=[]

danger=antiError(string)

string=string.replace(":", " ")

if (len(string)==5 or len(string)==4 or len(string)==3) and danger==False:
    for x in string.split():
        emptyList.append(int(x))
    hours=emptyList[0]
    minutes=emptyList[1]
    
    if hours>23 or hours<0:
        print("Введены некорректные данные, часы должны быть от 0 до 23 включительно")
    elif minutes>59 or minutes<0:
        print("Введены некорректные данные, минуты должны быть от 0 до 59 включительно")
    else:
        if hours==12 and minutes==0:
            print("полдень")
        elif hours==0 and minutes==0:
            print("полночь")
        else:
            printing=timeIdentification(hours, minutes)
            print(printing)
else:
    print("Введены некорректные данные, данные должны быть в формате: <число от 0 до 23> <пробел или двоеточие> <число от 0 до 59>")
