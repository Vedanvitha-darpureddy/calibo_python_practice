# 46. Write a Python program to print all Perfect numbers between 1 to n.

def is_perfect(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num

def perfect_numbers(n):
    for i in range(1, n + 1):
        if is_perfect(i):
            print(i, end=" ")

n = int(input("Enter n: "))
perfect_numbers(n)


# 47. Write a Python program to check whether a number is Strong number or not.

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def is_strong(num):
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total += factorial(digit)
        num //= 10

    return total == original

n = int(input("Enter a number: "))

if is_strong(n):
    print("Strong number")
else:
    print("Not a Strong number")


# 48. Write a Python program to print all Strong numbers between 1 to n.

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

def is_strong(num):
    original = num
    total = 0

    while num > 0:
        digit = num % 10
        total += factorial(digit)
        num //= 10

    return total == original

def strong_numbers(n):
    for i in range(1, n + 1):
        if is_strong(i):
            print(i, end=" ")

n = int(input("Enter n: "))
strong_numbers(n)


# 49. Write a Python program to print Fibonacci series up to n terms.

def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter number of terms: "))
fibonacci(n)


# 50. Write a Python program to print all negative elements in an array.

def print_negative(arr):
    for num in arr:
        if num < 0:
            print(num, end=" ")

arr = list(map(int, input("Enter array elements: ").split()))
print_negative(arr)


# 51. Write a Python program to find second largest element in an array.

def second_largest(arr):
    unique = list(set(arr))
    unique.sort()

    if len(unique) < 2:
        print("Second largest element does not exist")
    else:
        print("Second largest:", unique[-2])

arr = list(map(int, input("Enter array elements: ").split()))
second_largest(arr)


# 52. Write a Python program to find maximum and minimum element in an array.

def max_min(arr):
    maximum = arr[0]
    minimum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    print("Maximum:", maximum)
    print("Minimum:", minimum)

arr = list(map(int, input("Enter array elements: ").split()))
max_min(arr)


# 53. Write a Python program to count total number of even and odd elements in an array.

def count_even_odd(arr):
    even = 0
    odd = 0

    for num in arr:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even elements:", even)
    print("Odd elements:", odd)

arr = list(map(int, input("Enter array elements: ").split()))
count_even_odd(arr)


# 54. Write a Python program to count total number of negative elements in an array.

def count_negative(arr):
    count = 0

    for num in arr:
        if num < 0:
            count += 1

    print("Negative elements:", count)

arr = list(map(int, input("Enter array elements: ").split()))
count_negative(arr)

# 55. Write a Python program to copy all elements from an array to another array.

def copy_array(arr):
    new_arr = arr.copy()
    print("Original array:", arr)
    print("Copied array:", new_arr)

arr = list(map(int, input("Enter array elements: ").split()))
copy_array(arr)


# 56. Write a Python program to delete an element from an array at specified position.

def delete_element(arr, position):
    if 0 <= position < len(arr):
        arr.pop(position)
        print("Array after deletion:", arr)
    else:
        print("Invalid position")

arr = list(map(int, input("Enter array elements: ").split()))
position = int(input("Enter position: "))
delete_element(arr, position)


# 57. Write a Python program to count frequency of each element in an array.

def frequency(arr):
    visited = []

    for num in arr:
        if num not in visited:
            print(num, ":", arr.count(num))
            visited.append(num)

arr = list(map(int, input("Enter array elements: ").split()))
frequency(arr)


# 58. Write a Python program to print all unique elements in the array.

def unique_elements(arr):
    for num in arr:
        if arr.count(num) == 1:
            print(num, end=" ")

arr = list(map(int, input("Enter array elements: ").split()))
unique_elements(arr)


# 59. Write a Python program to count total number of duplicate elements in an array.

def count_duplicates(arr):
    count = 0
    visited = []

    for num in arr:
        if num not in visited:
            if arr.count(num) > 1:
                count += 1
            visited.append(num)

    print("Duplicate elements:", count)

arr = list(map(int, input("Enter array elements: ").split()))
count_duplicates(arr)


# 60. Write a Python program to delete an element from an array at specified position.

def delete_element(arr, position):
    if 0 <= position < len(arr):
        arr.pop(position)
        print("Array after deletion:", arr)
    else:
        print("Invalid position")

arr = list(map(int, input("Enter array elements: ").split()))
position = int(input("Enter position: "))
delete_element(arr, position)


# 61. Write a Python program to count frequency of each element in an array.

def frequency(arr):
    visited = []

    for num in arr:
        if num not in visited:
            print(num, ":", arr.count(num))
            visited.append(num)

arr = list(map(int, input("Enter array elements: ").split()))
frequency(arr)


# 62. Write a Python program to print all unique elements in the array.

def unique_elements(arr):
    for num in arr:
        if arr.count(num) == 1:
            print(num, end=" ")

arr = list(map(int, input("Enter array elements: ").split()))
unique_elements(arr)


# 63. Write a Python program to count total number of duplicate elements in an array.

def count_duplicates(arr):
    count = 0
    visited = []

    for num in arr:
        if num not in visited:
            if arr.count(num) > 1:
                count += 1
            visited.append(num)

    print("Duplicate elements:", count)

arr = list(map(int, input("Enter array elements: ").split()))
count_duplicates(arr)


# 64. Write a Python program to find length of a string and compare and concatenate two strings.

def string_operations(s1, s2):
    print("Length of first string:", len(s1))
    print("Length of second string:", len(s2))

    if s1 == s2:
        print("Strings are equal")
    else:
        print("Strings are not equal")

    print("Concatenated string:", s1 + s2)

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
string_operations(s1, s2)


# 65. Write a Python program to find total number of alphabets, digits or special character in a string.

def count_characters(s):
    alphabets = 0
    digits = 0
    special = 0

    for ch in s:
        if ch.isalpha():
            alphabets += 1
        elif ch.isdigit():
            digits += 1
        else:
            special += 1

    print("Alphabets:", alphabets)
    print("Digits:", digits)
    print("Special characters:", special)

s = input("Enter a string: ")
count_characters(s)


# 66. Write a Python program to count total number of vowels and consonants in a string.

def count_vowels_consonants(s):
    vowels = 0
    consonants = 0

    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)

