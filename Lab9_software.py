def decode(password):
    decoded_password = ''
    for char in password:
        decoded_char = chr((ord(char) - ord('0') - 3 + 10) % 10 + ord('0'))
        decoded_password += decoded_char
    return decoded_password

def encode(password):
    encoded_list = []
    for i in range(len(password)):
        encoded_list.append(int(password[i]) + 3)
    return ''.join(str(j) for j in encoded_list)


def main():
    encoded_password = ''
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter the password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif option == '2':
            if encoded_password:
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password} and the original password is {decoded_password}.")
            else:
                print("No encoded password found. Please encode a password first.")
        elif option == '3':
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()