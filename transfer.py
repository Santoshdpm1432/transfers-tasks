# Write a Python program that takes a list of numbers as input numbers = [25, 30,
# 20, 40, 15, 25] and prints the sum of the numbers. However, if the sum exceeds
# 100, stop adding numbers and print "Sum exceeded 100".

# sum = 0
# numbers = [25, 30, 20, 40, 15, 25]
# for i in numbers :
#     sum +=i
#     if sum >100:
#         print("sum is exceeded ")
#         break
# print(f"sum of the number is {sum}")

# Write a Python script that uses a for loop to iterate through numbers from 1 to
# 600. Print only the odd numbers, skipping the even ones using the continue
# statement.

# for i in range (1,601,2):
#     for j in range(2,i):
#         if i%j == 0:
#             continue
#     print(i)

# Write a Python script that checks if a number is even or odd. If the number is
# even, print "Even"; if odd, do nothing (use the pass statement).

# first_number = int(input("enter a first number :"))
# second_number = int(input("enter a second number :"))
# for i in range(first_number,second_number):
#     if i%2 == 0:
#         print(f"{i} is even number")
#     else:
#         pass

# Write a Python script that iterates through a list of words. If the word is "break,"
# exit the loop using the break statement. If the word is "skip," skip the rest of the
# code for the current iteration using the continue statement. For any other word,
# print the word

names = ["santosh","ashok","nagaprasad","break","skip"]

for i in names:
    if i == "break":
        print(f"{i} found, breaking the loop")
        break
    elif i == "skip":
        print(f"{i} found, skipping the loop")
        continue
    else:
        pass
    print(f"{i} found")
