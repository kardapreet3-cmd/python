print("-----WELCOME TO THE ATM MACHINE...!!-----")
account_inf={
    "Name":"Preet kardao",
    "Email":"kardapreet3@gmail.com",
    "Pin":1234,
    "Mobile":7276180877,
    "ACCOUNT NUMBER":98910000345101,
    "ACCOUNT AVAILABLE BALANCE":5000000000
}

correct_pin = 1234
attempts = 0
while attempts < 3:
    pin = int(input("Enter PIN: "))
    if pin == account_inf["Pin"]:
        print("VALID PIN")
        print("You have login successfully")
        break
    else:
        attempts += 1
        print("INVALID PIN")

if attempts == 3:
    print("Card Blocked! Maximum attempts reached.")
print("please get your choice want you want to do!")
print("1. Check Balance. ")
print("2. Withdraw Amount. ")
print("3. Deposit Amount. ")
print("4. Change PIN. ")
print("5. Account Details. ")
print("6. Exit. ")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Your Bank Account Number is: ", account_inf["ACCOUNT NUMBER"])
    print("Your Bank Account Balance is: ",account_inf["ACCOUNT AVAILABLE BALANCE"])
elif choice == 2:
    print("Your Bank Account Number is: ", account_inf["ACCOUNT NUMBER"])
    print("Available Balance: ", account_inf["ACCOUNT AVAILABLE BALANCE"])
    amount = int(input("Enter your Amount to be withdrawn: "))
    if amount <= account_inf["ACCOUNT AVAILABLE BALANCE"]:
        account_inf["ACCOUNT AVAILABLE BALANCE"] = account_inf["ACCOUNT AVAILABLE BALANCE"] - amount
        print("Withdrawal Successful")
        print("---RECIPT---")
        print("Transaction Successful")
        print("Your Bank Account Number is: ", account_inf["ACCOUNT NUMBER"])
        print("Your Bank Balance is: ", account_inf["ACCOUNT AVAILABLE BALANCE"])
        print("Thank you!!")
    else:
        print("Insufficient Balance")
elif choice == 3:
    print("Your Bank Account Number is: ", account_inf["ACCOUNT NUMBER"])
    print("Your Bank Accout Balance is: ", account_inf["ACCOUNT AVAILABLE BALANCE"])
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        account_inf["ACCOUNT AVAILABLE BALANCE"] += amount
        print("Deposit Successful")
        print("---RECIPT---")
        print("Transaction Successful")
        print("Your Bank Account Name is: ", account_inf["Name"])
        print("Your Bank Account Number is: ", account_inf["ACCOUNT NUMBER"])
        print("Your Bank Balance is: ", account_inf["ACCOUNT AVAILABLE BALANCE"])
        print("Thank you!!")
    else:
        print("Enter a valid amount")
elif choice == 4:
    old_pin = int(input("Enter current PIN: "))
    if old_pin == account_inf["Pin"]:
        new_pin = int(input("Enter new PIN: "))
        confirm_pin = int(input("Confirm new PIN: "))
    if new_pin == confirm_pin:
        account_inf["Pin"] = new_pin
        print("PIN changed successfully")
    elif new_pin != confirm_pin:
        print("PIN confirmation does not match")
    else:
        print("Incorrect current PIN")
elif choice == 5:
    print("-----Your Bank Account Details Are!!-----")
    print(account_inf["Name"])
    print(account_inf["Email"])
    print(account_inf["Mobile"])
    print(account_inf["ACCOUNT NUMBER"])
    print(account_inf["ACCOUNT AVAILABLE BALANCE"])
elif choice == 6:
    print("Exiting...")
    print("---Thank you for using ATM!!---")
else:
    print("Invalid choice")
    print("Enter Vaild choice!!")