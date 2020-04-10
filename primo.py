def primo(n):
    bandera = True
    if n < 2:
        bandera = False
    else:
        for x in range(2, n):
            if n % x == 0:
                bandera = False
    if bandera:
        print(n, "is a prime number")
    else:
        print(n, "is NOT a prime number")


number = int(input("Number: "))
primo(number)

