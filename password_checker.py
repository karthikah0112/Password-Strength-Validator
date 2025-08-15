import re

# Sample list of common weak passwords
weak_passwords = ["password", "123456", "qwerty", "letmein", "admin"]

def check_password(password):
    score = 0
    report = []

    # Length check
    if len(password) >= 12:
        score += 1
    else:
        report.append("Password should be at least 12 characters long.")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        report.append("Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        report.append("Add at least one lowercase letter.")

    # Number check
    if re.search(r"\d", password):
        score += 1
    else:
        report.append("Add at least one number.")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        report.append("Add at least one special character.")

    # Weak password check
    if password.lower() in weak_passwords:
        report.append("Password is too common/weak.")

    return score, report

# User input
password = input("Enter your password: ")
score, report = check_password(password)

print(f"\nPassword Strength Score: {score}/5")
if report:
    print("Suggestions to improve password:")
    for r in report:
        print(f"- {r}")
else:
    print("Your password is strong!")
