# # 1. Check Even or Odd (Integer)
# num = 24
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# # 2. Find Positive or Negative (Integer)
# num = -10
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


# # 3. Find Greatest of Three Numbers (Integer)
# a, b, c = 10, 25, 15
# if a > b and a > c:
#     print(a, "is greatest")
# elif b > c:
#     print(b, "is greatest")
# else:
#     print(c, "is greatest")


# # 4. Check Divisibility by 5 (Integer)
# num = 45
# if num % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not divisible by 5")


# # 5. Reverse a Number (Integer)
# num = 12345
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print("Reverse:", rev)


# # 6. Calculate Simple Interest (Float)
# p = 10000
# r = 5.5
# t = 2
# si = (p * r * t) / 100
# print("Simple Interest:", si)


# # 7. Convert Float into Integer
# num = 25.75
# print(int(num))


# # 8. Find Area of Circle (Float)
# radius = 7.5
# area = 3.14 * radius * radius
# print("Area:", area)


# # 9. Calculate Average of Three Numbers (Float)
# a, b, c = 10.5, 20.5, 30.5
# avg = (a + b + c) / 3
# print("Average:", avg)


# # 10. Find Discount (Float)
# price = 1000
# discount = 10
# final_price = price - (price * discount / 100)
# print("Final Price:", final_price)


# # 11. Count Vowels in String
# text = "python programming"
# count = 0
# for ch in text:
#     if ch in "aeiou":
#         count += 1
# print("Vowels:", count)


# # 12. Reverse a String
# text = "Python"
# print(text[::-1])


# # 13. Check Palindrome String
# text = "madam"
# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # 14. Count Words in String
# text = "Python is easy to learn"
# print("Words:", len(text.split()))


# # 15. Find Frequency of a Character
# text = "programming"
# ch = "m"
# print("Frequency:", text.count(ch))


# # 16. Convert String into Uppercase
# text = "hello python"
# print(text.upper())


# # 17. Check String Contains a Word
# text = "I love Python programming"
# if "Python" in text:
#     print("Word Found")
# else:
#     print("Word Not Found")


# # 18. Remove Spaces from String
# text = "Python is easy"
# print(text.replace(" ", ""))


# # 19. Find Longest Word
# text = "Python programming is interesting"
# words = text.split()
# longest = max(words, key=len)
# print("Longest Word:", longest)


# # 20. Count Digits in String
# text = "python12345"
# count = 0
# for ch in text:
#     if ch.isdigit():
#         count += 1
# print("Digits:", count)


# # 21. Find Maximum Element in List
# numbers = [10, 20, 50, 30, 40]
# print("Maximum:", max(numbers))


# # 22. Find Minimum Element in List
# numbers = [15, 5, 25, 10, 30]
# print("Minimum:", min(numbers))


# # 23. Calculate Sum of List
# numbers = [10, 20, 30, 40, 50]
# print("Sum:", sum(numbers))


# # 24. Find Even Numbers in List
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# for num in numbers:
#     if num % 2 == 0:
#         print(num)


# # 25. Remove Duplicate Elements
# numbers = [1, 2, 2, 3, 4, 4, 5]
# unique = list(set(numbers))
# print("Unique:", unique)



