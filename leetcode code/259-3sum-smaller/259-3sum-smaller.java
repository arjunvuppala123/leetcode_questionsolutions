class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        Arrays.sort(nums);
        int res = 0;
        for(int i=0;i<nums.length;i++){
            int l = i + 1;
            int r = nums.length - 1;
            
            while(l<r){
                int temp = nums[i] + nums[l] + nums[r];
                if (temp<target){
                    res = res + (r-l);
                    l++;
                }
                else{
                    r--;
                }
            }
        }
        
        return res;
    }
}