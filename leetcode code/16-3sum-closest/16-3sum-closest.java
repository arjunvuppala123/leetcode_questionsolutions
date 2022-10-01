class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int result = nums[0]+nums[1]+nums[2];
        
        for(int i=0;i<nums.length;i++){
            int left=i+1;
            int right=nums.length-1;
            while(left<right){
                int dummy = nums[i] + nums[left] + nums[right];
                if(dummy==target){
                   return dummy; 
                }
                if(Math.abs(dummy-target)<Math.abs(result-target)){
                    result = dummy;
                }
                if(dummy<target){
                    left += 1;
                }
                else{
                    right -= 1;
                }
            }
        }
        return result;
    }
}