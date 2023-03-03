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



'''Modified below by:
    Harit Palta
    Group 37 
    Lab 6 Version Control'''

#added decode function
def decode(password):
    # string to store decoded password
    decoded_pass = ''

    # decoding of each digit
    for num in range(len(password)):
        decoded_pass += str((int(password)-3)%10)  # shifting 3 digit down and mod keeps value within 0-9

    # return decoded password
    return decoded_pass





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
            if user_option == 2:
                print(f'The encoded password is {encode(user_password)}, and the original password is {user_password}')
                print()

            if user_option == 3:
                break

