#firstchallenge
def merge(list1, list2):
    merged_list = tuple(zip(list1, list2))
    return merged_list
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(merge(list1, list2))
#secondchallenge
nums = [x for x in range(1, 8)]
nums1 = [16,18,454,94,8,56,88,24,575,354,57,357]
zipped_list = list(zip(nums, nums1))
print(zipped_list)
#thirdchallenge
nums=[1,8,6,4,44,99,56,2,84,7]
print(sorted(nums))
#fifthchallenge
odd_nums = list(filter(lambda x:x%2!=0, nums1))
print(odd_nums)
