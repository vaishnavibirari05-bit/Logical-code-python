
# # 1. Check Even or Odd Number
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# # 2. Find Greatest of Three Numbers
# a = 10
# b = 25
# c = 15

# if a > b and a > c:
#     print("Greatest:", a)
# elif b > a and b > c:
#     print("Greatest:", b)
# else:
#     print("Greatest:", c)


# # 3. Check Positive, Negative or Zero
# num = int(input("Enter number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# # 4. Reverse a Number
# num = 12345
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# print("Reverse:", rev)


# # 5. Check Palindrome Number
# num = 121
# temp = num
# rev = 0

# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num = num // 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # 6. Find Factorial of a Number
# num = 5
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial:", fact)


# # 7. Check Prime Number
# num = 7
# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")


# # 8. Find Sum of Digits
# num = 1234
# total = 0

# while num > 0:
#     digit = num % 10
#     total += digit
#     num = num // 10

# print("Sum of digits:", total)


# # 9. Find Largest Element in a List
# numbers = [10, 45, 20, 80, 30]
# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

# print("Largest Element:", largest)


# # 10. Fibonacci Series
# n = 10
# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
