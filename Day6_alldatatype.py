
# # 1. Find Even or Odd (Integer)
# num = 25

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# # 2. Calculate Average (Float)
# a = 10.5
# b = 20.5
# c = 30.5

# avg = (a + b + c) / 3
# print("Average:", avg)


# # 3. Check Palindrome (String)
# a = "madam"

# if a == a[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# # 4. Find Second Largest (List)
# a = [10, 50, 30, 20, 40]

# b = sorted(set(a))
# print("Second Largest:", b[-2])


# # 5. Find Sum of Tuple Elements
# a = (10, 20, 30, 40, 50)

# total = 0
# for i in a:
#     total += i

# print("Sum:", total)


# # 6. Find Common Elements (Set)
# a = {10, 20, 30, 40}
# b = {30, 40, 50, 60}

# print("Common Elements:", a.intersection(b))


# # 7. Find Students Who Passed (Dictionary)
# students = {"Rahul": 80, "Amit": 30, "Sneha": 75}

# for name, marks in students.items():
#     if marks >= 35:
#         print(name, "Passed")


# # 8. Check Voting Eligibility (Boolean)
# age = 20

# eligible = age >= 18
# print("Eligible:", eligible)


# # 9. Count Vowels (String)
# a = "programming"
# count = 0

# for i in a:
#     if i in "aeiou":
#         count += 1

# print("Vowels:", count)


# # 10. Remove Duplicate Elements (List and Set)
# a = [10, 20, 10, 30, 20, 40]

# b = list(set(a))
# print("Without Duplicates:", b)
