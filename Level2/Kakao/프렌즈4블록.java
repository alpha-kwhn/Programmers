import java.util.*;
class Solution {
    public static String[][] maze;
    public static int M, N;
    public static int[] dir_x = {-1, -1, 0};
    public static int[] dir_y = {0, 1, 1};
    public static int answer = 0;
    public void init(String[] board, int m, int n) {
        N = n; 
        M = m;
        maze = new String[M][N];
        for(int i=0; i<M; i++) 
            for(int j=0; j<N; j++) 
                maze[i][j] = String.valueOf(board[i].charAt(j));
    }
    public void copyMaze(boolean[][] visited) {
        String[][] newOne = new String[M][N];
        for(int i=0; i<N; i++) {
            int j = M-1;
            int height = M-1;
            while(j >= 0) {      
                if(!visited[j][i]) {
                    newOne[height][i] = maze[j][i];
                    j--;
                    height--;
                } else
                    j--;
            }
            while(height >= 0) {
                newOne[height][i] = "";
                height--;
                answer++;
            }     
        }
        
        for(int i=0; i<M; i++)
            for(int j=0; j<N; j++)
                maze[i][j] = newOne[i][j];
    }
    public int solution(int m, int n, String[] board) {
        init(board, m, n);
        
        while(true) {
            int cnt = 0;
            boolean [][] visited = new boolean[m][n];
            for(int i=m-1; i>0; i--) {
                for(int j=0; j<n-1; j++) {
                    boolean able = true;
                    String start = maze[i][j];
                    if(start == "")
                        continue;
                    for(int p=0; p<3; p++) {
                        int dx = i + dir_x[p];
                        int dy = j + dir_y[p];
                        if(!start.equals(maze[dx][dy])){
                            able = false;
                            break;
                        }
                    }
                    if(able) {
                        visited[i][j] = true;
                        for(int p=0; p<3; p++) {
                            int dx = i + dir_x[p];
                            int dy = j + dir_y[p];
                            visited[dx][dy] = true;
                        }
                        cnt++;
                    }
                }
            }
            if(cnt == 0)
                break;
            else 
                copyMaze(visited);
        }
        return answer;
    }
}
