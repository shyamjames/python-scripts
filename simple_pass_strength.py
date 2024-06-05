print("Welcome to Password Strength Checker")

password = input("Enter your password: ")
length = len(password)


def has_all_char(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special_char = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special_char = True
    return has_upper and has_lower and has_digit and has_special_char

if length>8:
    if has_all_char(password):
        print("String Password")
    else:
        print("Password is missing some character types!")
else:
    print("Weak password: password length less than 8 characters")