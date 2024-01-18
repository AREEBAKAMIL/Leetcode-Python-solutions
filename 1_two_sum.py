class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x == y:
                    continue
                else:
                    if nums[x] + nums[y] == target:
                        return [x,y]


if __name__ == "__main__": 
    sol = Solution()
    print(sol.twoSum([3,2,4], 7))