from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
donations_total = {"admin": 0}  

def login(database, username, password):
    username_lower = username.lower() 
    if username_lower in database and database[username_lower] == password:
        return username_lower 
    else:
        return ""

def register(database, username, password):
    username_lower = username.lower()  
    if len(username) > 10:
        print("Username must not exceed 10 characters.")
        return ""
    elif len(password) < 5:
        print("Password must be at least 5 characters long.")
        return ""
    elif username_lower in database:
        print("Username already exists.")
        return ""
    else:
        database[username_lower] = password
        donations_total[username_lower] = 0
        return username_lower  

while True:
    show_homepage()
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("Login:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authorized_user = login(database, username, password)
        if authorized_user != "":
            print(f"\nLogged in as: {authorized_user}\n")
        else:
            print("Login failed.\n")
    elif choice == '2':
        print("Register:")
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            print("Registration successful!\n")
    elif choice == '3':
        if authorized_user == "":
            print("You are not logged in.\n")
        else:
            donation_amount = float(input("Enter amount to donate: $"))
            donation_string = f"{authorized_user} donated ${donation_amount:.2f}"
            donations.append(donation_string)
            donations_total[authorized_user] += donation_amount
    elif choice == '4':
        if not donations:
            print("No donations made yet.\n")
        else:
            show_donations(donations)
            total_donations = sum(float(donation.split('$')[1]) for donation in donations)
            print(f"\nTotal of donations: ${total_donations:.2f}\n")
    elif choice == '5':
        print("Total Donations for Each User:")
        for user, total in donations_total.items():
            print(f"{user}: ${total:.2f}")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.\n")
