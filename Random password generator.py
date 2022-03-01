import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

print()
print("Welcome to Randy's Random Password Generator")
print()
print()
while 1:
    question = input("Would you like to generate a random password? (yes or no): ")
    print()
    if question == "no" or question == "n" or question == 'N' or question == 'No' or question == 'NO':
        print("Thank you for considering Randy's. Now leaving Randy's random password generator App")
        quit()

    if question == "yes" or question == "y" or question == 'Y' or question == 'Yes' or question == 'YES':
            print()
            password_Length = int(input("How long would you like your password to be? (password character length): "))
            print()
            num_of_passwords = int(input("How many passwords would you like to create?: "))
            print()
            for i in range(0, num_of_passwords):
                password = " "
                for i in range(0, password_Length):
                    password_Char = random.choice(chars)
                    password = password + password_Char
                print('Your password is: ', password)
                print()
            continue


        