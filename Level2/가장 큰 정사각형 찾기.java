import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(int [][]board) {
        int[][] dp = new int[board.length][board[0].length];
        int answer = 0;
        
        for(int i=0; i<board.length; i++) {
            for(int j=0; j<board[0].length; j++) {
                if(board[i][j] == 1) {
                    dp[i][j] = 1;
                    answer = 1;
                }
            }
        }
        
        for(int i=1; i<board.length; i++) {
            for(int j=1; j<board[0].length; j++) {
                if(board[i][j] == 1) {
                    if(board[i-1][j-1] == 1 && board[i-1][j] == 1 && board[i][j-1] == 1) 
                        dp[i][j] = Math.min(Math.min(dp[i-1][j-1], dp[i-1][j]), dp[i][j-1]) + 1;
                    else 
                        dp[i][j] = 1;
                    answer = Math.max(answer, dp[i][j]);
                }
            }
        }
        
        return answer * answer;
    }
}
