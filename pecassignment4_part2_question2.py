num = int(input(" Enter a number : "))
range1 = int(input("Enter lower limit range : "))
range2 = int(input("Enter upper limit range : "))
for i in range(range1,range2 +1):
    if i ==0:
        continue
    if i%num ==0 :
        print(i)
    else:
        continue