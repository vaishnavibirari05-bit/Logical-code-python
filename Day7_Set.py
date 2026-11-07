# # 1. Create and Display a Set

# a = {10, 20, 30, 40, 50}
# print(a)


# # 2. Add an Element to a Set

# a = {10, 20, 30}
# a.add(40)
# print(a)


# # 3. Add Multiple Elements to a Set

# a = {1, 2, 3}
# a.update([4, 5, 6])
# print(a)


# # 4. Remove an Element from a Set

# a = {10, 20, 30, 40}
# a.remove(20)
# print(a)


# # 5. Find the Length of a Set

# a = {10, 20, 30, 40, 50}
# print("Length:", len(a))


# # 6. Check Whether an Element Exists

# a = {10, 20, 30, 40}

# if 20 in a:
#     print("Element exists")
# else:
#     print("Element not found")


# # 7. Find Maximum Element in a Set

# a = {10, 50, 20, 80, 30}
# print("Maximum:", max(a))


# # 8. Find Minimum Element in a Set

# a = {10, 50, 20, 80, 30}
# print("Minimum:", min(a))


# # 9. Find Sum of Set Elements

# a = {10, 20, 30, 40}
# print("Sum:", sum(a))


# # 10. Display Even Numbers from a Set

# a = {1, 2, 3, 4, 5, 6, 7, 8}

# for i in a:
#     if i % 2 == 0:
#         print(i)


# # 11. Display Odd Numbers from a Set

# a = {1, 2, 3, 4, 5, 6, 7, 8}

# for i in a:
#     if i % 2 != 0:
#         print(i)


# # 12. Find Union of Two Sets

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a.union(b))


# # 13. Find Intersection of Two Sets

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a.intersection(b))


# # 14. Find Difference Between Two Sets

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a.difference(b))


# # 15. Find Symmetric Difference

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a.symmetric_difference(b))


# # 16. Remove Duplicate Elements from a List

# a = [10, 20, 10, 30, 20, 40, 30]

# b = set(a)

# print(b)


# # 17. Check Whether Two Sets are Equal

# a = {1, 2, 3}
# b = {3, 2, 1}

# if a == b:
#     print("Both sets are equal")
# else:
#     print("Sets are not equal")


# # 18. Check Subset of a Set

# a = {1, 2}
# b = {1, 2, 3, 4, 5}

# print(a.issubset(b))


# # 19. Check Superset of a Set

# a = {1, 2, 3, 4, 5}
# b = {1, 2}

# print(a.issuperset(b))


# # 20. Find Common Elements in Three Sets

# a = {10, 20, 30, 40}
# b = {20, 30, 50, 60}
# c = {20, 30, 70, 80}

# result = a.intersection(b, c)

# print("Common Elements:", result)