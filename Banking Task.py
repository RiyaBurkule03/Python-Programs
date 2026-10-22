import math

balance = 10_000

print("Welcome to Kiran Bank")
print(f"Opening Balance: ₹{balance:.2f}")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        print(f"Current Balance: ₹{balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: ").strip())
            if not math.isfinite(amount) or amount <= 0:
                print("Invalid amount. Please enter an amount greater than 0.")
            else:
                balance += amount
                print("Deposit successful.")
                print(f"Updated Balance: ₹{balance:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: ").strip())
            if not math.isfinite(amount) or amount <= 0:
                print("Invalid amount. Please enter an amount greater than 0.")
            elif amount > balance:
                print("Transaction failed: Insufficient balance.")
                print(f"Current Balance: ₹{balance:.2f}")
            else:
                balance -= amount
                print("Withdrawal successful.")
                print(f"Updated Balance: ₹{balance:.2f}")
        except ValueError:
            print("Invalid amount. Please enter a valid number.")

    elif choice == "4":
        print("Thank you for banking with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")