s = input("Enter a string: ")
count_vowels_consonants(s)


# 67. Write a Python program to count total number of words in a string.

def count_words(s):
    words = s.split()
    print("Number of words:", len(words))

s = input("Enter a string: ")
count_words(s)


# 68. Write a Python program to find reverse of a string.

def reverse_string(s):
    print("Reverse:", s[::-1])

s = input("Enter a string: ")
reverse_string(s)


# 69. Write a Python program to check whether a string is palindrome or not.

def is_palindrome(s):
    s = s.lower()

    if s == s[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")

s = input("Enter a string: ")
is_palindrome(s)


# 70. Write a Python program to find first occurrence of a character in a given string.

def first_occurrence(s, ch):
    position = s.find(ch)

    if position != -1:
        print("First occurrence at index:", position)
    else:
        print("Character not found")

s = input("Enter a string: ")
ch = input("Enter character: ")
first_occurrence(s, ch)


# 71. Write a Python program to find last occurrence of a character in a given string.

def last_occurrence(s, ch):
    position = s.rfind(ch)

    if position != -1:
        print("Last occurrence at index:", position)
    else:
        print("Character not found")

s = input("Enter a string: ")
ch = input("Enter character: ")
last_occurrence(s, ch)


# 72. Write a Python program to search all occurrences of a character in given string.

def all_occurrences(s, ch):
    found = False

    for i in range(len(s)):
        if s[i] == ch:
            print("Character found at index:", i)
            found = True

    if not found:
        print("Character not found")

s = input("Enter a string: ")
ch = input("Enter character: ")
all_occurrences(s, ch)


# 73. Write a Python program to count occurrences of a character in given string.

def count_occurrences(s, ch):
    count = 0

    for c in s:
        if c == ch:
            count += 1

    print("Occurrences:", count)

s = input("Enter a string: ")
ch = input("Enter character: ")
count_occurrences(s, ch)


# 74. Write a Python program to find highest frequency character in a string.

def highest_frequency(s):
    max_count = 0
    max_char = ""

    for ch in s:
        count = s.count(ch)

        if count > max_count:
            max_count = count
            max_char = ch

    print("Highest frequency character:", max_char)
    print("Frequency:", max_count)

s = input("Enter a string: ")
highest_frequency(s)


# 75. Write a Python program to find lowest frequency character in a string.

def lowest_frequency(s):
    min_count = float("inf")
    min_char = ""

    for ch in s:
        count = s.count(ch)

        if count < min_count:
            min_count = count
            min_char = ch

    print("Lowest frequency character:", min_char)
    print("Frequency:", min_count)

s = input("Enter a string: ")
lowest_frequency(s)
