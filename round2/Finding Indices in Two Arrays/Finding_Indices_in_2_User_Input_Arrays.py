# Finding indices of elements from array1 within array2 with user input

input_str1 = input("Enter elements for the first array separated by spaces: ")
input_str2 = input("Enter elements for the second array separated by spaces: ")

# split seperated by spaces
arr1 = list(map(int, input_str1.split()))
arr2 = list(map(int, input_str2.split()))

indices_dict = {}

for num1 in arr1:
    if num1 not in indices_dict:
        indices_dict[num1] = []

    for i, num2 in enumerate(arr2):
        if num1 == num2:
            indices_dict[num1].append(i)

for num, indices in indices_dict.items():
    print(f"Element {num} from array1 is found at indices {indices} in array2.")