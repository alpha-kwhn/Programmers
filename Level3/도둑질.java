import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int[] money) {
        int[] dp = new int[money.length];
        int[] dp2 = new int[money.length];
        
        dp[0] = dp[1] = money[0];
        dp2[1] = money[1];
        
        for(int i=2; i<money.length-1; i++) 
            dp[i] = Math.max(dp[i-2] + money[i], dp[i-1]);
        
        for(int i=2; i<money.length; i++) 
            dp2[i] = Math.max(dp2[i-2] + money[i], dp2[i-1]);
        
        return Math.max(Arrays.stream(dp).max().getAsInt(), Arrays.stream(dp2).max().getAsInt());   
    }
}
