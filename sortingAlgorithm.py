''' The following function illustrates how the bubble sort algorithm works the function below will take a single
array as an input and then return a sorted array in ascending as a result. The bubble sort algorithm compares two
consecutive numbers in an array(which is a set of consecutive numbers) and then swaps the numbers if the number on
the left is greater than the number on the right. After all the numbers adjacent to each other is complete,
the largest number will be in the end of the array and the same process is applied again on the partially sorted
array for exactly the number of times as the length of the array, and in each pass the largest element in the
unsorted half will bubble up to the largest index. '''


def sort_by_bubble_sort(unsorted_array):
    # n represents the length of the unsorted array and is found by the in built function of python len()
    n = len(unsorted_array)
    # The array to be sorted is copied to a new array called array_to_be_sorted
    array_to_be_sorted = unsorted_array
    # starting from 0, up until the length of the array , this loop will do the same thing
    for i in range(n):
        # the current pass is changed for every pass until n-1, and is assigned to the variable current pass
        currentPass = i
        # the starting number of x is 0 and increments by 1 up until the number that yields from (n - currentPass -
        # 1) and represents the max index - 1
        for x in range(n - currentPass - 1):
            # compare the two consecutive numbers and if the number on the left is greater than the one on the right,
            # swap them in the array, otherwise do nothing
            if array_to_be_sorted[x] > array_to_be_sorted[x + 1]:
                array_to_be_sorted[x], array_to_be_sorted[x + 1] = array_to_be_sorted[x + 1], array_to_be_sorted[x]
        # uncomment the next line to see the state of the array after each and every pass
        #print(ListToBeSorted)
        # in the end of all the loops, return the sorted array
    return array_to_be_sorted


if __name__ == '__main__':

    # Here are some test cases that illustrates that this function works perfectly, with unsorted lists that are used
    # as input to the function above
    unsorted_list_1 = [5, 3, 10, 7, 4, 1]
    print(sort_by_bubble_sort(unsorted_list_1))

    unsorted_list_2 = [1, 1, 1, 1, 1]
    print(sort_by_bubble_sort(unsorted_list_2))

    unsorted_list_3 = [1, 2, 2, 2, 2, 1]
    print(sort_by_bubble_sort(unsorted_list_3))

    unsorted_list_4 = [1, 2, 1, 2, 1,2]
    print(sort_by_bubble_sort(unsorted_list_4))

    unsorted_list_5 = [3, 2, 1, 2, 1,2]
    print(sort_by_bubble_sort(unsorted_list_5))