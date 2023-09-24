# Finding indices of elements from array1 within array2 with user input

input_str1 = input("Enter elements for the first array separated by spaces: ")
input_str2 = input("Enter elements for the second array separated by spaces: ")

# split seperated by spaces
arr1 = list(map(int, input_str1.split()))
arr2 = list(map(int, input_str2.split()))

indices_dict = {}

for i, num in enumerate(arr2):
    if num not in indices_dict:
        indices_dict[num] = [i]
    else:
        indices_dict[num].append(i)

for num in arr1:
    if num in indices_dict:
        print(f"Element {num} from array1 is found at indices {indices_dict[num]} in array2.")