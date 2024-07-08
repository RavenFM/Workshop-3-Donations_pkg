def login(database, username, password):
    if username in database and database[username] == password:
        print(f"Welcome back {username}!")
        return username
    elif username in database and database[username] != password:
        print("Password incorrect.")
        return ""
    else:
        print("Username not found.")
        return ""

def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print(f"Username {username} registered.")
        return username