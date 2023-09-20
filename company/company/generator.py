import random

def generate_random_phone_number(code):
    # Country code for Uzbekistan
    country_code = "+998"

    # Generate the first two digits (xx) for the local number
    first_two_digits = str(code)

    # Generate the next three digits (xxx) for the local number
    next_three_digits = str(random.randint(100, 999))

    next_two_digits = str(random.randint(10, 99))


    # Generate the last two digits (xx) for the local number
    last_two_digits = str(random.randint(10, 99))

    # Combine the parts to create the phone number
    phone_number = f"{country_code} {first_two_digits} {next_three_digits} {next_two_digits} {last_two_digits}"
    
    return phone_number

# Number of phone numbers to generate
num_phone_numbers = 10000

# Generate random phone numbers and write them to a file
companies = ["Beeline.txt", "Ucell.txt", "MobiUz.txt", "Uzmobile.txt"]
codes = [99, 98]
with open("Uzmobile.txt", "w") as file:
    for _ in range(num_phone_numbers):
        random_phone_number = generate_random_phone_number(codes[_%2])
        file.write(random_phone_number + "\n")

print(f"{num_phone_numbers} random phone numbers have been written ")
