#Write a program to print multiplication table of any number.
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

n = int(input("Enter a number: "))
table(n)
#Count number of digits in a number
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

n = int(input("Enter a number: "))
print("Number of digits:", count_digits(n))

#Find first and last digit
def first_last(n):
    last = n % 10
    while n >= 10:
        n = n // 10
    first = n
    print("First digit:", first)
    print("Last digit:", last)

n = int(input("Enter a number: "))
first_last(n)
#Sum of first and last digit
def sum_first_last(n):
    last = n % 10
    while n >= 10:
        n = n // 10
    first = n
    return first + last

n = int(input("Enter a number: "))
print("Sum of first and last digit:", sum_first_last(n))

#check wheather palindrome or not
def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse  

n = int(input("Enter a number: "))

if is_palindrome(n):
    print("Palindrome")
else:
    print("Not a palindrome")

#Sum of digits
def sum_digits(n):
    total = 0

    while n > 0:
        total += n % 10
        n = n // 10

    return total

n = int(input("Enter a number: "))
print("Sum of digits:", sum_digits(n))

#product of digits
def product_digits(n):
    product = 1

    while n > 0:
        product *= n % 10
        n = n // 10

    return product  

n = int(input("Enter a number: "))
print("Product of digits:", product_digits(n))

# Reverse of a number
def reverse_number(n):
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return reverse

n = int(input("Enter a number: "))
print("Reverse of the number:", reverse_number(n))

#Frequency of each digit
def digit_frequency(n):
    frequency = [0] * 10

    while n > 0:
        digit = n % 10
        frequency[digit] += 1
        n = n // 10

    return frequency

n = int(input("Enter a number: "))
print("Frequency of each digit:", digit_frequency(n))
#Number in words
def number_words(n):
    words = ["Zero", "One", "Two", "Three", "Four",
             "Five", "Six", "Seven", "Eight", "Nine"]

    if n == 0:
        print("Zero")
        return

    digits = []

    while n > 0:
        digits.append(n % 10)
        n = n // 10

    for i in reversed(digits):
        print(words[i], end=" ")

n = int(input("Enter a number: "))
number_words(n)

# Print all ASCII characters with values
def ascii_values():
    for i in range(0, 128):
        print(i, "=", chr(i))

ascii_values()

#Find power using for loop
def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))

print("Result:", power(base, exponent))

#Find all factors of a number

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

n = int(input("Enter a number: "))
print("Factors:")
factors(n)

#Calculate factorial
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact

n = int(input("Enter a number: "))
print("Factorial:", factorial(n))

#Check whether a number is Prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input("Enter a number: "))
if is_prime(n):
    print("Prime")  
else:
    print("Not Prime")
#Print all Prime numbers from 1 to n
def print_primes(n):
    for num in range(2, n + 1):
        if is_prime(num):
            print(num, end=" ")

n = int(input("Enter a number: "))
print("Prime numbers from 1 to", n, ":")
print_primes(n)

#Sum of all Prime numbers from 1 to n
def sum_primes(n):
    total = 0
    for num in range(2, n + 1):
        if is_prime(num):
            total += num
    return total
n = int(input("Enter a number: "))
print("Sum of all prime numbers from 1 to", n, ":", sum_primes(n))  

#Find all Prime factors
def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0 and is_prime(i):
            factors.append(i)
            n //= i
    return factors

n = int(input("Enter a number: "))
print("Prime factors:", prime_factors(n))

#Check whether a number is Armstrong
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == n

n = int(input("Enter a number: "))
if is_armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")

#Print all Armstrong numbers from 1 to n
def print_armstrong(n):
    for num in range(1, n + 1):
        if is_armstrong(num):
            print(num, end=" ")

n = int(input("Enter a number: "))
print("Armstrong numbers from 1 to", n, ":")

#Check whether a number is Perfect number
def is_perfect(n):
    if n <= 1:
        return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n

n = int(input("Enter a number: "))
if is_perfect(n):
    print("Perfect number")
else:
    print("Not a perfect number")
    
