class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name
        return name

    def change_pin(self, pin):
        self.pin = pin
        return pin

    def change_password(self, password):
        self.password = password
        return password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of: ", self.balance)

    def withdraw(self, withdraw):
        self.balance -= withdraw

    def deposit(self, deposit):
        self.balance += deposit

    def transfer_money(self, amount, otheruser):
        print("\nYou are transferring $" + str(amount), "to", otheruser.name)
        print("Authentication required")
        pin = int(input("Enter your PIN: "))
        if self.pin == pin:
            print("Transfer authorized")
            print("Transferring $" + str(amount), "to", otheruser.name)
            self.balance -= amount
            otheruser.balance += amount
        else:
            print("Invalid PIN. Transaction canceled")

    def request_money(self, amount, otheruser):
        print("\nYou are requesting $" + str(amount), "from", otheruser.name)
        print("User authentication is required...")
        pin = int(input("Enter " + otheruser.name + "'s PIN: "))

        if otheruser.pin == pin:
            password = input("Enter your password: ")
            if self.password == password:
                self.balance += amount
                otheruser.balance -= amount
                print("Request authorized")
                print(otheruser.name + " sent $" + str(amount))
        elif otheruser.pin == pin:
            password = input("Enter your password: ")
            if self.password != password:
                print("Invalid password. Transaction canceled.")
        else:
            print("Invalid PIN. Transaction canceled.")


"""user1 = User("Bob", 1234, "password")


print(user1.name, user1.pin, user1.password)  # Task 1

user1.change_name("Mario")
user1.change_pin(2222)
user1.change_password("luigi")
print(user1.name, user1.pin, user1.password)  # Task 2

bankuser1 = BankUser("Bob", 1234, "password")  # Task 3


bankuser1.show_balance()
bankuser1.deposit(1000)
bankuser1.show_balance()
bankuser1.withdraw(500)
bankuser1.show_balance()"""

bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 5678, "alicepassword")

bankuser2.deposit(5000)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser2.transfer_money(500, bankuser1)
bankuser2.show_balance()
bankuser1.show_balance()

bankuser2.request_money(250, bankuser1)
bankuser2.show_balance()
bankuser1.show_balance()
