#   Login Function
def login(database,username,password):
    username = input("\nEnter Username: ")
    password = input("Enter Password: ")
    if database[username] == password:
        print(f"Welcome back {username}!\n")
        return username
    elif database[username] != password:
        print(f"Incorrect password for {'username'}\n")
        return ""
    else:
        print("User not found. Please register.\n")
        return ""
#   Register Funciton
def register(database,username):

    username = input("\nEnter Username: ")
    password = input("Enter Password: ")
    if username in list(database.keys()):   # Checks all keys(usernames) in the database
        print("Username already registered.\n")
        return ""
    else:
        database[username] = password       # Creates the key:value in the database
        print(f"Username {username} registered!\n")
        return 

