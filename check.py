#Write a program to check whether a number is negative, positive or zero.
number=int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Write a program to check whether a number is divisible by 5 and 11 or not.
number=int(input("enter a number:"))
if number%5==0 and number%11==0:
  print("number is divisible by 5 and 11")
else:
  print("number is not divisible by 5 and 11")

#Write a program to check whether a number is even or odd.
number=int(input("Enter a number: "))
if number%2==0:
    print("The number is even.")
else:
    print("The number is odd.")

#Write a program to check whether a year is leap year or not.
year=int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")

#Write a program to check whether a character is an alphabet or not.
ch=input("enter the character:")
if (ch>="A" and ch<="Z") or (ch>="a" and ch<="z"):
  print("it lies in the character")
else:
  print("does not lies in the character:")

#Write a program to input any alphabet and check whether it is vowel or consonant.
ch=input("enter the character:")
if ch in "aeiouAEIOU":
    print("it is a vowel")
else:
    print("it is a consonant")

#Write a program to input any character and check whether it is alphabet, digit or special character.
ch=input("enter the character:")
if (ch>="a" and ch<="z") and (ch>="A" and ch<="Z"):
  print("it is alphabet")
elif ch.isdigit():
  print("it is digit")
else:
  print("special character")

#Write aprogram to check whether a character is uppercase or lowercase alphabet.
ch=input("enter the character:")
if  (ch>="A" and ch<="Z"):
  print("UPPER CASE")
elif (ch>="a" and ch<="z"):
  print("lower case")
else:
  print("other character")

#Write a program to input week number and print week day    
week = int(input("Enter week number (1-7): "))

if week == 1:
    print("Monday")
elif week == 2:
    print("Tuesday")
elif week == 3:
    print("Wednesday")
elif week == 4:
    print("Thursday")
elif week == 5:
    print("Friday")
elif week == 6:
    print("Saturday")
elif week == 7:
    print("Sunday")
else:
    print("Invalid week number")    