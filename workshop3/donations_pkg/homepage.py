def show_homepage():
    print("         === Donate Me Homepage ===          ")
    print("------------------------------------------")
    print("| 1.    Login       | 2.    Register     |")
    print("------------------------------------------")
    print("| 3.    Donate      | 4.  Show Donations |")
    print("------------------------------------------")
    print("|                  5. Exit               |")
    print("------------------------------------------")

def donate(username):
    donation_amt = input("Enter amount to donate: ")
    donation_string = f"{username} donated ${donation_amt}"
    print("Thank you for your donation!")
    return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")
    if not donations:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
