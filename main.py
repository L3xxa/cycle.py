#1
# a=int(input("Введіть перше число: "))
# b=int(input("Введіть друге число: "))
# for i in range(a,b+1):
#     if(i%7==0):
#         print(i)
#

#2
# a=int(input("Введіть перше число: "))
# b=int(input("Введіть друге число: "))
# par=int(input("Виберіть що ви хочете вивести\n1-Всі числа діапазону\n2-Всі числа діапазону в спадному порядку\n3-Всі числа, кратні 7\n4-Кількість чисел, кратних 5\n: "))
# if (a<b):
#     start=a
#     finish=b
# else:
#     start = b
#     finish = a
# if (par==1):
#     for i in range(start,finish+1):
#         print(i)
# elif (par==2):
#     for i in range(finish,start-1,-1):
#         print(i)
# elif (par==3):
#     for i in range(start,finish+1):
#         if (i%7==0):
#             print(i)
# elif (par==4):
#     c=0
#     for i in range(start, finish + 1):
#         if (i%5==0):
#             c+=1
#     print("Кількість чисел, кратних 5:",c)


# 3
# a=int(input("Введіть перше число: "))
# b=int(input("Введіть друге число: "))
# if (a<b):
#     start=a
#     finish=b
# else:
#     start = b
#     finish = a
# for i in range(start,finish+1):
#     if (i%5==0)and(i%3==0):
#         print(i, "-Fizz_Buzz")
#     elif (i%5==0):
#         print(i,"-Buzz")
#     elif (i%3==0):
#         print(i, "-Fizz")
#     elif (i%3!=0)and(i%5!=0):
#         print(i,)
