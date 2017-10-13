def aproximarPi(n):
    suma = 0
    contador = 0

    for d in range(1, n + 1, 2):
        contador += 1

        if contador % 2 == 1:
            suma = suma + 1 / d
        else:
            suma = suma - 1 / d

    return 4*suma


def main():
    print(aproximarPi(100000))


main()
