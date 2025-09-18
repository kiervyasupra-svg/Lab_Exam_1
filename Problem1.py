def gcd(a,b):
    if b == 0:
        return  a
    else:
        return gcd(b, a % b)
def lcm(x, y ):
    return (x * y)// gcd(x,y)
def get_possitive_int(promt):
    while True:
        try:
            value = int(input(promt))
            if value<= 0:
                print("please Enter a number: ")
            else:
                return value
        except ValueError:
            print("Mali imong gi butang.")
x = get_possitive_int("Enter a number: ")
y = get_possitive_int("Enter next number: ")
result = lcm(x,y)
print(f"The LCM of {x} and {y} is {result}")







