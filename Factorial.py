''' fact = 1
number = int(input("Enter the number: "))
for i in range(1, number + 1):
    fact *= i
print(f"The factorial of {number} is {fact}") '''

# capitals = {
#     "USA": "Washington, D.C.",
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "India": "New Delhi",
#     "Germany": "Berlin"
# }

# print("Country Capitals:")
# for country, capital in capitals.items():
#     print(f"The capital of {country} is {capital}.")


# number = [1, 2, 3, 4, 5]
# for num in number:
#     if num % 2 == 0:
#         print(num, end=" ")
#         print(type(num))


# num = []
# for i in range(1, 5):
#     n = int(input(f"Enter number {i}: "))
#     num.append(n)
# greatest = max(num)
# smallest = min(num)
# print(f"The numbers entered are: {num}")
# print(type(num))
# print(f"The greatest number is {greatest}")
# print(f"The smallest number is {smallest}")


# s= input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in s:
#     if char in vowels:
#         count += 1
#         print(char, end=" ")
# print(f"\nThe number of vowels in the string is: {count}")


# s = input("Enter the word: ")
# reverse = ""
# for char in s:
#     print(char)
#     reverse = char + reverse
# print(f"The reverse of the word is: {reverse}")

# word = input("Enter a word: ")
# palindrome = ""
# for i in word:
#     palindrome = i + palindrome
# if word == palindrome:
#     print(f"{word} is a palindrome.")
# else:
#     print(f"{word} is not a palindrome.")

# def primecomposite(num):
#     if num < 2:
#         return "Neither prime nor composite"
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return "Composite"
#     return "Prime"
# number = int(input("Enter a number: "))
# print(primecomposite(number))


# def primeComposite(n):
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:
#             c+=1
#     if c==2:
#         print(f"{n} is a prime number")
#     else:
#         print(f"{n} is a composite number")
# n = int(input("Enter a number: "))
# primeComposite(n)

# def average(n):
#     print(n)
#     s= sum(n)
#     avg  = s/len(n)
#     return avg
# n = []
# for i in range(1, 6):
#     num = int(input(f"Enter number {i}: "))
#     n.append(num)
# print(f"The average of the numbers is: {average(n)}")

# def longest(w1,w2):
#     if len(w1) > len(w2):
#         return "The longest word is: " + w1
#     elif len(w2) > len(w1):
#         return "The longest word is: " + w2
#     else:
#         return "Both words have the same length"

# str1 = input("Enter the first word: ")
# str2 = input("Enter the second word: ") 
# print(longest(str1, str2))

# def check_vowel(char):
#     vowels = "aeiouAEIOU"
#     counter = 0
#     for i in char:
#         if i in vowels:
#             counter += 1
#     return counter
# string = input("Enter a string: ")
# print(f"The number of vowels in the string is: {check_vowel(string)}")

# import math
# num = int(input("Enter a number: "))
# s = math.sqrt(num)
# if s.is_integer():
#     print(f"{num} is a perfect square.")
# else:
#     print(f"{num} is not a perfect square.")


# from math import sqrt,tan,cos,sin
# print("Square root of 16 is:", sqrt(16))
# print("Tangent of 0 degrees is:", tan(0))
# print("Cosine of 0 degrees is:", cos(0))
# print("Sine of 0 degrees is:", sin(0))

import datetime as dt
current_time = dt.datetime.now()
print("Current time:", current_time)