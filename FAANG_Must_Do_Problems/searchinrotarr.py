class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        beg = 0
        end = len(nums)-1
        while beg<=end:
            mid = (beg+end)//2
            if target == nums[mid]:
                return mid
            elif nums[beg]<=nums[mid]:
                if nums[beg]<=target<=nums[mid]:
                    end = mid-1
                else:
                    beg = mid+1
            else:
                if nums[mid]<=target<=nums[end]:
                    beg = mid+1
                else:
                    end = mid-1
        return -1