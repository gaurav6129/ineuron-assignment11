#Write a python script to calculate sum of digits of a given number
def getSum(n):
    sum = 0
    for digit in str(n):
      sum += int(digit)
    return sum
n=int(input("enter the number"))
#n = 123456778
print(getSum(n))
