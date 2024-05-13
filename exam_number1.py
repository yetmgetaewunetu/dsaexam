def count_ocuurence():
    numbers = input("Enter space separated sequence of numbers: ").split()
    key = input("Enter the number you wanted to search: ")
    if key not in numbers:
        print("the number is not present is the list")
        return
    cnt = 0
    for number in numbers:
        if number == key:
            cnt += 1
    print(f"the number {key} exist {cnt} times in the list!")

count_ocuurence()
