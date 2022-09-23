#Write a python script to count digits in a given number
num=int(input("enter the number"))
#num = 3452
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))