#Учитывая массив целых чисел в виде строк и чисел, верните сумму значений массива, как если бы все они были числами. Верните свой ответ в виде числа.

def sum_mix(arr):
    #your code here
    result = 0
    for i in arr:
        i = int(i)
        result += i
    print(result)

sum_mix([9, 3, '7', '3']) #22
sum_mix(['5', '0', 9, 3, 2, 1, '9', 6, 7]) #42