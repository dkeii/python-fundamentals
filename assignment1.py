import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> tuple:
    min = arr[0];
    max = arr[0];
    for i in range(arr.length()):
        if min > arr[i]:
            min = arr[i];
        if max < arr[i]:
            max = arr[i];
    return  min, max

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    new_arr = StaticArray(arr.length())
    for i in range(arr.length()):
        if arr[i] % 3 == 0 and arr[i] % 5 == 0:
            # new_arr[i] = 'fizzbuzz'
            new_arr.set(i, "fizzbuzz")
        elif arr[i] % 3 == 0:
            # new_arr[i] = 'fizz'
            new_arr.set(i, 'fizz')
        elif arr[i] % 5 == 0:
            # new_arr[i] = 'buzz'
            new_arr.set(i, "buzz")
        else:
            new_arr.set(i, arr[i])
    return new_arr
# ------------------- PROBLEM 3 - REVERSE -----------------------------------


def reverse(arr: StaticArray) -> None:
    ln = arr.length()
    i = 0
    j = ln - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    temp_arr = StaticArray(arr.length())

    # Store values in the new array 
    for i in range(arr.length()):
        temp_arr.set(i, arr[i])


    steps = steps % temp_arr.length()

    # left and right pointers 
    l, r = 0, temp_arr.length() - 1
    

    if steps != 0:
        # 1st reverse 
        while l < r:
            temp_arr[l], temp_arr[r] = temp_arr[r], temp_arr[l]
            l, r = l + 1, r - 1
        
        # 2nd reverse 
        l, r = 0, steps - 1 
        while l < r: 
            temp_arr[l], temp_arr[r] = temp_arr[r], temp_arr[l]
            l, r = l + 1, r - 1
        
        # 3d reverse 
        l, r = steps, temp_arr.length() - 1 
        while l < r: 
            temp_arr[l], temp_arr[r] = temp_arr[r], temp_arr[l]
            l, r = l + 1, r - 1
        
        # setting values back to original array 
        l, r = 0, 0
    return temp_arr 

# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    l = abs((end-start)) + 1 
    temp_arr = StaticArray(l)
    if start < end:
        for i, x in enumerate(range(start, end + 1)):
            print(i, x)
            temp_arr.set(i, x)
    elif start > end:
        for i, x in enumerate(range(start, end - 1, -1)):
            print(i, x)
            temp_arr.set(i, x)
            # temp_arr.set(i, i - 1, -1)
    elif start == end:
        temp_arr.set(0, start)          
    
    return temp_arr

# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    ascending = True
    descending = True
    
    for i in range(1, arr.length()):
        if arr[i-1] > arr[i] or arr[i-1] == arr[i]:
            ascending = False
    if ascending:
        return 1 
    
    for i in range(1, arr.length()):
        if arr[i-1] < arr[i] or arr[i-1] == arr[i]:
            descending = False
    if descending:
        return -1 
        
    return 0

# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> tuple:
    frequency = 1
    element = arr[0]

    for i in range(0, arr.length() - 1):
        temp = arr[i]
        count = 0
        if arr[i] == arr[i+1]:
            # print(i, arr[i], arr[i+1])
            count = frequency + 1
            frequency += 1
            element = arr[i]
        if arr[i] != arr[i+1] and frequency > 1:
            return element, frequency

    return element, frequency 

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:

    last_el = None
    num = 0

    for i in range(arr.length()):
        if last_el is None or arr[i] != last_el:
            num += 1
        last_el = arr[i]

    new_arr = StaticArray(num)

    last_el = None
    index = 0         
    for i in range(arr.length()):
        if last_el is None or arr[i] != last_el:          
            new_arr[index] = arr[i]
            index += 1
        last_el = arr[i]          
    return new_arr

# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    new_arr = StaticArray(arr.length())
    k = 0
    n = arr.length()
    min_and_max = min_max(arr)
    max = min_and_max[1]
    min = min_and_max[0]

    rng = max - min + 1
    count = StaticArray(rng)

    # Counting elements and assigning to the proper index 
    for i in range(count.length()):
        count[i] = 0

    for i in range(arr.length()):
        count[arr[i] - min] += 1

    # Updating count array 
    for i in range(1, count.length()):
        count[i] += count[i-1]
    
    # Sorting the original array
    for i in range(arr.length() -1, -1, -1):
        count[arr[i] - min ] -= 1
        new_arr[count[arr[i] - min]] = arr[i]
        
    ln = new_arr.length()
    x = 0
    j = ln - 1
    while x < j:
        new_arr[x], new_arr[j] = new_arr[j], new_arr[x]
        x += 1
        j -= 1

        
    # print(count)
    return new_arr

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    new_arr = StaticArray(arr.length())

    # min, max = min_max(new_arr)
    # rng = max - min + 1
    # print(rng, max, min)
    
    for i in range(1, arr.length()):
        if arr[i-1] < arr[i]:
            # print(new_arr)
            new_arr[i] = arr[i] * arr[i]
            new_arr.set(i, new_arr[i])
            start = new_arr[0]
            end = new_arr[new_arr.length() - 1]
            print(start, end)
            if start != None and end != None:
                print(start, end)
        
    
    return new_arr

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]: 3}, Max: {result[1]: 3}")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    print(f"Min: {result[0]}, Max: {result[1]}")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        print(f"Min: {result[0]: 3}, Max: {result[1]}")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    # print('\n# rotate example 2')
    # array_size = 1_000_000
    # source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    # arr = StaticArray(len(source))
    # for i, value in enumerate(source):
    #     arr[i] = value
    # print(f'Started rotating large array of {array_size} elements')
    # rotate(arr, 3 ** 14)
    # rotate(arr, -3 ** 15)
    # print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        mode, frequency = find_mode(arr)
        print(f"{arr}\nMode: {mode}, Frequency: {frequency}\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    #[10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    # print('\n# count_sort example 2')
    # array_size = 5_000_000
    # min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    # max_val = min_val + 998
    # case = [random.randint(min_val, max_val) for _ in range(array_size)]
    # arr = StaticArray(len(case))
    # for i, value in enumerate(case):
    #     arr[i] = value
    # print(f'Started sorting large array of {array_size} elements')
    # result = count_sort(arr)
    # print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    # print('\n# sorted_squares example 2')
    # array_size = 5_000_000
    # case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    # arr = StaticArray(len(case))
    # for i, value in enumerate(sorted(case)):
    #     arr[i] = value
    # print(f'Started sorting large array of {array_size} elements')
    # result = sorted_squares(arr)
    # print(f'Finished sorting large array of {array_size} elements')
