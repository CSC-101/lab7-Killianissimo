import convert


def gather_numbers():
    userData = []
    output = []
    check = ""
    while check != "done":
        userData.append(input("Enter a number (enter done if Done): "))
        check = userData[-1]
    for i in range(len(userData)):
        if convert.str_to_float(userData[i]) is not None:
            output.append(convert.str_to_float(userData[i]))
    return output


if __name__ == '__main__':
    print(gather_numbers())

