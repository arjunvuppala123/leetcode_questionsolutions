class Solution {
    public int maxArea(int[] height) {
        int n = height.length;
        int area = 0;
        int currArea = 0;
        int left = 0;
        int right = n-1;
        
        for(int i=0;i<n;i++){
            currArea = Math.min(height[left],height[right])*(right-left);
            if(currArea > area){
                area = currArea;
            }
            if(height[left]<height[right]){
                left += 1;
            }
            else{
                right -= 1;
            }
        }
        return area;
    }
}