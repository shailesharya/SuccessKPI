# Display Even and Odd numbers from 1 to 100.

def display_even_odd_numbers():
    '''
    This function displays Even and Odd numbers from 1 to 100
    '''
    # display even numbers
    print("Even numbers from 1 to 100 are: ")
    for i in range(1, 101):
        if i % 2 == 0:
            print(i, end=" ")
    print()
    # display odd numbers
    print("Odd numbers from 1 to 100 are: ")
    for i in range(1, 101):
        if i % 2 != 0:
            print(i, end=" ")
    print()
    

if __name__ == "__main__":
    display_even_odd_numbers()