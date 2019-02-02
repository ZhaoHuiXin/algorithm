class Solution:
	def bsearch(self, nums, left, right, val):
		"""
		:type nums: List[int]
		:type left: int
		:type right: int
		:type val: int
		:rtype: int
		"""
		if left > right:
			return -1
		mid = left + ((right-left)>>1)
		if nums[mid] == val:
			return mid
		elif nums[mid] > val:
			right = mid - 1
			return self.bsearch(nums, left, right, val)
		else:
			left = mid + 1
			return self.bsearch(nums, left, right, val)

			
if __name__ == "__main__":
	a = [1,3,4,5,7,7,7,7,8,10,11]
	s = Solution()
	r = s.bsearch(a, 0, len(a)-1, 7)
	print(r)