def CountEvenNumbers(nums):
    count = 0
    for i in range(len(nums)):
        string_digits = str(nums[i])
        if len(string_digits) % 2 == 0:		# Time complexity O(n * log10(M))
            count += 1				        # Space complexity O(1)
    return count

2nd approach:
event_count =0
    for i in range(len(nums)):
        digits_count = 0
        while(nums[i]>0):
            nums[i] = nums[i] //10		# Time complexity O(n * log10(M))
            digits_count += 1			# Space complexity O(1)
        if digits_count % 2 == 0:
            event_count += 1
    return event_count
