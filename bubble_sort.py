class Solution:
	def bubbleSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		if len(nums) <= 1:
			return nums
        # 标志，当某次冒泡没有交换操作时，数组已经有序，无需再进行比较和交换操作
		flag = False
		for i in range(0, len(nums)):
			for j in range(1, len(nums)-i):
				if nums[j] < nums[j-1]:
					nums[j], nums[j-1] = nums[j-1], nums[j]
					flag = True
			if not flag:
				break
		return nums
if __name__ == "__main__":
	nums = [1,3,2,4,6,8,4,5,6,7]
	s = Solution()
	r = s.bubbleSort(nums)
	print(r)
