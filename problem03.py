print("Mobile Network Checker")

number = input("Input your 11-digit number: ")
print("Your number:", number)


if len(number) != 11:
    print("Invalid number: must be 11 digits.")
elif not number.startswith("09"):
    print("Wrong number: must start with '09'.")
else:
    prefix = number[:4]


    if prefix in ["0905", "0906", "0915", "0916", "0920"]:
        print("The network of the number is TM.")
    elif prefix in ["0917", "0994", "0997"]:
        print("The network of the number is Globe.")
    elif prefix in ["0913", "0914", "0920", "0921","0928","0929","0930"]:
        print("The network of the number is Smart.")
    elif prefix in ["0901","0902","0924"]:
        print("The network of the number is RED.")
    elif prefix in ["0909","0910","0911","0912","0918","0919"]:
        print("The network of the number is TNT")
    elif prefix in ["0922","0923","0932","0933"]:
        print("The network of the number is Sun")
    elif prefix in ["0991","0992","0993","0994","0995","0996","0997","0998"]:
        print("The network of the number is DITO")
    else:
        print("Unknown network.")
