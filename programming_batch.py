# check whether number is even or odd.

# num = int(input("Enter the number :-"))
# if num % 2 == 0:
#     print(f"{num} is even number. ")
# else:
#     print(f"{num} is odd number. ")

# Check the number is Positive, negative, or Zero.
# num = int(input("Enter The Number :-"))
# if num == 0:
#     print(f"{num} is zero ")
# elif num > 0:
#     print((f"{num} is positive Number "))
# else:
#     print(f"{num}is Negative Number ")

# Reverse the number using for and while both a = 12345
# num = [12345]

# check the number palindrome or not
# a = int(input("Enter the number :-"))
# rev = ""

# for i in str(a):
#     rev = i + rev

# if str(a) == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# check the number is prime or not
# num = int(input("Enter The Prime Number :-"))
# if num <= 1:
#     print(f"{num} is not prime number")
# else:
#     for i in range (2,num):
#         if num % i == 0:
#             print(f"{num}num is not prime")
#     else:
#         (f"{num} Prime Number")


# print 1 to 100 prime number.
# for num in range(2, 101):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)

# Find Factorial:
# num = 3
# fact = 1
# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial =", fact)

# print Square and cube of particular number.
# num =  5
# square = num**2
# cube = num**3

# print("Square =", square)
# print("Cube =", cube)

# Reverse an string without using slicing.
# str1 = "Python"
# rev = ""
# for i in str1:
#     rev = i + rev
# print(rev)
        
# List
# 1.Print even and odd number from list

# num = [2, 65, 43, 12, 1, 23, 21, 15,27]
# for i in num:
#     if i % 2 == 0:
#         print(f"{i} is even number. ")
#     else:
#         print(f"{i} is odd number. ")

# 2. Count even and odd from list

# num = [2, 65, 43, 12, 1, 23, 21, 15,27]
# even_num = 0
# odd_num = 0
# for i in num:
#     if i % 2 == 0:
#         print(f"{i} is even number. ")
#         even_num = i+1
#     else:
#         print(f"{i} is odd number. ")
#         odd_num += 1

# print(even_num)
# print(odd_num)

# 3. reverse the list without using predefined function.

# num = [2, 65, 43, 12, 1, 23, 21, 15, 27]
# rev = []
# for i in num:
#     rev = [i] + rev
# print(rev)

# 4.print prime number from list
# num = [12, 43, 53, 2, 3, 4, 21, 13, 16]
# for i in num:
#     count = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count += 1

#     if count == 2:
#         print(i, "is Prime")
#     else:
#         print(i, "is Not Prime")

# 5. print only string from list.
# a = ["ram", 23, "hello", 21, 45, 82, "hello World", 54]
# for ele in a:
#     if isinstance(ele, str):
#         print(ele)

# 6.  print only int from list.
# a = ["ram", 23, "hello", 21, 45, 82, "hello World", 54]
# for ele in a:
#     if isinstance(ele, int):
#         print(ele)

# Tuple
# 1. Find max
# a = (12, 32, 43, 23, 17, 87, 45, 90)
# b = list(a)
# print(a)
# max_num = max(a)
# print(max_num)

#2. find min in tuple

# a = (12, 32, 43, 23, 17, 87, 45, 90)
# b = list(a)
# print(a)
# min_num = min(a)
# print(min_num)

# 3. find sum in tuple.
# a = (12, 32, 43, 23, 17, 87, 45, 90)
# b = list(a)
# print(a)
# sum_num = sum(a)
# print(sum_num)

# 4. find the length of a tuple without using len()
# a = (12, 43, 53, 2, 3, 4)
# b = 0
# for i in a:
#     b += 1

# print("Length:", b)

#5. Find the sum of tuple elements
# a = (12, 43, 53, 2, 3, 4)
# b = 0
# for i in a:
#     b += i
# print("Sum:", b)

# 6. Display only Even  numbers from a tuple
# a = (12, 43, 53, 2, 3, 4)

# for b in a:
#     if b % 2 == 0:
#         print(b)

# dict
# 1. display all keys and values of a dictionary
# a = {"name": "Vaishnavi", "age": 20, "city": "Pune"}
# for i, j in a.items():
#     print(i, j)

# 2. find the total marks of all student
# a = {"Rahul": 80, "Priya": 90, "Amit": 70}

# total = 0
# for i in a.values():
#     total += i

# print("Total Marks:", total)

# 3.Display students who scored above 60
# a = {"Rahul": 80, "Priya": 50, "Amit": 70}

# for i, b in a.items():
#     if b > 60:
#         print(i, b)

# 4. count the number of student who passed
# a = {"Rahul": 80, "Priya": 30, "Amit": 70, "Neha": 45}
# count = 0
# for i in a.values():
#     if i >= 35:
#         count += 1
# print("Passed Students:", count)

# 5. find the highest marks in a dictionary
a = {"Rahul": 80, "Priya": 50, "Amit": 70}

for i, b in a.items():
    if b < 60:
        print(i, b)