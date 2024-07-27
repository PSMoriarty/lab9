def decode(password):
    decoded_password = ''
    for char in password:
        decoded_char = chr((ord(char) - ord('0') - 3 + 10) % 10 + ord('0'))
        decoded_password += decoded_char
    return decoded_password