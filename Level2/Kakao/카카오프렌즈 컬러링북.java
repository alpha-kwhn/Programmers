import java.util.*;
class Solution {
    static int [] dir_x = {-1, 0, 1, 0};
    static int [] dir_y = {0, 1, 0, -1};
    static int[][] maze;
    static int[][] dp;
    static class Point implements Comparable<Point> {
        int num, cnt;
        Point(int num, int cnt) {
            this.num = num; this.cnt = cnt;
        }
        @Override
        public int compareTo(Point p) {
            if(this.cnt > p.cnt)
                return 1;
            else if(this.cnt < p.cnt)
                return -1;
            return 0;
        }
    }
    public static boolean isOK(int a, int b, int h, int w) {
        return (0 <= a && a < h && 0 <= b && b < w); 
    }
    public static int DFS(int a, int b) {
        if(dp[a][b] > -1) return 0; // 검사한곳은 집계 미포함
        dp[a][b] = 1;
        for(int i=0; i<4; i++) {
            int dx = a + dir_x[i];
            int dy = b + dir_y[i];
            if(isOK(dx, dy, maze.length, maze[0].length)) {
                if(maze[dx][dy] != 0 && maze[dx][dy] == maze[a][b])
                    dp[a][b] += DFS(dx, dy);
            }
        }
        return dp[a][b];
    }
    public int[] solution(int m, int n, int[][] picture) {
        PriorityQueue<Point> answer = new PriorityQueue<>(Comparator.reverseOrder());
        maze = new int[picture.length][picture[0].length];
        for(int i=0; i<picture.length; i++)
            for(int j=0; j<picture[0].length; j++)
                maze[i][j] = picture[i][j];
        dp = new int[picture.length][picture[0].length];
        for(int i=0; i<picture.length; i++) 
            Arrays.fill(dp[i], -1);
        for(int i=0; i<picture.length; i++) {
            for(int j=0; j<picture[0].length; j++) {
                if(picture[i][j] != 0 && dp[i][j] == -1) {
                    int num = DFS(i, j);
                    answer.add(new Point(picture[i][j], num));
                }
            }
        }
        
        return new int[]{answer.size(), answer.peek().cnt};
    }
}
