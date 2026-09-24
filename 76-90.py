# 75. Write a Python program to find lowest frequency character in a string

string = input("Enter a string: ")

frequency = {}

for ch in string:
    if ch != " ":
        frequency[ch] = frequency.get(ch, 0) + 1

lowest = min(frequency.values())

for ch in string:
    if ch != " " and frequency[ch] == lowest:
        print("Lowest frequency character:", ch)
        break


# 76. Write a Python program to count frequency of each character in a string

string = input("Enter a string: ")

frequency = {}

for ch in string:
    frequency[ch] = frequency.get(ch, 0) + 1

for ch, count in frequency.items():
    print(ch, ":", count)


# 77. Write a Python program to create a file and write contents, save and close the file

file = open("sample.txt", "w")

file.write("Hello, this is a sample file.\n")
file.write("Python file handling is easy.")

file.close()

print("File created successfully.")


# 78. Write a Python program to read file contents and display on console

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()


# 79. WAP to read numbers from a file and write even, odd and prime numbers to separate files

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


numbers = input("Enter numbers separated by spaces: ")

with open("numbers.txt", "w") as file:
    file.write(numbers)

with open("numbers.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

with open("even.txt", "w") as even_file:
    with open("odd.txt", "w") as odd_file:
        with open("prime.txt", "w") as prime_file:

            for num in numbers:

                if num % 2 == 0:
                    even_file.write(str(num) + " ")

                else:
                    odd_file.write(str(num) + " ")

                if is_prime(num):
                    prime_file.write(str(num) + " ")

print("Numbers written to separate files.")


# 80. Write a Python program to copy contents from one file to another file

source = "sample.txt"
destination = "copy.txt"

with open(source, "r") as file:
    content = file.read()

with open(destination, "w") as file:
    file.write(content)

print("File copied successfully.")


# 81. Write a Python program to merge two files into third file

file1 = "file1.txt"
file2 = "file2.txt"
file3 = "merged.txt"

with open(file1, "w") as file:
    file.write("This is the first file.\n")

with open(file2, "w") as file:
    file.write("This is the second file.\n")

with open(file1, "r") as f1:
    content1 = f1.read()

with open(file2, "r") as f2:
    content2 = f2.read()

with open(file3, "w") as f3:
    f3.write(content1)
    f3.write(content2)

print("Files merged successfully.")


# 82. Write a Python program to count characters, words and lines in a text file

with open("sample.txt", "r") as file:
    content = file.read()

characters = len(content)
words = len(content.split())
lines = len(content.splitlines())

print("Characters:", characters)
print("Words:", words)
print("Lines:", lines)


# 83. WAP to check whether a number is prime, Armstrong or perfect number using functions

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == n


def is_perfect(n):
    if n <= 1:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


n = int(input("Enter a number: "))

print("Prime:", is_prime(n))
print("Armstrong:", is_armstrong(n))
print("Perfect:", is_perfect(n))


# 84. WAP to find all prime numbers between given interval using functions

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    if is_prime(n):
        print(n, end=" ")


# 85. WAP to print all strong numbers between given interval using functions

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result


def is_strong(n):
    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total += factorial(digit)
        n //= 10

    return total == original


start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    if is_strong(n):
        print(n, end=" ")


# 86. WAP to print all Armstrong numbers between given interval using functions

def is_armstrong(n):
    original = n
    digits = str(n)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == original


start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    if is_armstrong(n):
        print(n, end=" ")


# 87. WAP to print all perfect numbers between given interval using functions

def is_perfect(n):
    if n <= 1:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total += i

    return total == n


start = int(input("\nEnter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):
    if is_perfect(n):
        print(n, end=" ")


# 88. WAP to Print the Alternate Elements in an Array

arr = list(map(int, input("\nEnter array elements: ").split()))

print("Alternate elements:")

for i in range(0, len(arr), 2):
    print(arr[i], end=" ")


# 89. WAP to Display the ATM Transaction

balance = 10000

while True:

    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Amount deposited successfully.")
            print("Balance:", balance)
        else:
            print("Invalid amount.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount > balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            balance -= amount
            print("Please collect your cash.")
            print("Balance:", balance)

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice.")


# 90. WAP to print reverse case of a given string

string = input("Enter a string: ")

result = ""

for ch in string:

    if ch.isupper():
        result += ch.lower()

    elif ch.islower():
        result += ch.upper()

    else:
        result += ch

print("Reverse case:", result)