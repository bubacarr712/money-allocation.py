import time
import os
import sys

"""
this program will help you to allocate your money without using a calculator
first you enter your total Amount that have(which is the total Amount)
second you enter  your Dominions starting from D200 to D5)
then you have your result at the bottom 
if it is talley
when the text turn to green means its talley
when the text turn to red means you had a shortage
when the text turn to yellow means you had a surplus

"""


print("......................................")
print("Welcome to the money Alocation program")
print("......................................")
#the loop block is to avoid chrashing of the code if the user enter an string instead a number
#the first loop gives option to the user wether to re-alocate if the total amoun is not talley with the total
#the second and forth loop is input validation(avoid chrashing of the code if a user enter a string

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
        print("\033[01;31mYou have a shortage of ","D{0:,d}".format (Total_Sale - GMT),"\n")
        print("Please recount your money properly")
    elif Total_Sale < GMT:
        print("\033[01;33m you have a surplus of ","D{0:,d}".format(GMT - Total_Sale),"\n")
        print("Please recount your money properly\n")
    else:
        print("\033[01;32m your money is talley please Bank it\n")
        sys.exit()
    print("do you want restart your Allocation \n Choose!! ")
    print("Yes(Y) Or No(n)")
    option = input()
    if option.lower() in ["yes","y"]:
        continue
    elif option.lower() in ["no","n"]:
        break

