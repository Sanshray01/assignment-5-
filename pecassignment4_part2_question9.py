lines = int(input("enter number of words you want to enter : "))
list1 = []
for i in range(lines):
    list1.append(input("enter a word :"))
for i in set(list1):
    print(list1.count(i))

