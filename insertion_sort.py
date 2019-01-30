class Solution:
	def insertionSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: void
		"""
		length = len(nums)
		if length <= 1:
			return
		for i in range(0, length-1):
			for j in range(i+1, 0, -1):
				# 不用“<=”为了保证排序的稳定性
				if nums[j] < nums[j-1]:
					nums[j], nums[j-1] = nums[j-1], nums[j]
				# 当已排序部分的最大值小于等于本次的取值，本次操作直接中断
				else:
					break
		return

if __name__ == "__main__":
	nums = [1,3,2,4,6,8,4,5,6,7]
	s = Solution()
	s.insertionSort(nums)
	print(nums)