balance = 1000.0
successful_transactions = 0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("0. Exit")
    choice = input("Choose an option: ")

    if choice == "0":
        break
    elif choice not in ("1", "2"):
        print("Invalid option.")
        continue

    amount = float(input("Enter amount (Rs.): "))
    if amount <= 0:
        print("Amount must be positive.")
    elif choice == "1":
        balance += amount
        successful_transactions += 1
        print("Deposit successful.")
    elif choice == "2":
        if amount <= balance:
            balance -= amount
            successful_transactions += 1
            print("Withdrawal successful.")
        else:
            print("Transaction rejected: insufficient balance.")

    print("Current balance: Rs.", round(balance, 2))

print("\n--- Transaction Summary ---")
print("Final balance: Rs.", round(balance, 2))
print("Successful transactions:", successful_transactions)
