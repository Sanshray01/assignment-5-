Alphabet = 'ABCDEFGHIJLMNOPQRST'
alphabet1 = list(map(str,Alphabet))
ran =  int(input("Enter rows : "))
a = 0
b = 1
letter = ((ran)*(ran+1))//2
if letter >26:
    Alphabet = (letter//26) +1
alphabet1 = list(map(str,Alphabet))
for i in range(ran):
    b = a+i +1
    print(Alphabet[a:b])
    a+=i+1