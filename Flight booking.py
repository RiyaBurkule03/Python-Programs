class Flight:
    def __init__(self, code, source, destination, seats, fare):
        self.code = code
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare


class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10


class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets
        self.subtotal = flight.fare * tickets
        self.discount = self.subtotal * passenger.get_discount()
        self.total = self.subtotal - self.discount

    def show_summary(self):
        print("\nBooking confirmed!")
        print("Booking ID:", self.booking_id)
        print("Flight:", self.flight.code)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Passenger:", self.passenger.name)
        print("Passenger type:", type(self.passenger).__name__.replace("Passenger", ""))
        print("Tickets:", self.tickets)
        print(f"Base fare per ticket: ₹{self.flight.fare:.2f}")
        print(f"Subtotal: ₹{self.subtotal:.2f}")
        print(f"Discount: ₹{self.discount:.2f}")
        print(f"Final amount: ₹{self.total:.2f}")


class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "Mumbai", "Bengaluru", 25, 3500),
            Flight("PN303", "Pune", "Hyderabad", 18, 3000),
        ]
        self.booking = None

    def view_flights(self):
        print("\nAvailable Flights")
        for flight in self.flights:
            print(
                flight.code, "|", flight.source, "to", flight.destination,
                "| Seats:", flight.seats, "| Fare: ₹", flight.fare
            )

    def book_flight(self):
        code = input("Enter flight code: ").strip().upper()

        flight = None
        for item in self.flights:
            if item.code == code:
                flight = item
                break

        if flight is None:
            print("Flight code not found.")
            return

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter age: "))
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Age and ticket count must be whole numbers.")
            return

        passenger_type = input("Passenger type (Regular/Student): ").strip().lower()

        if not name:
            print("Passenger name cannot be blank.")
        elif age <= 0:
            print("Age must be greater than 0.")
        elif tickets <= 0:
            print("Ticket count must be greater than 0.")
        elif tickets > flight.seats:
            print("Booking failed: Not enough seats available.")
        elif passenger_type not in ("regular", "student"):
            print("Please enter Regular or Student.")
        else:
            if passenger_type == "student":
                passenger = StudentPassenger(name, age)
            else:
                passenger = Passenger(name, age)

            flight.seats -= tickets
            self.booking = Booking("BK1001", flight, passenger, tickets)
            self.booking.show_summary()

    def view_booking(self):
        if self.booking is None:
            print("There are no confirmed bookings yet.")
        else:
            self.booking.show_summary()

    def run(self):
        print("Welcome to Kiran Air Booking")

        while True:
            print("\n1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.view_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please choose 1, 2, 3, or 4.")


app = FlightBookingSystem()
app.run()