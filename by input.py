#14. Write a program to input basic salary of an employee and calculate its Gross salary according to following:
#BasicSalary <= 10000 : HRA = 20%, DA = 80%
#BasicSalary <= 20000 : HRA = 25%, DA = 90%
#BasicSalary > 20000 : HRA = 30%, DA = 95%
#gross salary = basic_salary + hra + da
basic_salary = float(input("Enter basic salary: "))

if basic_salary <= 10000:
    hra = basic_salary * 20 / 100
    da = basic_salary * 80 / 100

elif basic_salary <= 20000:
    hra = basic_salary * 25 / 100
    da = basic_salary * 90 / 100

else:
    hra = basic_salary * 30 / 100
    da = basic_salary * 95 / 100

gross_salary = basic_salary + hra + da

print("Gross Salary =", gross_salary)

#Write a program to print day of week name using switch case
day = int(input("Enter day number (1-7): "))

days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

if day in days:
    print(days[day])
else:
    print("Invalid day number")

#Write a program to print all natural numbers from 1 to n. - using while loop
n = int(input("Enter n: "))

i = 1

while i <= n:
    print(i, end=" ")
    i = i + 1     

#write a program to print all natural numbers in reverse (from n to 1). - using while loop
n = int(input("Enter n: ")) 
i = n
while i >= 1:
    print(i, end=" ")
    i = i - 1 

#write a program to print all alphabets from a to z. - using while loop
i = ord('a')
while i <= ord('z'):
    print(chr(i), end=" ")
    i = i + 1
#write a program to print all alphabets from z to a. - using while loop
i = ord('z')    
while i >= ord('a'):
    print(chr(i), end=" ")
    i = i - 1
#write a program to print all even numbers between 1 to 100. - using while loop
i = 1   
while i <= 100:
    if i % 2 == 0:
        print(i, end=" ")
    i = i + 1
#write a program to print all odd numbers between 1 to 100. - using while loop
i = 1       
while i <= 100:
    if i % 2 != 0:
        print(i, end=" ")
    i = i + 1
   
