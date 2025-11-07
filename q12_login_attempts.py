# q12_login_attempts.py

attempts = 0
password_correct = "pass123"

while attempts < 3:
    entered = input("Enter password: ")
    if entered == password_correct:
        print("Access granted")
        break
    else:
        attempts += 1
        print("Wrong password, try again")

if attempts == 3:
    print("Account locked.")
# This program allows a user to attempt to enter the correct password up to three times before locking the account.