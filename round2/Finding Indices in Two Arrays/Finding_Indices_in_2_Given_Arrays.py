#Finding indices of elements from given array1 within array2

arr1 = [1,2,3]
arr2 = [1,6,2,5,3,1,4]

indices_dict = {}

for num1 in arr1:
    if num1 not in indices_dict:
        indices_dict[num1] = []
    
    for i, num2 in enumerate(arr2):
        if num1 == num2:
            indices_dict[num1].append(i)

for num, indices in indices_dict.items():
    print(f"Element {num} from array1 is found at indices {indices} in array2.")