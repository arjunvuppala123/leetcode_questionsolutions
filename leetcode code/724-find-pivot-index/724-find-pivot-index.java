class Solution {
    public int pivotIndex(int[] nums) {
        int leftSum = 0;
        int totalSum = 0;
        for (int num:nums)
            totalSum += num;
        int i = 0;
        while (i<nums.length){
            if (totalSum - nums[i] == leftSum){
                return i;
            }
            else{
                leftSum += nums[i];
                totalSum -= nums[i];
            }
            i++;
        }
        return -1;
    }
}