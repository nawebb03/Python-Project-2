#Name: Nathan Webb
#Date: 10/25/2019
#Description: Project 2

#Initialize global variable

balance = 1000.00

#Define function menus

def menu():
    print()
    print("*******************************************")
    print("* 1. Balance Inquiry                      *")
    print("* 2. Deposit Funds                        *")
    print("* 3. Withdrawl Funds                      *")
    print("* 4. Exit                                 *")
    print("*******************************************")
    choice = input("Choice ==>")
    while choice != "4":
        if choice == "1":
            print("Checking Balance: $", format(balance,',.2f'),sep='')
            menu()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdrawl()
        elif choice == "4":
            print("Exiting...")
            exit()
        else:
            print("***Invalid Entry***")
            menu()
    else:
        print("Exiting...")
        exit()

#Prompt to enter PIN

def pin_menu():
    print("Welcome to MCC ATM")
    attempts = 1
    while attempts <= 3:
        attempts = attempts + 1
        PIN = int(input("Enter your PIN:"))
        if PIN == 1234:
            menu()
            break
        else:
            print("***Invalid PIN Entered***")
            continue
    else:
        print("Invalid PIN entered 3 times. Exiting Program.")

#Deposit prompt

def deposit():
    global balance
    deposit = int(input("Deposit Amount:"))
    balance = balance + deposit
    menu()

#Withdrawl prompt

def withdrawl():
    global balance
    withdrawl = int(input("Withdrawl Amount:"))
    if withdrawl <= balance:
        if withdrawl % 10 != 0:  #Ensure that amount is multiple of 10
            print("Invalid Withdrawl Amount, Must be denomination of 10")
            menu()
        else:
            balance = balance - withdrawl
            menu()
    else:
        print("***Not Sufficient Funds in Checking Account***")
        menu()

#Start program by calling initial menu

pin_menu()
