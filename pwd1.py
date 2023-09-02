
import string
import getpass

def check_password_strength(password):
    # Define criteria for password strength
    length_criteria = 15
    uppercase_criteria = 1
    lowercase_criteria = 1
    digit_criteria = 1
    special_character_criteria = 1

    # Check length
    if len(password) < length_criteria:
        return "Weak: Password should be at least 8 characters long."

    # Check uppercase letters
    if sum(1 for char in password if char.isupper()) < uppercase_criteria:
        return "Weak: Password should contain at least 1 uppercase letter."

    # Check lowercase letters
    if sum(1 for char in password if char.islower()) < lowercase_criteria:
        return "Weak: Password should contain at least 1 lowercase letter."

    # Check digits
    if sum(1 for char in password if char.isdigit()) < digit_criteria:
        return "Weak: Password should contain at least 1 digit."

    # Check special characters
    if sum(1 for char in password if not char.isalnum()) < special_character_criteria:
        return "Weak: Password should contain at least 1 special character."

    return "Strong: Password is strong."

# Test the function with a password
password_to_check = "P@ssword22"
result = check_password_strength(password_to_check)
print(result)