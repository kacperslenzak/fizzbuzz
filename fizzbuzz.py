def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "ThreeFive"
    elif n % 3 == 0:
        return "Three"
    elif n % 5 == 0:
        return "Five"

    return n


for i in range(1, 101):
    print(fizz_buzz(i))
