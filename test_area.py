def reverse_list(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    print(arr)

# reverse_list([3,5,1,9,-1])

def sa_range(start, end): 
    temp_arr = []
    if start < end:
        for i, x in enumerate(range(start, end + 1)):
            print(i)
            temp_arr.append(x)
            print(temp_arr)
    elif start > end: 
        for i, x in enumerate(range(start, end - 1, -1)):
            print(i)
            temp_arr.append(x)
    else:
        temp_arr.append(x) 
    print(temp_arr)

# sa_range(0, -3)

def is_sorted(arr):
    is_ascending = True
    for i in range(1, len(arr)):
        # print(arr[i - 1], arr[i])
        if arr[i - 1] > arr[i] or arr[i - 1] == arr[i]:
            is_ascending = False
    if is_ascending:
        return 1

    is_descending = True
    for i in range(1, len(arr)):
        if arr[i - 1] < arr[i] or arr[i - 1] == arr[i]:
            is_descending = False
    if is_descending:
        return -1
    
    return 0
# print(is_sorted([-100, -8, 0, 2, 3, 10, 20, 100]))
# print(is_sorted(['A', 'B', 'Z', 'a', 'z']))
# print(is_sorted(['Z', 'T', 'K', 'A', '5']))
# print(is_sorted([1, 3, -10, 20, -30, 0]))
# print(is_sorted([-10, 0, 0, 10, 20, 30]))
# print(is_sorted([100, 90, 0, -90, -200]))
# print(is_sorted(['apple']))

def maxFrequency_2(arr):
    count = {}

    # looping elements of array, and adding its element as key in count dictionary
    for elem in arr:
        count[elem] = 0
        print(count)

    # looping elements of the array, and storing the frequency of each element in the array
    for elem in arr:
        count[elem] += 1
        print(count[elem], elem)
        
    max_frequency = 1
    elem = arr[0]

    for i in range(0, len(count)):
        # print(count[arr[i]], arr[i])
        if count[arr[i]] > max_frequency:
            elem = arr[i]
            max_frequency = count[arr[i]]

#     # return elem and max_frequency
    return elem, max_frequency

# print(maxFrequency_2([2, 2, 2, 2, 1, 1, 1, 1]))

def maxFrequency(arr): 
    frequency = 1
    element = arr[0]

    for i in range(0, len(arr) - 1):
        temp = arr[i]
        count = 0
        if arr[i] == arr[i+1]:
            # print(i, arr[i], arr[i+1])
            frequency += 1
            element = arr[i]
            print(frequency, element)
        if arr[i] != arr[i+1] and frequency > 1:
            print(frequency, element)
            return frequency, element

    return frequency, element

# print(maxFrequency([-242, -129, -129, 903, 903, 903]))
# print(maxFrequency([1, 20, 30, 40, 500, 500, 500]))
# print(maxFrequency([2, 2, 2, 2, 1, 1, 1, 1]))
# print(maxFrequency([-921, -921, -921, 665, 873, 873, 873, 903]))
# print(maxFrequency(['zebra', 'sloth', 'otter', 'otter', 'moose', 'koala']))
# print(maxFrequency(['Albania', 'Belgium', 'Chile', 'Denmark', 'Egypt', 'Fiji']))

def remove_duplicates(arr):
    #Find number of distinct elements
    n = 0
    prev_element = None
    for i in range(arr.length()):
        if prev_element is None or arr[i] != prev_element:
            n+= 1
        prev_element = arr[i]

    #Create static array of size n
    new_arr = StaticArray(n)

    #Now assign non duplicate elements from original array
    prev_element = None
    k = 0           #Current available index for new array
    for i in range(arr.length()):
        if prev_element is None or arr[i] != prev_element:          
            new_arr[k] = arr[i]
            k+= 1
        prev_element = arr[i]          
    return new_arr

def sa_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            print(arr[j])
        # for j in range(0, len(arr) - i-1):
        #     if arr[j] < arr[j + 1]:
        #         arr[j + 1], arr[j] = arr[j], arr[j + 1]
    return new_arr

# print(sa_sort([0, -5, -4, -3, -2, -1 , 0]))
# print(sa_sort([10100, 10721, 10320, 10998]))
# print(sa_sort([-100320, -100450, -100999, -100001]))

def array_test(arr):
    for i in range(0, len(arr)):
        print(arr[i-1], arr[i])
array_test([0, -5, -4, -3, -2, -1])