def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        current_index = 0
        count = 0
        for el in nums:
            if el == 0:
                count += 1
        for i in range(0, len(nums)):
            if nums[i] == 0:
                for k in range(i, len(nums)-1):
                    nums[k] = nums[k+1]
        for r in range(len(nums)-count, len(nums)):
            nums[r] = 0
        print nums

moveZeroes([0,1,0])
