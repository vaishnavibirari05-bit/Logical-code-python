# # 1. Create and display a list
# a = [10, 20, 30, 40, 50]
# print(a)

# # 2. Print elements using for loop
# a = [10, 20, 30, 40, 50]
# for i in a:
#     print(i)

# # 3. Print elements using while loop
# a = [10, 20, 30, 40, 50]
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# # 4. Find length of list
# a = [10, 20, 30, 40]
# print(len(a))

# # 5. Find sum of list
# a = [10, 20, 30, 40]
# total = 0
# for i in a:
#     total += i
# print(total)

# # 6. Find maximum number
# a = [12, 45, 23, 67, 34]
# print(max(a))

# # 7. Find minimum number
# a = [12, 45, 23, 67, 34]
# print(min(a))

# # 8. Display even numbers
# a = [1, 2, 3, 4, 5, 6]
# for i in a:
#     if i % 2 == 0:
#         print(i)

# # 9. Display odd numbers
# a = [1, 2, 3, 4, 5, 6]
# for i in a:
#     if i % 2 != 0:
#         print(i)

# # 10. Count even numbers
# a = [1, 2, 3, 4, 5, 6]
# count = 0
# for i in a:
#     if i % 2 == 0:
#         count += 1
# print(count)

# # 11. Count odd numbers
# a = [1, 2, 3, 4, 5, 6]
# count = 0
# for i in a:
#     if i % 2 != 0:
#         count += 1
# print(count)

# # 12. Search element in list
# a = [10, 20, 30, 40]
# num = 30
# if num in a:
#     print("Found")
# else:
#     print("Not Found")

# # 13. Reverse list using loop
# a = [10, 20, 30, 40]
# b = []
# for i in a:
#     b.insert(0, i)
# print(b)

# # 14. Find duplicate elements
# a = [10, 20, 10, 30, 20, 40]
# for i in a:
#     if a.count(i) > 1:
#         print(i)

# # 15. Remove duplicate elements
# a = [10, 20, 10, 30, 20, 40]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)

# # 16. Square of each element
# a = [2, 3, 4, 5]
# for i in a:
#     print(i * i)

# # 17. Find positive numbers
# a = [-2, 5, -3, 8, 10]
# for i in a:
#     if i > 0:
#         print(i)

# # 18. Find negative numbers
# a = [-2, 5, -3, 8, 10]
# for i in a:
#     if i < 0:
#         print(i)

# # 19. Sort list in ascending order
# a = [40, 10, 30, 20]
# a.sort()
# print(a)

# # 20. Merge two lists
# a = [10, 20, 30]
# b = [40, 50, 60]
# c = a + b
# print(c)


# # ================= TUPLE PROGRAMS (21-30) =================

# # 21. Create and display tuple
# a = (10, 20, 30, 40)
# print(a)

# # 22. Display tuple using for loop
# a = (10, 20, 30, 40)
# for i in a:
#     print(i)

# # 23. Display tuple using while loop
# a = (10, 20, 30, 40)
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# # 24. Find tuple length
# a = (10, 20, 30, 40)
# print(len(a))

# # 25. Find sum of tuple
# a = (10, 20, 30, 40)
# total = 0
# for i in a:
#     total += i
# print(total)

# # 26. Find maximum element
# a = (12, 45, 23, 67, 34)
# print(max(a))

# # 27. Find minimum element
# a = (12, 45, 23, 67, 34)
# print(min(a))

# # 28. Display even numbers
# a = (1, 2, 3, 4, 5, 6)
# for i in a:
#     if i % 2 == 0:
#         print(i)

# # 29. Count particular element
# a = (10, 20, 10, 30, 10)
# print(a.count(10))

# # 30. Find index of element
# a = (10, 20, 30, 40)
# print(a.index(30))


# # ================= DICTIONARY PROGRAMS (31-40) =================

# # 31. Create and display dictionary
# student = {"name": "Rahul", "age": 20, "marks": 85}
# print(student)

# # 32. Display all keys
# student = {"name": "Rahul", "age": 20, "marks": 85}
# for i in student:
#     print(i)

# # 33. Display all values
# student = {"name": "Rahul", "age": 20, "marks": 85}
# for i in student.values():
#     print(i)

# # 34. Display keys and values
# student = {"name": "Rahul", "age": 20, "marks": 85}
# for k, v in student.items():
#     print(k, v)

# # 35. Find total marks
# marks = {"Math": 80, "English": 75, "Python": 90}
# total = 0
# for i in marks.values():
#     total += i
# print(total)

# # 36. Students scoring above 60
# students = {"Amit": 75, "Rahul": 45, "Sneha": 85}
# for k, v in students.items():
#     if v > 60:
#         print(k, v)

# # 37. Count passed students
# students = {"Amit": 75, "Rahul": 25, "Sneha": 85}
# count = 0
# for v in students.values():
#     if v >= 35:
#         count += 1
# print(count)

# # 38. Find maximum marks
# marks = {"Amit": 75, "Rahul": 45, "Sneha": 85}
# print(max(marks.values()))

# # 39. Search a key
# student = {"name": "Rahul", "age": 20}
# if "name" in student:
#     print("Key Found")
# else:
#     print("Key Not Found")

# # 40. Add new key-value pair
# student = {"name": "Rahul", "age": 20}
# student["city"] = "Pune"
# print(student)


# # ================= FOR LOOP PROGRAMS (41-45) =================

# # 41. Print numbers from 1 to 10
# for i in range(1, 11):
#     print(i)

# # 42. Multiplication table
# num = 5
# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# # 43. Find factorial
# num = 5
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
# print(fact)

# # 44. Fibonacci series
# a, b = 0, 1
# for i in range(10):
#     print(a)
#     a, b = b, a + b

# # 45. Check prime number
# num = 7
# count = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not Prime")


# # ================= WHILE LOOP PROGRAMS (46-50) =================

# # 46. Print numbers from 1 to 10
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# # 47. Sum of numbers from 1 to 10
# i = 1
# total = 0
# while i <= 10:
#     total += i
#     i += 1
# print(total)

# # 48. Reverse a number
# num = 12345
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10
# print(rev)

# # 49. Check palindrome number
# num = 121
# temp = num
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = rev * 10 + digit
#     num //= 10

# if temp == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# # 50. Sum of digits
# num = 12345
# total = 0
# while num > 0:
#     digit = num % 10
#     total += digit
#     num //= 10
# print(total)



