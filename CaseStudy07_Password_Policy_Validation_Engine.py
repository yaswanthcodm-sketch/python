password = input("Enter a sample password to check: ")
errors = []

if len(password) < 8:
    errors.append("Use at least 8 characters.")
if not any(ch.isupper() for ch in password):
    errors.append("Include at least one uppercase letter.")
if not any(ch.islower() for ch in password):
    errors.append("Include at least one lowercase letter.")
if not any(ch.isdigit() for ch in password):
    errors.append("Include at least one digit.")
if " " in password:
    errors.append("Do not include spaces.")

if len(errors) == 0:
    print("Result: Sample password meets all classroom rules.")
else:
    print("Result: Sample password does not meet the rules.")
    for error in errors:
        print("-", error)
