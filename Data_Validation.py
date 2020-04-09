# A Python Program to validate users data and generate random passwords from their data.

import string
import random


# This is a Function that stores the inputted user details.

def user_details():

    # Users will be asked to enter their First name, Last name and Email address.

    first_name = input("Please Enter your First Name: ")
    last_name = input("Please Enter your Last Name: ")
    email = input("Please Enter your Email: ")
    info_of_user = [first_name, last_name, email]

    return info_of_user


# This is a Function that generates random letters from the alphabets to form the user password.

def random_password(info_of_user):

    letters = string.ascii_letters
    length = 5
    generated_password = ''.join(random.choice(letters) for i in range(length))

    # The variable 'PASSWORD' is gotten from the first 2 letters of the first name and last 2 letters of the last name.

    password = (info_of_user[0][0:2] + info_of_user[1][-2:])

    # Concatenation of the variable 'PASSWORD' and 'GENERATED_PASSWORD'

    pass_of_user = str(password + generated_password)

    return pass_of_user


# Main Program

user = True
users_container = []

# A while loop set to the Boolean variable 'USER', which will keep running as long as 'USER' remains TRUE.

while user:

    # Get the user details and show the user their auto generated password.

    user_info = user_details()
    user_password = random_password(user_info)
    print("Your Auto Generated Password is: " + str(user_password))

    # Ask the user whether they like the auto generated password.

    like_gen_password = input("""
Do you like the Auto Generated Password? 
If yes, please type YES. If no, please type NO: 
""")

    # This loop explains what happens if the user likes the password and if the user does not like the password

    while like_gen_password.upper() == 'YES':

        # The user auto generated password is added to their information which is then stored in a container

        user_info.append(user_password)
        users_container.append(user_info)

        break

    else:

        # The user is asked to input their preferred password but it should not be less than 7

        user_pref_password = input("Please enter your preferred password not less than 7 characters: ")

        # This loop will keep running until the user inputs the a password with 7 or more characters.

        while len(user_pref_password) < 7:

            # An error message is printed out when the user preferred password is less than 7.
            # The user is asked to input is preferred password again.

            print("ERROR! Your password is less than 7. \n")

            user_pref_password = input("Please enter your preferred password again: ")

        else:

            # The user preferred password is added to their information which is then stored in a container

            user_info.append(user_pref_password)
            users_container.append(user_info)

# Another user details

    another_user = input("Do you want to input another user? If yes, enter YES. If no, enter NO: ")

    # This condition will run the program again asking for the new user details,
    # at the same time keeping the previous user details intact.

    if another_user.upper() == 'YES':

        user = True

    # If there is no new user to input, the user(s) detail(s) will be printed out in a list on the screen.

    else:

        user = False
        for items in users_container:
            print(items)
