import random
#
#
#
#
#
#
#
#
#
#
#
#
#
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
    #return(List)

def sortVibor(List):
    movings=0
    comparisons=0
    for i in range(len(List)):
        comparisons+=1
        if List[i]!=min(List[i:]):
            temporaryVariable=min(List[i:])
            List.remove(min(List[i:]))
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
    #return(List)



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
            startList[i-1]==int(input("Ведите число: "))
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
