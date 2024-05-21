def check_password_complexity(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    elif not any(c.isupper() for c in password):
        return "Weak: Password must contain at least one uppercase letter."
    elif not any(c.islower() for c in password):
        return "Weak: Password must contain at least one lowercase letter."
    elif not any(c.isdigit() for c in password):
        return "Weak: Password must contain at least one digit."
    elif not any(c in "$@#&!" for c in password):
        return "Weak: Password must contain at least one special character ($, @, #, or !)."
    else:
        return "Strong: Password meets complexity requirements."

user_password = input("Enter your password: ")
result = check_password_complexity(user_password)
print(result)
