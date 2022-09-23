# Python program to convert decimal to binary
from re import A


def decimalToBinary(n):
	return bin(n).replace("0b", "")
if __name__ == '__main__':
    A=int(input("enter first decimal number"))
    B=int(input("enter second decimal number"))
    C=int(input("enter the third decimal number"))
    print(decimalToBinary(A))
    print(decimalToBinary(B))
    print(decimalToBinary(C))

	#print(decimalToBinary(8))
	#print(decimalToBinary(18))
	#print(decimalToBinary(7))
