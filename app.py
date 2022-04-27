from donations_pkg.homepage import show_homepage,donate,show_donations
from donations_pkg.user import login,register

# Variable Holders
donation_string = ""
username = " "
password = " "
database = {}
donations = []
authorized_user = ""

# Start of the Program

show_homepage(authorized_user)

while True: # User Inputs
    user_choice = input("Choose an option: ")
    if user_choice == "1":      # Login
        authorized_user = login(database,username,password)
        show_homepage(authorized_user)

    elif user_choice == "2":        # Register
        authorized_user = register(database,username)
        show_homepage(authorized_user)
    elif user_choice == "3":        # Donate
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations += donation_string
        show_homepage(authorized_user)

    elif user_choice == "4":        # Donations
        show_donations(donations)
        show_homepage(authorized_user)

    elif user_choice == "5":        # Exit
        print("Have a Nice Day!")
        break