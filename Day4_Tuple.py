
# # ==========================================
# # PYTHON TUPLE - 50 PRACTICE PROGRAMS
# # ==========================================


# # 1. Create and print a tuple
# a = (10, 20, 30, 40, 50)
# print(a)


# # 2. Find the length of a tuple
# a = (10, 20, 30, 40, 50)
# print(len(a))


# # 3. Access the first element
# a = (10, 20, 30, 40)
# print(a[0])


# # 4. Access the last element
# a = (10, 20, 30, 40)
# print(a[-1])


# # 5. Print all elements using for loop
# a = (10, 20, 30, 40)
# for i in a:
#     print(i)


# # 6. Print all elements using while loop
# a = (10, 20, 30, 40)
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1


# # 7. Find the maximum number
# a = (12, 45, 67, 23, 89)
# print(max(a))


# # 8. Find the minimum number
# a = (12, 45, 67, 23, 89)
# print(min(a))


# # 9. Find the sum of tuple elements
# a = (10, 20, 30, 40)
# print(sum(a))


# # 10. Count even numbers
# a = (10, 15, 20, 25, 30, 35)
# count = 0
# for i in a:
#     if i % 2 == 0:
#         count += 1
# print(count)


# # 11. Count odd numbers
# a = (10, 15, 20, 25, 30, 35)
# count = 0
# for i in a:
#     if i % 2 != 0:
#         count += 1
# print(count)


# # 12. Display even numbers
# a = (10, 15, 20, 25, 30, 35)
# for i in a:
#     if i % 2 == 0:
#         print(i)


# # 13. Display odd numbers
# a = (10, 15, 20, 25, 30, 35)
# for i in a:
#     if i % 2 != 0:
#         print(i)


# # 14. Check whether an element exists
# a = (10, 20, 30, 40)
# if 20 in a:
#     print("Element found")
# else:
#     print("Element not found")


# # 15. Count the occurrence of an element
# a = (10, 20, 10, 30, 10, 40)
# print(a.count(10))


# # 16. Find the index of an element
# a = (10, 20, 30, 40)
# print(a.index(30))


# # 17. Reverse a tuple using slicing
# a = (10, 20, 30, 40, 50)
# print(a[::-1])


# # 18. Print the first three elements
# a = (10, 20, 30, 40, 50)
# print(a[:3])


# # 19. Print the last three elements
# a = (10, 20, 30, 40, 50)
# print(a[-3:])


# # 20. Print elements from index 1 to 4
# a = (10, 20, 30, 40, 50, 60)
# print(a[1:5])


# # 21. Concatenate two tuples
# a = (10, 20, 30)
# b = (40, 50, 60)
# c = a + b
# print(c)


# # 22. Repeat a tuple three times
# a = (10, 20, 30)
# print(a * 3)


# # 23. Find the length without using len()
# a = (10, 20, 30, 40, 50)
# count = 0
# for i in a:
#     count += 1
# print(count)


# # 24. Find the sum without using sum()
# a = (10, 20, 30, 40)
# total = 0
# for i in a:
#     total += i
# print(total)


# # 25. Find maximum without using max()
# a = (12, 45, 67, 23, 89)
# maximum = a[0]
# for i in a:
#     if i > maximum:
#         maximum = i
# print(maximum)


# # 26. Find minimum without using min()
# a = (12, 45, 67, 23, 89)
# minimum = a[0]
# for i in a:
#     if i < minimum:
#         minimum = i
# print(minimum)


# # 27. Separate positive and negative numbers
# a = (10, -5, 20, -8, 30, -2)
# for i in a:
#     if i >= 0:
#         print("Positive:", i)
#     else:
#         print("Negative:", i)


# # 28. Create a tuple of squares
# a = (1, 2, 3, 4, 5)
# b = ()
# for i in a:
#     b += (i * i,)
# print(b)


# # 29. Create a tuple of cubes
# a = (1, 2, 3, 4, 5)
# b = ()
# for i in a:
#     b += (i ** 3,)
# print(b)


# # 30. Find numbers greater than 50
# a = (20, 60, 45, 80, 30, 90)
# for i in a:
#     if i > 50:
#         print(i)


# # 31. Find numbers less than 50
# a = (20, 60, 45, 80, 30, 90)
# for i in a:
#     if i < 50:
#         print(i)


# # 32. Check whether tuple is empty
# a = ()
# if len(a) == 0:
#     print("Tuple is empty")
# else:
#     print("Tuple is not empty")


# # 33. Convert list into tuple
# a = [10, 20, 30, 40]
# b = tuple(a)
# print(b)


# # 34. Convert tuple into list
# a = (10, 20, 30, 40)
# b = list(a)
# print(b)


# # 35. Sort tuple elements
# a = (50, 20, 40, 10, 30)
# b = tuple(sorted(a))
# print(b)


# # 36. Find second largest number
# a = (10, 50, 30, 90, 70)
# b = sorted(set(a))
# print(b[-2])


# # 37. Find second smallest number
# a = (10, 50, 30, 90, 70)
# b = sorted(set(a))
# print(b[1])


# # 38. Remove duplicate elements
# a = (10, 20, 10, 30, 20, 40)
# b = tuple(set(a))
# print(b)


# # 39. Merge two tuples
# a = (1, 2, 3)
# b = (4, 5, 6)
# c = a + b
# print(c)


# # 40. Compare two tuples
# a = (10, 20, 30)
# b = (10, 20, 30)
# if a == b:
#     print("Both tuples are equal")
# else:
#     print("Tuples are different")


# # 41. Find common elements
# a = (10, 20, 30, 40)
# b = (20, 40, 50, 60)
# for i in a:
#     if i in b:
#         print(i)


# # 42. Find unique elements from two tuples
# a = (10, 20, 30)
# b = (20, 40, 50)
# c = tuple(set(a) ^ set(b))
# print(c)


# # 43. Multiply all tuple elements
# a = (2, 3, 4, 5)
# total = 1
# for i in a:
#     total *= i
# print(total)


# # 44. Find the average of tuple elements
# a = (10, 20, 30, 40, 50)
# total = 0
# for i in a:
#     total += i
# print(total / len(a))


# # 45. Check whether all elements are positive
# a = (10, 20, 30, 40)
# if all(i > 0 for i in a):
#     print("All are positive")
# else:
#     print("Some numbers are not positive")


# # 46. Find the frequency of each element
# a = (10, 20, 10, 30, 20, 10)
# for i in set(a):
#     print(i, "=", a.count(i))


# # 47. Find palindrome tuple
# a = (1, 2, 3, 2, 1)
# if a == a[::-1]:
#     print("Palindrome tuple")
# else:
#     print("Not palindrome")


# # 48. Unpack tuple elements
# a = (10, 20, 30)
# x, y, z = a
# print("x =", x)
# print("y =", y)
# print("z =", z)


# # 49. Find the difference between maximum and minimum
# a = (10, 50, 30, 90, 20)
# result = max(a) - min(a)
# print(result)


# # 50. Find the sum of even and odd numbers separately
# a = (10, 15, 20, 25, 30, 35)
# even_sum = 0
# odd_sum = 0

# for i in a:
#     if i % 2 == 0:
#         even_sum += i
#     else:
#         odd_sum += i

# print("Even sum:", even_sum)
# print("Odd sum:", odd_sum)

