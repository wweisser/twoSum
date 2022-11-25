class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List = [0, 0];
        i = 0;
        j = 1;
        lenNums = len(nums);
        print(lenNums);
        while i < lenNums:
            j = i + 1;
            while j < lenNums:
                if (nums[i] + nums[j]) == target:
                    List[0] = i;
                    List[1] = j;
                j = j + 1;
            i = i + 1;
        return (List);
        
