import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int maxi = nums.length / 2;
        Set<Integer> sets = new HashSet<>();
        for(int i=0; i<nums.length; i++)
            sets.add(nums[i]);
        return Math.min(maxi, sets.size());
    }
}
