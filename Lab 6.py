'''
Andrew Ballard
Group 37
COP3502C
Lisha Zhou
Lab 6: Version Control
'''


def encode(password):
    #this takes each character in password and add 3 to the number
    # if the number turns out to be over 10, then it loops to 0 and continues from there
    encoded_password = ''
    for num in range(len(password)):
        encoded_password += str((int(num)+3)%10)
    #print(encoded_password)  #this is used to test out if function works with input
    return encoded_password



if __name__ == "__main__":

        user_option = 1     # used any number but 3 to enter loop

        while user_option != 3:


            # Menu to be displayed throughout loop
            menu = '''Menu
-------------
1. Encode
2. Decode
3. Quit '''

            print(menu)
            print()

            user_option = int(input('Please enter and option: '))
            if user_option == 1:
                user_password = input('Please enter your password to encode: ')
                encode(user_password)
                print('Your password has been encoded and stored!')
                print()


            if user_option == 3:
                break

# this is a comment used to see if file is pushed from pycharm