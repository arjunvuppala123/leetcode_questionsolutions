public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> mySet = new HashSet<int>(nums.Length);
        foreach (var num in nums){
            if (!mySet.Add(num))
                return true;
        }

        return false;
    }
}
