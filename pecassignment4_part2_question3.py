line1 = int(input("enter your 1st line :"))
line2 = int(input("enter your 2nd line :"))
line3 = int(input("enter your 3rd line :"))
# Checking that the triangle is possible or not.
s = (line1+ line2+line3)/2
if line1 == (line2 +line3):
    print("no, formation of triangle is not possible")
elif line2 == (line1+line3):
    print("no, formation of triangle is not possible")
elif line3 ==(line2 +line1):
    print("no, formation of triangle is not possible")

# now we will find the area of triangle    
elif line1 < (line2 +line3):
    print(f"so by using herons formula \narea of triangle is {(s*(s-line1)*(s-line2)*(s-line3))**(1/2)}")
elif line2 < (line1 +line3):
     print(f"so by using herons formula \narea of triangle is {(s*(s-line1)*(s-line2)*(s-line3))**(1/2)}")
elif line3 < (line2 +line1):
     print(f"so by using herons formula \narea of triangle is {(s*(s-line1)*(s-line2)*(s-line3))**(1/2)}")
else:
    print("no, formation of triangle is not possible")