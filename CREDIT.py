def main():
    card_number = input("Number: ")

    # Check if input is only digits
    if not card_number.isdigit():
        print("INVALID")
        return

    length = len(card_number)
    first_digit = card_number[0]

    # AMEX
    if length == 15 and first_digit == "3":
        print("AMEX")

    # VISA
    elif length == 16 and first_digit == "4":
        print("VISA")

    # MASTERCARD
    elif length == 16 and first_digit == "5":
        print("MASTERCARD")

    else:
        print("INVALID")


main()
