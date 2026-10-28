import Functions 

print("\nWelcome to Carter's Bank\n")

name = input("Please enter your name: \n")
account = Functions.BankAccount(name, 0)  # created once, starting balance 0

while True:
    try:
        option = int(input("\nPlease choose an option:\n" \
            "1. Deposit\n" \
            "2. Withdraw\n" \
            "3. Account Information\n" \
            "4. Quit\n\n"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if option == 1:
        account.deposit(0)
    elif option == 2:
        account.withdraw(0)
    elif option == 3:
        print(account.account_information())
    elif option == 4:
        account.quit()
    else:
        print("Invalid option. Please try again.")