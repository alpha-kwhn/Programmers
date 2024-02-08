import java.util.*;

class Solution {
    
    static int N;
    static int M;
    static int [] dir_x = {0, 1};
    static int [] dir_y = {1, 0};
    static int [][] maze;
    
    public boolean isOK(int a, int b) {
        return (0 <= a && a < N && 0 <= b && b < M);
    }
    
    public int solution(int m, int n, int[][] puddles) {
        maze = new int[n][m];
        maze[0][0] = 1;
        
        N = n;
        M = m;

        for(int i=0; i<puddles.length; i++) 
            maze[puddles[i][1]-1][puddles[i][0]-1] = -1;
        
        for(int a=0; a<n; a++) {
            for(int b=0; b<m; b++) {
                if(maze[a][b] == -1) continue;
                
                for(int i=0; i < 2; i++) {
                    int dx = a + dir_x[i];
                    int dy = b + dir_y[i];

                    if(isOK(dx, dy)) {
                        if(maze[dx][dy] != -1) {
                            maze[dx][dy] += maze[a][b];
                            if(maze[dx][dy] > 1000000007) maze[dx][dy] %= 1000000007;
                            // 효율성 테스트 관건 포인트
                        }
                    }
                }
            }
        }
        
        return (maze[N-1][M-1]);
    }
}
