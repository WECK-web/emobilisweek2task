# q11_dictionary_access.py

user_profile = {
    "name": "Jane Doe",
    "email": "jane@example.com",
    "verified": False
}

answer = input("Has the user verified their account? (yes/no): ").lower()

if answer == "yes":
    user_profile["verified"] = True
    print("Updated profile:", user_profile)
else:
    print("Verification pending.")
