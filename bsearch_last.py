class Solution:
	def bsearch(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		low = 0
		high = len(nums) - 1
		while low <= high:
			mid = low + ((high-low)>>1)
			if nums[mid] > val:
				high = mid - 1
			elif nums[mid] < val:
				low = mid + 1
			else:
				if mid == len(nums)-1 or nums[mid+1] != val:
					return mid
				else:
					low = mid + 1
		return -1

if __name__ == "__main__":
	a = [1,3,4,5,7,7,7,7,8,10,11,11,11,11,11]
	s = Solution()
	r = s.bsearch(a, 11)
	print(r)