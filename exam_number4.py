def bubbles_sort_for_alphabets(alphabets):
    for i in range(len(alphabets) - 1, 0 , -1):
        for j in range(0, i):
            if alphabets[j] > alphabets[j + 1]:
                alphabets[j] , alphabets[j + 1] = alphabets[j + 1] , alphabets[j]

    print(*alphabets)
    return alphabets

alphabets = ['d','c','g','b','k','o','a','z','a','b','c','e','d']
bubbles_sort_for_alphabets(alphabets)
