class Solution:
	def bsearch(self, nums, val):
		"""
		:type nums: List[int] order
		:type val: int
		:rtype: int
		"""
		length = len(nums)
		low = 0
		high = length - 1
		while low <= high:
			mid = low + ((high-low) >> 1)
			if nums[mid] == val:
				return mid
			elif nums[mid] < val:
				low = mid + 1
			else:
				high = mid - 1
		return -1

if __name__ == "__main__":
	s = Solution()
	l = [1,3,5,6,7,8,10]
	r = s.bsearch(l, 2)
	print(r)