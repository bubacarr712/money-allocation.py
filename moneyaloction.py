import time
import os
import sys

print("......................................")
print("Welcome to the money Alocation program")
print("......................................")
#this loop block is to avoid crashing of the code

while True:
    while True:
        try:
            Total_Sale = int(input("Please enter your total sale amount:.."))
            print("enter the amount you have on the following notes.\n")
        except ValueError:
            print("What you enter may contain (letter)s")
            print("Please Enter a number")
        else:
            break
    Data = [200,100,50,25,20,10,5]
    GMT = 0
    for i in range(len(Data)):
        print(Data[i], "x ",end="")
        while True:
            try:
                Notes = int(input())
            except ValueError:
                print("Please Enter a Number")
                print(Data[i], "x ",end="")
            else:
                break
        Total = Data[i] * Notes
        print("D{0:,d}".format(Total))
        GMT = Total + GMT
    print("your total amount is. ","D{0:,d}".format(GMT),'\n')
    if Total_Sale > GMT:
        print("You have a shortage of ","D{0:,d}".format (Total_Sale - GMT),"\n")
        print("Please recount your money properly")
    elif Total_Sale < GMT:
        print("you have a surplus of ","D{0:,d}".format(GMT - Total_Sale),"\n")
        print("Please recount your money properly\n")
    else:
        print("your money is talley please Bank it\n")
        sys.exit()
    print("do you want restart your Allocation \n Choose!! ")
    print("Yes(Y) Or No(n)")
    option = input()
    if option.lower() == "yes" or option == "y":
        continue
    elif option.lower() == "no" or option == "n":
        break

