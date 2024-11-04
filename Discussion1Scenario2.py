correct_password = "secure123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        attempts += 1
        print("Incorrect password. Try again.")

if attempts == max_attempts:
    print("Account locked due to too many failed attempts.")
