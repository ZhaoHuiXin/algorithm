class Solution:
	def selectionSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void
		"""
		length = len(nums)
		if length <= 1:
			return
		for i in range(0, length-1):
			# 从索引为0开始，依次将每个位置的初始值作为本次内层循环的最小值
			min_index = i
			for j in range(i+1, length):
				# 循环过程中发现小于最小值的值，先记录其索引，内循环结束后进行值交换
				if nums[j] < nums[min_index]:
					min_index = j
			nums[min_index], nums[i] = nums[i], nums[min_index]
		return

if __name__ == "__main__":
	nums = [1,3,2,4,6,8,20,4,5,6,7,10]
	s = Solution()
	s.selectionSort(nums)
	print(nums)