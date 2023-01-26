num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))
num3 = int(input("enter number 3 :"))
num4 = int(input("enter number 4 :"))
num5 = int(input("enter number 5 :"))
num6 = int(input("enter number 6 :"))
num7 = int(input("enter number 7 :"))
num8 = int(input("enter number 8 :"))
num9 = int(input("enter number 9 :"))
num10 = int(input("enter number 10 :"))
list1 =[]
list1.append(num1)
list1.append(num2)
list1.append(num3)
list1.append(num4)
list1.append(num5)
list1.append(num6)
list1.append(num7)
list1.append(num8)
list1.append(num9)
list1.append(num10)
print(list1)
list2 =[]
for i in list1:
    if i>0:
        list2.append(i)
print(list2)
list3=[]
for i in list1:
    if i<0:
        list3.append(i)
print(list3)
list4 =[]
for i in list1:
    if i%2 !=0:
        list4.append(i)
print(list4)
list5 =[]
for i in list1:
    if i%2 ==0:
        list5.append(i)
print(list5)
for i in set(list1):
    print(list1.count(i))
    

