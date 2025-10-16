def bubble_sort(arr):
    size = len(arr)
    swapped = False
    for i in range(size):
        for j in range(size-1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def bubble_sort_dict(arr, key):
    size = len(arr)
    swapped = False
    for i in range(size):
        for j in range(size-1 - i):
            if arr[j][key] > arr[j + 1][key]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    number_list = [64, 34, 25, 12, 22, 11, 90]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    
    print("Unsorted list:", number_list)
    sorted_list = bubble_sort(number_list)
    print("Sorted list:", sorted_list)
    
    print("Unsorted elements:", elements)
    sorted_elements = bubble_sort(elements)
    print("Sorted elements:", sorted_elements)
    
    
    elements_dic = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    
    print("Unsorted elements dictionary:", elements_dic)
    sorted_elements_dic = bubble_sort_dict(elements_dic, 'transaction_amount')
    print("Sorted elements dictionary by transaction_amount:", sorted_elements_dic)
    
    
    sorted_elements_dic_name = bubble_sort_dict(elements_dic, 'name')
    print("Sorted elements dictionary by name:", sorted_elements_dic_name)
    
    