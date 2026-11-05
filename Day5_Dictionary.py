# # 1. Create and print a dictionary
# student = {"name": "Rahul", "age": 21, "city": "Pune"}
# print(student)


# # 2. Access a value using its key
# student = {"name": "Rahul", "age": 21}
# print(student["name"])


# # 3. Access value using get()
# student = {"name": "Rahul", "age": 21}
# print(student.get("age"))


# # 4. Print all keys
# student = {"name": "Rahul", "age": 21, "city": "Pune"}
# for i in student:
#     print(i)


# # 5. Print all values
# student = {"name": "Rahul", "age": 21, "city": "Pune"}
# for i in student.values():
#     print(i)


# # 6. Print all keys and values
# student = {"name": "Rahul", "age": 21, "city": "Pune"}
# for key, value in student.items():
#     print(key, ":", value)


# # 7. Find the length of a dictionary
# student = {"name": "Rahul", "age": 21, "city": "Pune"}
# print(len(student))


# # 8. Add a new key-value pair
# student = {"name": "Rahul", "age": 21}
# student["city"] = "Pune"
# print(student)


# # 9. Update an existing value
# student = {"name": "Rahul", "age": 21}
# student["age"] = 22
# print(student)


# # 10. Delete an element using del
# student = {"name": "Rahul", "age": 21, "city": "Pune"}
# del student["age"]
# print(student)


# # 11. Delete an element using pop()
# student = {"name": "Rahul", "age": 21, "city": "Pune"}
# student.pop("age")
# print(student)


# # 12. Check whether a key exists
# student = {"name": "Rahul", "age": 21}
# if "name" in student:
#     print("Key found")
# else:
#     print("Key not found")


# # 13. Check whether a value exists
# student = {"name": "Rahul", "age": 21}
# if 21 in student.values():
#     print("Value found")
# else:
#     print("Value not found")


# # 14. Copy a dictionary
# student = {"name": "Rahul", "age": 21}
# new_student = student.copy()
# print(new_student)


# # 15. Clear all dictionary elements
# student = {"name": "Rahul", "age": 21}
# student.clear()
# print(student)


# # 16. Merge two dictionaries
# a = {"name": "Rahul", "age": 21}
# b = {"city": "Pune", "marks": 85}
# a.update(b)
# print(a)


# # 17. Create dictionary using fromkeys()
# keys = ("name", "age", "city")
# student = dict.fromkeys(keys, "Unknown")
# print(student)


# # 18. Find the maximum value
# marks = {"Rahul": 85, "Amit": 90, "Neha": 78}
# print(max(marks.values()))


# # 19. Find the minimum value
# marks = {"Rahul": 85, "Amit": 90, "Neha": 78}
# print(min(marks.values()))


# # 20. Find the sum of all values
# marks = {"Rahul": 85, "Amit": 90, "Neha": 78}
# print(sum(marks.values()))


# # 21. Calculate average marks
# marks = {"Rahul": 85, "Amit": 90, "Neha": 78}
# total = sum(marks.values())
# average = total / len(marks)
# print(average)


# # 22. Display students who scored above 60
# marks = {"Rahul": 85, "Amit": 45, "Neha": 78, "Raj": 55}
# for name, mark in marks.items():
#     if mark > 60:
#         print(name, mark)


# # 23. Display students who passed
# marks = {"Rahul": 85, "Amit": 25, "Neha": 78, "Raj": 30}
# for name, mark in marks.items():
#     if mark >= 35:
#         print(name, "Pass")


# # 24. Count the number of passed students
# marks = {"Rahul": 85, "Amit": 25, "Neha": 78, "Raj": 30}
# count = 0
# for mark in marks.values():
#     if mark >= 35:
#         count += 1
# print(count)


# # 25. Count the number of failed students
# marks = {"Rahul": 85, "Amit": 25, "Neha": 78, "Raj": 30}
# count = 0
# for mark in marks.values():
#     if mark < 35:
#         count += 1
# print(count)


# # 26. Find the student with highest marks
# marks = {"Rahul": 85, "Amit": 90, "Neha": 78}
# topper = max(marks, key=marks.get)
# print(topper, marks[topper])


# # 27. Find the student with lowest marks
# marks = {"Rahul": 85, "Amit": 90, "Neha": 78}
# lowest = min(marks, key=marks.get)
# print(lowest, marks[lowest])


# # 28. Display even values
# data = {"a": 10, "b": 15, "c": 20, "d": 25}
# for key, value in data.items():
#     if value % 2 == 0:
#         print(key, value)


