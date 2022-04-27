# Program Screen 
def show_homepage(authorized_user):
    print("        === DonateMe Homepage ===     ")
    print("--------------------------------------------")
    print("| 1.   Login        | 2.    Register        |")
    print("--------------------------------------------")
    print("| 3.   Donate       | 4.    Show Donations  |")
    print("--------------------------------------------")
    print("|                5. Exit                    |")
    print("--------------------------------------------")
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}")

# Donate Function
def donate(username):
    donation_amt = input("\nEnter amount to donate: ")
    donation_string = [f"{username} donated ${float(donation_amt)}."]
    print("Thank You for your donation!\n")
    return donation_string

# Donation list Function
def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently there are no donations.\n")
    else:
        for donated in donations:
            print(donated)
