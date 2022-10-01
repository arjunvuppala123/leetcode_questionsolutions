class Solution {
    public int brokenCalc(int startValue, int target) {
        int ans = 0;
        while (startValue < target){
            ans++;
            if(target%2!=0){
                target += 1;
            }
            else{
                target /= 2;
            }
        }
        return ans + startValue - target;
    }
}