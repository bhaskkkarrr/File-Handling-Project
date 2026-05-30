import random
# a="Hello World"
# print(a[0:6:3])

"""OPERATORS"""
# print(126 > 130)
# print((456 == 456) != (235 == 236))
# print(12 < 10 or 45 == 56 or 69 > 70 or 15 != 13)
# print(True and bool(0))


# gender = input("Enter your gender");
# if gender[0] == "M":
#   print("Hey male")
# elif gender[0] == "F":
#   print("Hey female")  
# else:
#   print("Enter only Male or Female")  


# LEAP YEAR
# year = int(input("Enter a year"))

# if year % 100 == 0 and year % 400 == 0:
#     print("It is a leap  year")
# elif year % 100 != 0 and year % 4 == 0:
#     print("It is a leap  year")
# else:
#     print("It is not a leap year")  


"""LOOPS"""
# for i in range(1,11):
#   print(f"5 x {i} = {i*5} ")

# n = int(input("Enter a number: "))
# for i in range(n,n*10+1,n):
#   print(i)

# name = "Bhaskar Chauhan"
# print(len(name))

# FACTORIAL
# factorial = 1
# n = int(input("Enter a number: "))

# for i in range(n, 0, -1):
#   factorial *= i

# print(factorial)  

# SUM OF ODD EVEN
# oddSum = 0
# evenSum = 0
# n = int(input("Enter a number: "))
# for i in range(n):
#   if i % 2 == 0:
#     evenSum += i
#   else:
#     oddSum += i  

# print(f"Sum of even numbers is {evenSum} \nSum of oddd numbers is {oddSum}")

# FACTORS OF A NUMBER
# n = int(input("Enter a number: "))
# for i in range(1,n+1):
#   if n % i == 0:
#     print(i)

# CHECK FOR PERFECT NUMBER
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n):
#   if n % i == 0:
#     sum += i

# if sum == n:
#   print(f"{n} is a perfect number")    
# else:
#   print(f"{n} is not a perfect number")     
 
#PRIME CHECK
# n = int(input("Enter a number: "))
# flag = 0

# for i in range(2,n):
#   if n % i == 0:
#     flag = 1

# if flag == 1:
#   print(f"{n} is not a prime number")
# else:
#   print(f"{n} is a prime number")


# REVERSE STRING
# revS = ""
# s = input("Enter a string: ")
# for i in range(len(s)-1,-1,-1):
#   revS += s[i]

# print(f"Reversed string: {revS}")

# PALINDROME STRING
# s = input("Enter a string: ")
# revS = ""
# for i in range(len(s)-1, -1, -1):
#   revS += s[i]
# if revS == s:
#   print("String is Palindrome")  
# else:
#   print(f"{revS} is not a palindrome")


# WHILE LOOP
# n = int(input("Enter a digit: "))
# while n > 0:
#   print(n % 10)
#   n //= 10


# n = int(input("Enter a digit: "))
# revInt = ""
# while n > 0:
#   digit = str(n % 10)
#   revInt += digit
#   n //= 10

# print("Reversed: ",revInt)  
# if str(n) == revInt:
#   print("Palindrome")  
# else:
#   print("Not palindrome") 

# num = random.randint(1,10)
# print("Number to guess", num)
# n = int(input("Enter a number: "))
# while True:
#   if num > n:
#     n = int(input("Guess a bigger number: "))
#   elif num < n:
#     n = int(input("Guess a smaller number: "))
#   else:
#     print("Number guessed !!!!")
#     break
    

# DATA STRUCTURES
# LIST
# l = [32,33,34,34,32,21,65,23]
# s = 0
# for i in l:
#   s += i

# print(f"Average is: {s/len(l)}")

# largest = l[0]
# idx = 0
# for i in range(len(l)):
#   if l[i] > largest:
#     largest = l[i]
#     idx = i

# print(f"Largest element is {largest} at {idx}")    


# largest = l[0]
# secLargest = l[0]

# for i in l:
#   if i > largest:
#     secLargest = largest
#     largest = i
#   elif i > secLargest:
#     secLargest = i

# print(f"Second largest element is {secLargest}") 

# flag = 1
# prevElement = l[0]
# for i in l:
#   if prevElement > i:
#     flag = 0
#     break

#   prevElement = i  

# if flag == 1:
#   print("List is sorted") 
# else:
#   print("List is not sorted") 


# DICTONARY
# d = {1:100,2:200,3:300,4:450}
# for i in d:
#   print(d[i])

# help(dict)

# d1 = {1:100,2:200,3:300,4:450}
# d2 = {4:100,6:120,7:300,8:450}
# for i in d2:
#   d1[i] = d2[i]

# print(d1)  

# d = { 1:100,2:200,3:300,4:450}
# sum = 0
# for i in d:
#   sum += d[i]

# print(sum)  

# l = [1,1,1,1,12,2,2,3,4,4,3,23,2,3,4,4]
# d={}
# for i in l:
#   if i in d.keys():
#     d[i] += 1
#   else:
#     d[i] = 1

# for i in d:
#   print(f"{i}:{d[i]}")

# d1 = {1:10, 2:20, 3:30}
# d2 = {3:40, 4: 60, 2: 10}

# for i in d2:
#   if i in d1.keys():
#     d1[i] += d2[i]
#   else:
#     d1[i] = d2[i]
    
# print(d1)  