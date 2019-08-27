mockString = input("Enter your text: ")


def spongemock(s):
    sponge_string = ''
    for pos, letter in enumerate(s):
        if pos % 2 == 0:
            sponge_string += letter.upper()
        else:
            sponge_string += letter

    return sponge_string


modified_string = spongemock(mockString)
print(modified_string)
