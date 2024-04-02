"""Password Cracker"""

input_password = input()
lowercase_count = 0
uppercase_count = 0
digit = 0
if len(input_password) >= 8 and len(input_password) <= 12: 
    for char in input_password:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        elif char.isdigit():
            digit += 1
    if lowercase_count >=3 and uppercase_count >= 2 and digit >= 1:
        print("Valid")
    else:
        print('Invalid')
else:
    print('Invalid')