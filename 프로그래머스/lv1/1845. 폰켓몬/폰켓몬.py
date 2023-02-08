def solution(nums):
    answer = 0
    length = len(nums)//2
    nums = set(nums)
    if len(nums) < length:
        answer = len(nums)
    else:
        answer = length
    return answer