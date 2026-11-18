# # 10 Python Programs Using Functions

# # 1. Add Two Numbers
# def add(a, b):
#     return a + b

# print("Addition:", add(10, 20))


# # 2. Check Even or Odd
# def check_even_odd(num):
#     if num % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")

# check_even_odd(15)


# # 3. Greatest of Two Numbers
# def greatest(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print("Greatest:", greatest(25, 15))


# # 4. Check Positive, Negative or Zero
# def check_number(num):
#     if num > 0:
#         print("Positive Number")
#     elif num < 0:
#         print("Negative Number")
#     else:
#         print("Zero")

# check_number(-5)


# # 5. Factorial of a Number
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact = fact * i
#     return fact

# print("Factorial:", factorial(5))


# # 6. Check Prime Number
# def check_prime(num):
#     if num < 2:
#         return False

#     for i in range(2, num):
#         if num % i == 0:
#             return False

#     return True

# print("Prime Number:", check_prime(7))


# # 7. Reverse a String
# def reverse_string(text):
#     return text[::-1]

# print("Reverse String:", reverse_string("Python"))


# # 8. Check Palindrome String
# def palindrome(text):
#     if text == text[::-1]:
#         print("Palindrome")
#     else:
#         print("Not Palindrome")

# palindrome("madam")


# # 9. Sum of List Elements
# def list_sum(numbers):
#     total = 0
#     for num in numbers:
#         total += num
#     return total

# data = [10, 20, 30, 40, 50]
# print("List Sum:", list_sum(data))


# # 10. Fibonacci Series
# def fibonacci(n):
#     a = 0
#     b = 1

#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b

# print("\nFibonacci Series:")
# fibonacci(10)