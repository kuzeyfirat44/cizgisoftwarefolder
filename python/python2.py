num1 = int(input("Give Me A Number."))
if num1 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")


asalsayi = int(input("Give Me A Number."))
if asalsayi < 2:
    print("The number is not prime.")
else:
    for i in range(2, asalsayi):
        if asalsayi % i == 0:
            print("The number is not prime.")
            break
    else:
        print("The number is prime.")