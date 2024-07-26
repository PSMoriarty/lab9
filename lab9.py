# Lab 9


def encode(password):
    encoded_list = []
    for i in range(len(password)):
        encoded_list.append(int(password[i]) + 3)
    return ''.join(str(j) for j in encoded_list)




