def CountEvenNumbers(nums):
    count = 0
    for i in range(len(nums)):
        string_digits = str(nums[i])
        if len(string_digits) % 2 == 0:
            count += 1
    return count
