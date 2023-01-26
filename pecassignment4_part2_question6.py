num = int(input("enetr the lower bound of the range : "))
num2 = int(input("enetr the upper bound of the range : "))
for i in range(num,num2+1):
    prime = True
    if i ==0 or i ==1:
        prime = False
    elif i>1:    
        for j in range(2,i):
            if i %j==0:
                prime = False
                break
            else:prime=True
    if prime == True:
        print(i)
                 
        
            
    
    
        
    

    
    
        
     