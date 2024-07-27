# Lab 9

def encode(password):
    encoded_list = []
    for i in range(len(password)):
        encoded_list.append(int(password[i]) + 3)
    return ''.join(str(j) for j in encoded_list)


def decode(password):
    decoded_password = ''
    for char in password:
        decoded_char = chr((ord(char) - ord('0') - 3 + 10) % 10 + ord('0'))
        decoded_password += decoded_char
    return decoded_password

def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def main():
    menu_option = 0
    password = ''
    while menu_option != 3:
        menu()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            enc_pw = input('Please enter the password to encode: ')
            password = encode(enc_pw)
            print('Your password has been encoded and stored!')
        elif menu_option == 2:
            if len(password) != 0 :
                print(f'The encoded password is {password},'
                      f'and the original password is {decode(password)}.')
            else:
                "No password has been entered."
        elif menu_option != 3:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()
