def main():
    for k in range(5,51,5):
        print(k)

    print ("------")

    for a in range(-2,3,1):
        print (a)

    print("------")

    for b in range(1,21):
        if b%2==0:
            print("%02d es par" %b)
        else:
            print("%02d es impar"%b)

main()

