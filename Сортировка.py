import random
'''
Сортировка пузырьком
    получаем список
    (длина списка) раз
        проходим по парам списка (пара - 2 соседних числа в списке)
            если левое число в паре больше правого
                переставляем их местами в списке
    выводим отсортированный список, кол-во сравнений и кол-во перестановок

Сортировка выбором
    получаем список
    (длина списка) раз
        ищем минимальное число в промежутке счетчик - конец и ставим на место с номером счетчика
        увеличиваем счетчик
    выводим отсортированный список, кол-во поисков минимального числа и кол-во перестановок

Сортировка вставками
    проходим по списку 
        переставляем элемент влево пока он не станет больше левостоящего (точнее сравниваем его с левостоящими пока не найдем меньший)
    выводим отсортированный список, кол-во сравнений и кол-во перестановок
    

Основная часть
    справшиваем про тестовый режим 
        если режим тестовый
            генерируем список из 10 чисел от 0 до 99
            выводим его 
            идем дальше
        иначе
            спрашиваем длинну списка и запоминаем ее
            спрашиваем нужно ли сгенерировать список
                если нет
                    просим ввести список
                    если длина списка неверная 
                        выводим ошибку
                иначе
                    генерируем список данной длины
                    спрашиваем хотит ли пользователь изменити список
                        если да
                            спрашиваем номер изменяемого элемента
                            спрашиваем на что поиенять элемент
                            переносимся к вопросу про изменение списка
                        если нет
                            идем дальше
    если нет ошибок ввода
        производим сортировку 
    иначе 
        выводим ошибку
'''
def mini(list):
    Comparisons=0
    Movings=0
    minim=list[0]
    for i in range(len(list)-1):
        Comparisons+=1
        if list[i+1]<minim:
            minim=list[i+1]
            Movings+=1
    return [minim, Comparisons, Movings]
def sortPuzir(List):
    movings=0
    comparisons=0
    for n in range(len(List)):
        for i in range(len(List)-n-1):
            comparisons+=1
            if List[i]>List[i+1]:
                List[i],List[i+1]=List[i+1],List[i]
                movings+=1
    print("Сортировка пузырьком результат:", *List, "Перестановок:", movings, "Сравнений:", comparisons)

def sortVibor(List):
    movings=0
    comparisons=0
    for i in range(len(List)):
        comparisons+=1
        temporaryVariable, comparisons, movings=mini(List[i:])[0], mini(List[i:])[1]+comparisons, mini(List[i:])[2]+movings
        if List[i]!=temporaryVariable:
            del List[List[i:].index(temporaryVariable)+i]
            List.insert(i, temporaryVariable)
            movings+=1
    print("Сортировка выбором результат:", *List, "Перестановок:", movings, "Сравнений:", comparisons)

def sort3(List):
    movings=0
    comparisons=0
    for i in range(1, len(List)):
        comparisons+=1
        if List[i]<List[i-1]:
            temporaryVariable=List[i]
            del List[i]
            movings+=1
            for j in range(i):
                comparisons+=1
                if List[i-j-2]<temporaryVariable or i-j==1:
                    List.insert(i-j-1, temporaryVariable)
                    break
    print("Сортировка вставками результат:", *List, "Перестановок:", movings, "Сравнений:", comparisons)



danger=False
test=input("Тестовый режим? введите что-то или \"нет\": ")
if test=="нет":
    lenth=int(input("Введите количество чисел: "))
    isListRandom=input("Хотите сгенерировать список, напишите \"да\" или \"нет\": ")
    if isListRandom=="нет" and danger!=True:
        startList=[]
        startStringList=input("Введите числа через пробел: ")
        for x in startStringList.split():
            startList.append(int(x))
        if len(startList)!=lenth:
            danger=True
            print("Неверное количество чисел")
    elif isListRandom=="да" and danger!=True:
        startList = [random.randint(0, 99) for _ in range(lenth)]
        print("Сгенерированный список:", *startList)
        isWantToChange=input("Хотите изменить список? Напишите \"да\" или \"нет\": ")
        if isWantToChange!="да" and isWantToChange!="нет":
            danger=True    
        while isWantToChange=="да" and danger!=True:
            i=int(input("Введите номер изменяемого элемента: "))
            startList[i-1]=int(input("Ведите число: "))
            print("Список:", *startList)
            isWantToChange=input("Хотите изменить список? Напишите \"да\" или \"нет\": ")
    else:
        danger=True
else:
    startList = [random.randint(0, 99) for _ in range(10)]
    print("Список:", startList)
    
if danger!=True:
    startList2=startList.copy()
    startList3=startList.copy()
    sortPuzir(startList)
    sortVibor(startList2)
    sort3(startList3)
else:
    print("Неправильный ввод")
