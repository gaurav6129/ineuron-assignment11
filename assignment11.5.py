#Write a python script to calculate sum of first N Even natural numbers
num = int(input("Print sum of even numbers : "))
sum = 0
for i in range(1, num + 1):
    if((i % 2) == 0):
        sum += i

print("\nSum of even numbers from 1 to", num, "is :", sum)