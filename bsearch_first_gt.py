class Solution:
	def bsearch(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		low = 0
		high = len(nums) - 1
		while low <= high:
			mid = low + ((high-low) >> 1)
			if nums[mid] >= target:
				if mid == 0 or nums[mid-1] < target:
					return mid
				else:
					high = mid - 1
			else:
				low = mid + 1
		return -1

if __name__ == "__main__":
	a = [1,3,4,5,7,7,7,7,8,10,11,11,11,11,11]
	s = Solution()
	r = s.bsearch(a, 11)
	print(r)