# # 29. Display odd values
# data = {"a": 10, "b": 15, "c": 20, "d": 25}
# for key, value in data.items():
#     if value % 2 != 0:
#         print(key, value)


# # 30. Count even values
# data = {"a": 10, "b": 15, "c": 20, "d": 25}
# count = 0
# for value in data.values():
#     if value % 2 == 0:
#         count += 1
# print(count)


# # 31. Count odd values
# data = {"a": 10, "b": 15, "c": 20, "d": 25}
# count = 0
# for value in data.values():
#     if value % 2 != 0:
#         count += 1
# print(count)


# # 32. Create a dictionary of squares
# numbers = (1, 2, 3, 4, 5)
# squares = {}
# for i in numbers:
#     squares[i] = i ** 2
# print(squares)


# # 33. Create a dictionary of cubes
# numbers = (1, 2, 3, 4, 5)
# cubes = {}
# for i in numbers:
#     cubes[i] = i ** 3
# print(cubes)


# # 34. Swap keys and values
# data = {"a": 1, "b": 2, "c": 3}
# new_data = {}
# for key, value in data.items():
#     new_data[value] = key
# print(new_data)


# # 35. Sort dictionary by keys
# data = {"c": 30, "a": 10, "b": 20}
# new_data = dict(sorted(data.items()))
# print(new_data)


# # 36. Sort dictionary by values
# data = {"a": 30, "b": 10, "c": 20}
# new_data = dict(sorted(data.items(), key=lambda x: x[1]))
# print(new_data)


# # 37. Remove duplicate values
# data = {"a": 10, "b": 20, "c": 10, "d": 30}
# new_data = {}
# for key, value in data.items():
#     if value not in new_data.values():
#         new_data[key] = value
# print(new_data)


# # 38. Find common keys in two dictionaries
# a = {"name": "Rahul", "age": 21, "city": "Pune"}
# b = {"name": "Amit", "age": 22, "marks": 80}
# for key in a:
#     if key in b:
#         print(key)


# # 39. Find unique keys in two dictionaries
# a = {"a": 10, "b": 20, "c": 30}
# b = {"b": 40, "c": 50, "d": 60}
# for key in a:
#     if key not in b:
#         print(key)
# for key in b:
#     if key not in a:
#         print(key)


# # 40. Count frequency of characters
# text = "programming"
# frequency = {}
# for i in text:
#     frequency[i] = frequency.get(i, 0) + 1
# print(frequency)


# # 41. Count frequency of words
# text = "python is easy python is powerful"
# words = text.split()
# frequency = {}
# for i in words:
#     frequency[i] = frequency.get(i, 0) + 1
# print(frequency)


# # 42. Find the largest key
# data = {10: "A", 20: "B", 30: "C"}
# print(max(data))


# # 43. Find the smallest key
# data = {10: "A", 20: "B", 30: "C"}
# print(min(data))


# # 44. Multiply all dictionary values
# data = {"a": 2, "b": 3, "c": 4}
# total = 1
# for value in data.values():
#     total *= value
# print(total)


# # 45. Create a dictionary from two lists
# keys = ["name", "age", "city"]
# values = ["Rahul", 21, "Pune"]
# student = dict(zip(keys, values))
# print(student)


# # 46. Check whether a dictionary is empty
# data = {}
# if not data:
#     print("Dictionary is empty")
# else:
#     print("Dictionary is not empty")


# # 47. Create a nested dictionary
# students = {
#     "student1": {"name": "Rahul", "marks": 85},
#     "student2": {"name": "Neha", "marks": 90}
# }
# print(students)


# # 48. Access values from a nested dictionary
# students = {
#     "student1": {"name": "Rahul", "marks": 85},
#     "student2": {"name": "Neha", "marks": 90}
# }
# print(students["student1"]["name"])
# print(students["student2"]["marks"])


# # 49. Find the second highest value
# marks = {"Rahul": 85, "Amit": 90, "Neha": 78, "Raj": 95}
# values = sorted(set(marks.values()))
# print(values[-2])


# # 50. Separate even and odd values into dictionaries
# data = {"a": 10, "b": 15, "c": 20, "d": 25}

# even = {}
# odd = {}

# for key, value in data.items():
#     if value % 2 == 0:
#         even[key] = value
#     else:
#         odd[key] = value

# print("Even Dictionary:", even)
# print("Odd Dictionary:", odd)


