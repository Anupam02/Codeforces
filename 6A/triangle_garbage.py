
def insertion_sort_with_args(*args, **kwargs):
    input_list = list(args)
    print type(input_list)
    for i in xrange(1, len(input_list)):
        key = input_list[i]
        j = i - 1
        while j >= 0 and input_list[j] > key:
            input_list[j+1] = input_list[j]
            j = j - 1
        input_list[j + 1] = key
    print input_list

def insertion_sort(arr):
    for i in xrange(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j > 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j = j-1
        arr[j+1] = key
    print arr
        
        
def main(*args, **kwargs):
    input_list = map(int, raw_input().split())
    print input_list, id(input_list)
    insertion_sort(input_list)
    print input_list

if __name__ == '__main__':
    main()
