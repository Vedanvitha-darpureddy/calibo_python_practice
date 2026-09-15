#Write a program to find maximum between two numbers.
n1=int(input("Enter first number: "))
n2=int(input("Enter second number: ")) 
if n1>n2:
    print(n1,"is maximum")        
else:
    print(n2,"is maximum")          
#Write a program to find maximum between three numbers
n1=int(input("enter a number"))
n2=int(input("enter a number"))
n3=int(input("enter a number"))
if n1>n2 and n1>n3:
    print(n1,"is the largest number")
elif n2>n1 and n2>n3:
    print(n2,"is the largest number")
else:
    print(n3,"is the largest number")      