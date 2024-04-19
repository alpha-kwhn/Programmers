import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        int answer = 0;
        int[][] test = new int[triangle.length][triangle.length];
        test[0][0] = triangle[0][0];
        for(int i=1; i<triangle.length; i++) {
            for(int j=0; j<=i; j++) {
                if(j == 0) 
                    test[i][j] = triangle[i][j] + test[i-1][j];
                else if(j == i)
                    test[i][j] = triangle[i][j] + test[i-1][j-1];
                else 
                    test[i][j] = triangle[i][j] + Math.max(test[i-1][j-1], test[i-1][j]);
            }
        }
        
        for(int i=0; i<triangle.length; i++)
            answer = Math.max(answer, test[triangle.length-1][i]);
        
        return answer;
    }
}
