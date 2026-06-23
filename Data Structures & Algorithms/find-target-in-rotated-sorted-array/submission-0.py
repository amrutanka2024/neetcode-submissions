class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L , R = 0 , len(nums) - 1

        while L <= R :
            M = (L + R) // 2
            if target == nums[M]:
                return M
            
            if nums[L] <= nums[M]: 
# check if target is small than left or bigger than middle if we need to go to the right part so L got updated
                if target > nums[M] or target < nums[L]:
                    L = M +1
                else:
                    R = M - 1
            
            else:#  in case the list =  [5,6,1,2,3,4] , T = 2
                if target < nums[M] or target > nums[R]:
                    R = M - 1
                else:
                    L = M + 1
        return -1