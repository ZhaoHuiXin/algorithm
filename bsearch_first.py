class Solution:
	def bsearch(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""
		high = len(nums) - 1
		low = 0
		while low <= high:
			mid = low + ((high - low)>>1)
			if nums[mid] < val:
				low = mid + 1
			elif nums[mid] > val:
				high = mid - 1
			else:
				if mid == 0 or nums[mid-1] != val:
					return mid
				else:
					high = mid - 1
		return -1

if __name__ == "__main__":
	a = [1,3,4,5,7,7,7,7,8,10,11]
	s = Solution()
	r = s.bsearch(a, 7)
	print(r)