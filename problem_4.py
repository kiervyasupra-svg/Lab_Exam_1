def isPalindrome(valStr):

    return valStr == valStr[::-1]


def toBinaryIfNumber(value):


    if value.isdigit():


        return bin(int(value))[2:]

    else:

        return None


def main():
    user_input = input("Enter a value: ")

    input_palindrome = isPalindrome(user_input)

    print(f"Input is a palindrome: {input_palindrome}")

    binary_equiv = toBinaryIfNumber(user_input)

    if binary_equiv is not None:

        print(f"Binary equivalent: {binary_equiv}")

        binary_palindrome = isPalindrome(binary_equiv)

        print(f"Binary is a palindrome: {binary_palindrome}")

    else:

        print("(No binary conversion since input is text)")


if __name__ == "__main__":
    main()
Message
Text
Editor
