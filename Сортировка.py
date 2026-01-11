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
    n=1
def sortVibor(List):
    printingList=[]
    printingList.append(min(List))
    List.remove(min(List))
def sort3(List):
    n=1


danger=False
lenth=int(input("Введите количество чисел: "))
isListRandom=input("Хотите сгенерировать список, напишите \"Да\" или \"Нет\":" )
if isListRandom!="Да" and isListRandom!="Нет":
    danger=True
if isListRandom=="Нет" and danger!=True:
    startList=[]
    startStringList=input("Введите числа через пробел")
    for x in startStringList.split():
        startList.append(int(x))
    if len(startList)!=lenth:
        danger=True
        print("Неверное количество чисел")
else:
    startList = [random.randint(0, 99) for _ in range(lenth)]
    print(*startList)
    isWantToChange=input("Хотите изменить список? Напишите \"Да\" или \"Нет\":")
    while isWantToChange=="Да" and danger!=True:
        i=int(input("Введите номер изменяемого элемента: "))
        startList[i-1]==int(input("Ведите число: "))
        print(*startList)
        isWantToChange=input("Хотите изменить список? Напишите \"Да\" или \"Нет\":")
    if isWantToChange!="Да" and isWantToChange!="Нет":
        danger=True

        
