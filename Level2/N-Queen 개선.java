import java.util.*;

class Solution {
    static int answer = 0;
    static int N;
    static boolean[] visitCol;
    static boolean[] visitRow;
    static boolean[] visitCross_1;
    static boolean[] visitCross_2;
    
    // 대각선 존재 여부 파악법 -> 행 + 열 좌표값이 같으면 같은 대각선
    // "" 2 -> 행 - 열 + N 값이 같으면 대각선에 위치
    
    public static void backtrack(int row) {
        if(row == N) {
            answer++;
            return;
        }
        
        for(int i=0; i<N; i++) {
            if(!visitCol[i] && !visitRow[row] && !visitCross_1[row+i] && !visitCross_2[i - row + N]) {
                visitCol[i] = true;
                visitRow[row] = true;
                visitCross_1[row+i] = true;
                visitCross_2[i - row + N] = true;
                backtrack(row+1);
                visitCol[i] = false;
                visitRow[row] = false;
                visitCross_1[row+i] = false;
                visitCross_2[i - row + N] = false;
            }
        }
    }
    
    public int solution(int n) {
        N = n;
        visitCol = new boolean[N];
        visitRow = new boolean[N];
        visitCross_1 = new boolean[2*N];
        visitCross_2 = new boolean[2*N];
        backtrack(0);
        
        return answer;
    }
}
