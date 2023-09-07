#Factorial of a number
a=int(input("enter the number:"))#Reads number
fact=1
for i in range (1,a+1):
    fact=fact*i
    print("factorial of",a,"is",fact)
    
