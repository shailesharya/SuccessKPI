def display_even_odd_numbers():
    even_nos = []
    odd_nos = []

    startPoint = int(input("Enter the start point: "))
    endPoint = int(input("Enter the end point: "))
    for i in range(startPoint, endPoint+1):
        if i % 2 == 0:
            even_nos.append(i)
        else:
            odd_nos.append(i)

    print("Even numbers are: ", even_nos)
    print("Odd numbers are: ", odd_nos)

if __name__ == "__main__":
    display_even_odd_numbers()