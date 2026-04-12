import json
import time
import getpass  # cross-platform secure password input

# Store admin credentials
ADMIN_NAME = "James Mwanri"
ADMIN_PASSWORD = "Password!2004@"

# File to store customer data
DATA_FILE = "customers_data.json"

# Dictionary to store customers
customers = {}

# Function to save customers to a file
def save_customers_to_file():
    with open(DATA_FILE, 'w') as file:
        json.dump(customers, file, indent=4)
    print("Customer data saved successfully.")

# Function to load customers from a file
def load_customers_from_file():
    global customers
    try:
        with open(DATA_FILE, 'r') as file:
            customers = json.load(file)
        print("Customer data loaded successfully.")
    except FileNotFoundError:
        print("No existing data found. Starting fresh.")
    except json.JSONDecodeError:
        print("Data file is corrupted. Starting fresh.")

# Function to verify admin securely
def secure_input(prompt="Enter password: "):
    return getpass.getpass(prompt)

def admin_login():
    name = input("Enter admin name: ")
    password = secure_input("Enter admin password: ")
    if name == ADMIN_NAME and password == ADMIN_PASSWORD:
        print("Admin logged in successfully!")
        return True
    else:
        print("Invalid admin credentials. Access denied.")
        return False

# Admin functions
def view_customers():
    if customers:
        print("Customers List:")
        for acc_num, details in customers.items():
            print(f"Account Number: {acc_num}, Name: {details['name']}, Balance: {details['balance']}")
    else:
        print("No customers found.")

def delete_customer():
    acc_num = input("Enter account number to delete: ")
    if acc_num in customers:
        del customers[acc_num]
        save_customers_to_file()
        print("Customer deleted successfully.")
    else:
        print("Customer not found.")

# User registration
def register_customer():
    print("Registering a new customer...")
    name = input("Enter your name: ")
    acc_num = input("Enter your account number: ")
    acc_type = input("Enter account type (e.g., savings, checking): ")
    initial_amount = float(input("Enter initial deposit amount: "))
    password = secure_input("Create a password for your account: ")
    
    customers[acc_num] = {
        "name": name,
        "type": acc_type,
        "balance": initial_amount,
        "password": password
    }
    save_customers_to_file()
    print(f"Customer {name} registered successfully!")

# Customer login
def customer_login():
    acc_num = input("Enter your account number: ")
    if acc_num in customers:
        password = secure_input("Enter your password: ")
        if customers[acc_num]["password"] == password:
            print(f"Welcome back, {customers[acc_num]['name']}!")
            return acc_num
        else:
            print("Incorrect password.")
    else:
        print("Account not found.")
    return None

# Customer functions
def add_balance(acc_num):
    amount = float(input("Enter the amount to add: "))
    customers[acc_num]["balance"] += amount
    save_customers_to_file()
    print("Balance updated successfully.")

def check_balance(acc_num):
    print(f"Your current balance is: {customers[acc_num]['balance']}")

def withdraw_balance(acc_num):
    amount = float(input("Enter the amount to withdraw: "))
    if customers[acc_num]["balance"] >= amount:
        customers[acc_num]["balance"] -= amount
        save_customers_to_file()
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")

# Main menu
def main_menu():
    load_customers_from_file()
    while True:
        print("\nWelcome to the Banking System")
        print("1. Admin Login")
        print("2. Register as a Customer")
        print("3. Customer Login")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            if admin_login():
                while True:
                    print("\nAdmin Menu")
                    print("1. View Customers")
                    print("2. Delete Customer")
                    print("3. Logout")
                    admin_choice = input("Choose an option: ")

                    if admin_choice == "1":
                        view_customers()
                    elif admin_choice == "2":
                        delete_customer()
                    elif admin_choice == "3":
                        break
                    else:
                        print("Invalid option. Please try again.")

        elif choice == "2":
            register_customer()

        elif choice == "3":
            acc_num = customer_login()
            if acc_num:
                while True:
                    print("\nCustomer Menu")
                    print("1. Add Balance")
                    print("2. Check Balance")
                    print("3. Withdraw Balance")
                    print("4. Logout")
                    user_choice = input("Choose an option: ")

                    if user_choice == "1":
                        add_balance(acc_num)
                    elif user_choice == "2":
                        check_balance(acc_num)
                    elif user_choice == "3":
                        withdraw_balance(acc_num)
                    elif user_choice == "4":
                        break
                    else:
                        print("Invalid option. Please try again.")

        elif choice == "4":
            print("Thank you for using the banking system. Goodbye!")
            save_customers_to_file()
            break

        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
