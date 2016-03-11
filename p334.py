class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        history = []
        for i in range(1, len(nums)):
            print "nums[%i] = %i, nums[%i] = %i" % (i-1, nums[i-1], i, nums[i])
            if nums[i-1] < nums[i]:
                if not history:
                    history = nums[i-1:i+1]
                else:
                    if nums[i-1] > history[0]:
                        return True
                    elif nums[i] > history[1]:
                        return True
                    else:
                        history = nums[i-1:i+1]
        return False