import java.util.*;
class Solution {
    static long[] dp;
    public int solution(int n) {
        if(n % 2 == 1)
            return 0;
        else {
            dp = new long[n+1];
            dp[0] = 1L;
            dp[2] = 3L;
            dp[4] = 11L;
            int start = 6;
            while(start <= n) {
                dp[start] = ((((dp[start-2] * 4) % 1000000007) + 1000000007) - (dp[start-4] % 1000000007)) % 1000000007;
                start += 2;
            }
            return (int)(dp[n] % 1000000007);
        }
    }
}
