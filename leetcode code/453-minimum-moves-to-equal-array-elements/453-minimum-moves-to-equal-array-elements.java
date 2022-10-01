class Solution {
    public int minMoves(int[] nums) {
        int sum = IntStream.of(nums).sum();
        Arrays.sort(nums);
        int min = nums[0];
        int length = nums.length;
        return sum - min*length;
    }
}