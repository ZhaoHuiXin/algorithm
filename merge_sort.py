class Solution:
	def mergeSort(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		length = len(nums)
		if length <= 1:
			return nums
		mid = length // 2
		# 分治 + 递归
		left = self.mergeSort(nums[:mid])
		right = self.mergeSort(nums[mid:])
		return self.merge(left, right)

	def merge(self, left, right):
		"""
		:type left: List[int]
		:type right: List[int]
		:rtype: List[int]
		"""
		res = []
		p = q = 0
		while p != len(left) and q != len(right):
			# 使用 “<=” 保证排序的稳定性
			if left[p] <= right[q]:
				res.append(left[p])
				p += 1
			else:
				res.append(right[q])
				q += 1
		l = left[p:] or right[q:]
		res.extend(l)
		return res


if __name__ == "__main__":
	nums = [1,3,2,4,6,8,4,5,6,7,11,13,10,21,12]
	s = Solution()
	r = s.mergeSort(nums)
	print(r)