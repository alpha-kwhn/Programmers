import java.util.*;

class Solution {
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int [][] maze = new int[n+1][n+1];
        
        for(int i=0; i<maze.length; i++) {
            Arrays.fill(maze[i], (10000*n)+1);
            maze[i][i] = 0;
        }
        
        for(int i=0; i<fares.length; i++) {
            maze[fares[i][0]][fares[i][1]] = fares[i][2];
            maze[fares[i][1]][fares[i][0]] = fares[i][2];
        }
        
        for(int i=1; i<n+1; i++) {
            for(int j=1; j<n+1; j++) {
                for(int p=1; p<n+1; p++) {
                    if(maze[j][i] + maze[i][p] < maze[j][p])
                        maze[j][p] = maze[j][i] + maze[i][p];
                }
            }
        }
        
        int min_a = maze[s][a];
        int min_b = maze[s][b];
        int mix = (100000 * n) + 1;
        
        for(int i=1; i<n+1; i++) {
            if(i == a) {
                mix = Math.min(mix, maze[s][a] + maze[a][b]);
            } else if(i == b) {
                mix = Math.min(mix, maze[s][b] + maze[b][a]);
            } else {
                mix = Math.min(mix, maze[s][i] + maze[i][a] + maze[i][b]);
            }
        }
        
        return Math.min(mix, min_a+min_b);
    }
}
