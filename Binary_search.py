def binary_search(ranges, item, k):
	
	low = 0
	high = len(ranges[k]) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = ranges[k][mid]
		if item in range(guess[0], guess[1]+1):
			return True, guess
		elif guess[0] > item:
			high = mid - 1
		else:
			low = mid + 1
	return False, None

def binary_search_stranded(ranges, item, s, k):
	
	low = 0
	high = len(ranges[s][k]) - 1
	while low <= high:
		mid = (low + high) // 2
		guess = ranges[s][k][mid]
		if item in range(guess[0], guess[1]+1):
			return True
		elif guess[0] > item:
			high = mid - 1
		else:
			low = mid + 1
	return False