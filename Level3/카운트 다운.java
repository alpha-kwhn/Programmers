import java.util.*;

class Solution {
    public int[] solution(int target) {
        int [][] mem = new int[100001][2];
        mem[0][0] = 0;
        
        int [] answer = new int[2];
        
        for(int i=1; i<=100000; i++) {
            mem[i][0] = Integer.MAX_VALUE;
            mem[i][1] = 0;
        }
        
        for(int i=1; i<=20; i++) {
            mem[i][0] = 1;
            mem[i][1] = 1;
        }
        
        for(int i=21; i<=target; i++) {
            for(int j=1; j<=20; j++) {
                if(mem[i][0] > mem[i-j][0] + 1) {
                    mem[i][0] = mem[i-j][0] + 1;
                    mem[i][1] = mem[i-j][1] + 1;
                } else if(mem[i][0] == mem[i-j][0] + 1)
                    mem[i][1] = Math.max(mem[i][1], mem[i-j][1] + 1);
                
                if(i >= 2*j) {
                    if(mem[i][0] > mem[i-2*j][0] + 1) {
                        mem[i][0] = mem[i-2*j][0] + 1;
                        mem[i][1] = mem[i-2*j][1];
                    } 
                }
                
                if(i >= 3*j) {
                    if(mem[i][0] > mem[i-3*j][0] + 1) {
                        mem[i][0] = mem[i-3*j][0] + 1;
                        mem[i][1] = mem[i-3*j][1];
                    } 
                }
                
                if(i >= 50) {
                    if(mem[i][0] > mem[i-50][0] + 1) {
                        mem[i][0] = mem[i-50][0] + 1;
                        mem[i][1] = mem[i-50][1] + 1;
                    } else if(mem[i][0] == mem[i-50][0] + 1)
                        mem[i][1] = Math.max(mem[i][1], mem[i-50][1] + 1);
                }
            }
        }
        answer[0] = mem[target][0];
        answer[1] = mem[target][1];
        
        return answer;
    }
}
