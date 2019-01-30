class Solution:
	def quickSort(self, nums, left, right):
		"""
		:type nums: List[int]
		:type left: int
		:type right: int
		:rtype: void
		"""
		if left >= right:
			return
		povit = self.partition(nums, left, right)
		self.quickSort(nums, left, povit-1)
		self.quickSort(nums, povit+1, right)

	def partition(self, nums, left, right):
		"""
		:type nums: List[int]
		:type left: int
		:type right: int
		:rtype: int
		"""
		# 以末点作为分界点
		povit = nums[right]
		povit_index = left
		for i in range(left, right):
			# 将小于分界点的值从最左侧依次摆放，不考虑它们的顺序
			if nums[i] < povit:
				nums[povit_index], nums[i] = nums[i], nums[povit_index]
				povit_index += 1
		# 将分界点放到正确的位置
		nums[right], nums[povit_index] = nums[povit_index], nums[right]
		return povit_index

if __name__ == "__main__":
	nums = [1,3,2,4,6,8,4,5,6,7,11,13,10,21,12]
	s = Solution()
	# 注意使用时传入的是length-1，否则会发生越界
	s.quickSort(nums, 0, len(nums)-1)
	print(nums)