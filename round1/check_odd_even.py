def check_odd_even():
    '''
    This function checks if a number is odd or even
    '''
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(str(num) + " is Even")
    else:
        print(str(num) + "is Odd")


if __name__ == "__main__":
    check_odd_even()