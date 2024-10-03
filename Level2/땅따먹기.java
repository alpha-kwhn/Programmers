import java.util.*;
import java.util.stream.*;

class Solution {
    int solution(int[][] land) {
        int N = land.length;
        int[][] dp = new int[N][4];
        dp[0] = land[0].clone();
        
        for(int i=0; i<N-1; i++) {
            for(int j=0; j<4; j++) {
                for(int k=0; k<4; k++) {
                    if(j == k)
                        continue;
                    dp[i+1][k] = Math.max(dp[i+1][k], dp[i][j] + land[i+1][k]);
                }
            }
        }
        
        return Arrays.stream(dp[N-1]).max().getAsInt();
    }
}
