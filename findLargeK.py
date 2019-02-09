class Solution:
	def findLargeK(self, nums, k):
		left, right = 0, len(nums)-1
		while left <= right:
			pivot = self.partition(nums, left, right)
			if k-1 == pivot:
				return nums[pivot]
			elif k-1 > pivot:
				left = pivot + 1
			else:
				right = pivot - 1
		return -1
	def partition(self, nums, left, right):
		pivot = right
		index = left
		for i in range(left, right):
			if nums[i] > nums[pivot]:
				nums[index], nums[i] = nums[i], nums[index]
				index += 1
		nums[pivot], nums[index] = nums[index], nums[pivot]
		return index

if __name__ == "__main__":
	a = [1,2,5,3,6,7,12,5,3,7,3]
	s = Solution()
	r = s.findLargeK(a, 7)
	print(r)