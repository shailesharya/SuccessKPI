#Finding indices of elements from given array1 within array2

# input_str1 = input("Enter elements for the first array separated by spaces: ")
# input_str2 = input("Enter elements for the second array separated by spaces: ")

# # split seperated by spaces
# arr1 = list(map(int, input_str1.split()))
# arr2 = list(map(int, input_str2.split()))

arr1 = [1,2,3]
arr2 = [1,6,2,5,3,1,4]

indices_dict = {}

for i, num in enumerate(arr2):
    if num not in indices_dict:
        indices_dict[num] = [i]
    else:
        indices_dict[num].append(i)

for num in arr1:
    if num in indices_dict:
        print(f"Element {num} from array1 is found at indices {indices_dict[num]} in array2.")


# for i, num1 in enumerate(arr1):
#     for j, num2 in enumerate(arr2):
#         if num1 == num2:
#             print(f"Element {num1} from array1 is found at index {j} in array2.")
            

