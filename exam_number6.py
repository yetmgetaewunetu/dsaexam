def delete_element_static_size(array, index):
    if index <0 or index >= len(array):
        print("Invalid index!")
        return
    new_array = [0]* (len(array) - 1)

    for i in range(len(array)):
        if i == index:
            continue
        if i > index:
            new_array[i - 1] = array[i]
            continue
        new_array[i] = array[i]
    array = new_array
    print(f"the array after deleting becomes--> {array}")





#dynamic size
def delete_element(array, index):
    if index >= len(array) or index < 0:
        print("Invalid index!")
        return
    nums.pop(index)


nums = [3,7,1,9,4]
delete_element_static_size(nums, 0)
