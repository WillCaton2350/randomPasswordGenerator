import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

print()
print("Password Generator")
print()
print()
while 1:
    question = input("Generate a random password? (yes or no): ")
    print()
    if question == "no" or question == "n" or question == 'N' or question == 'No' or question == 'NO':
        print("Exiting...")
        quit()

    if question == "yes" or question == "y" or question == 'Y' or question == 'Yes' or question == 'YES':
            print()
            password_Length = int(input("Password character length: "))
            print()
            num_of_passwords = int(input("Number of Passwords: "))
            print()
            for i in range(0, num_of_passwords):
                password = " "
                for i in range(0, password_Length):
                    password_Char = random.choice(chars)
                    password = password + password_Char
                print('Your password is: ', password)
                print()
            continue   


        
