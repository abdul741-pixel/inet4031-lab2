# user-processing.py
# reads list-of-users.txt and prints each username

with open("list-of-users.txt", "r") as f:
    for line in f:
        user = line.strip()
        if user:
            print(user)
