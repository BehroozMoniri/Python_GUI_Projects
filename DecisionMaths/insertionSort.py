# Recursive Python program for insertion sort
from time import process_time
# Recursive function to sort an array using insertion sort
def insertionSortRecursive(arr, n):
    # base case
    if n <= 1:
        return
 
    # Sort first n-1 elements
    insertionSortRecursive(arr, n - 1)
 
    # Insert last element at its correct position in sorted array.
    last = arr[n - 1]
    j = n - 2
 
    # Move elements of arr[0..i-1], that are
    # greater than key, to one position ahead
    # of their current position
    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = last
 
 
# Driver program to test insertion sort
if __name__ == '__main__':
    A = [-7, 11, 6, 0, -3, 5, 10, 2]
    start = process_time()
    n = len(A)
    insertionSortRecursive(A, n)
    end = process_time()
    print("insertionSortRecursive(A, n): ",A , f"Took: {end-start} seconds")
    

def bubble_sort(arr):
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        swapped = False
    # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
            # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            # If we didn't make any swaps in a pass, 
            # the list is already sorted and we can 
            # exit the outer loop
            if not swapped:
                return

# Sample list to be sorted
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Bubble Sorted list is:")
print(arr)

# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
