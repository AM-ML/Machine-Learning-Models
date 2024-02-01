import time

def split(a, low, high):
	pivot = a[low]

	while(True):
		while low < high and pivot <= a[high]:
			high-= 1

		if low >= high:
			break

		a[low] = a[high]
		low+=1

		while low < high and pivot >= a[low]:
			low +=1

		if low >= high:
			break

		a[high] = a[low]

		high -= 1
	a[high] = pivot

	return high

def quicksort(a, low, high):
	if low >= high:
		return 
	middle = split(a, low, high)
	quicksort(a, low, middle - 1)
	quicksort(a, middle + 1, high)



def bubblesort(a):

	temp = 0

	for _ in range(len(a)):
		for i in range(len(a) - 1):
			if a[i] > a[i+1]:
				temp = a[i]
				a[i] = a[i+1]
				a[i+1] = temp



def timed(f, *args, **kwargs):
    start_time = time.time()
    f(*args, **kwargs)
    return time.time() - start_time