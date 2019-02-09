class Solution:
	def quickSort(self, nums, left, right):
		if left >= right:
			return
		povit = self.povit(nums, left, right)
		self.quickSort(nums, left, povit-1)
		self.quickSort(nums, povit+1, right)


	def povit(self, nums, left, right):
		p = right
		index = left
		for i in range(left, right):
			if nums[i] < nums[p]:
				nums[index], nums[i] = nums[i], nums[index]
				index += 1
		nums[index], nums[right] = nums[right], nums[index]
		return index


if __name__ == "__main__":
	nums = [20,1,3,2,4,6,8,4,5,7,3,2,1,10,15,21,12]
	s = Solution()
	s.quickSort(nums, 0, len(nums)-1)
	print(nums)