def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    if not s.isalnum():
        return False

    first_num_index = None
    for i, character in enumerate(s):
        if character.isnumeric():
            if character == "0":
                return False
            first_num_index = i
            break

    if first_num_index is None:
        return True

    for character in s[first_num_index:]:
        if not character.isnumeric():
            return False

    return True


if __name__ == "__main__":
    main()
