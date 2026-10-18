import random

sources = ["Pune Station", "Swargate", "Hinjawadi"]
destinations = ["Shivajinagar", "Kothrud", "Wakad"]
distances = [5, 8, 10]

cab_types = ["Auto", "Sedan", "SUV"]
rates = [12, 18, 25]

while True:
    print("\n=== Cab Booking Chatbot ===")
    print("1. Book Ride")
    print("2. Exit")

    menu_choice = input("Enter your choice: ")

    if menu_choice == "2":
        print("Thank you for using the Cab Booking Chatbot. Goodbye!")
        break
    elif menu_choice != "1":
        print("Invalid choice. Please select 1 or 2.")
        continue

    print("\nChoose cab type:")
    for i in range(len(cab_types)):
        print(f"{i + 1}. {cab_types[i]} (₹{rates[i]}/km)")

    cab_choice = input("Enter cab choice: ")
    if not cab_choice.isdigit() or not 1 <= int(cab_choice) <= len(cab_types):
        print("Invalid cab choice. Returning to the main menu.")
        continue

    print("\nChoose a route:")
    for i in range(len(sources)):
        print(
            f"{i + 1}. {sources[i]} to {destinations[i]} "
            f"({distances[i]} km)"
        )

    route_choice = input("Enter route choice: ")
    if not route_choice.isdigit() or not 1 <= int(route_choice) <= len(sources):
        print("Invalid route choice. Returning to the main menu.")
        continue

    cab_index = int(cab_choice) - 1
    route_index = int(route_choice) - 1
    fare = rates[cab_index] * distances[route_index]

    print("\n=== Ride Details ===")
    print(f"Cab type: {cab_types[cab_index]}")
    print(f"Source: {sources[route_index]}")
    print(f"Destination: {destinations[route_index]}")
    print(f"Distance: {distances[route_index]} km")
    print(f"Rate: ₹{rates[cab_index]}/km")
    print(f"Total fare: ₹{fare}")

    print("\n1. Confirm & Share OTP")
    print("2. Cancel Ride")
    confirm_choice = input("Enter your choice: ")

    if confirm_choice == "2":
        print("Ride cancelled. No OTP was shared.")
    elif confirm_choice == "1":
        otp = random.randint(1000, 9999)
        print(f"Your OTP is: {otp}")
        print("Cancellation is not allowed after the OTP is shared.")
        print("Booking confirmed!")
    else:
        print("Invalid choice. Ride cancelled. No OTP was shared.")