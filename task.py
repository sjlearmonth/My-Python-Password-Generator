import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

total_number_of_characters = nr_letters + nr_symbols + nr_numbers
password = ""

for index in range(0, total_number_of_characters):
    character = random.randint(0, 2)
    if character == 0 and nr_letters > 0:
        next_random_character = letters[random.randint(0, len(letters))]
        nr_letters -= 1
    elif character == 1 and nr_symbols > 0:
        next_random_character = symbols[random.randint(0, len(symbols))]
        nr_symbols -= 1
    elif nr_numbers > 0:
        next_random_character = numbers[random.randint(0, len(numbers))]
        nr_numbers -= 1
    password += next_random_character
print("Your randompassword is: " + password)







