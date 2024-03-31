import java.util.*;
class Solution {
    static int[] dir_x = {-1, 0, 1, 0};
    static int[] dir_y = {0, 1, 0, -1};
    static int answer = Integer.MAX_VALUE;
    static boolean [][] visited;
    static int N;
    static int M;
    public static boolean isOK(int a, int b) {
        return (0 <= a && a < N && 0 <= b && b < M);
    }
    static class Point implements Comparable<Point> {
        int x; int y; int time;
        Point(int x, int y, int time) { this.x = x; this.y = y; this.time = time;}
        @Override
        public int compareTo(Point o) {
            return this.time - o.time;
        }
    }
    public int solution(int[][] maps) {
        PriorityQueue<Point> queue = new PriorityQueue<>();
        queue.add(new Point(0, 0, 1));
        N = maps.length;
        M = maps[0].length;
        visited = new boolean[N][M];
        visited[0][0] = true;
        while(!queue.isEmpty()) {
            Point target = queue.poll();
            if(target.x == N-1 && target.y == M-1) {
                return target.time;
            } else {
                int dx = target.x;
                int dy = target.y;
                int sc = target.time;
                for(int i=0; i<4; i++) {
                    if(isOK(dx + dir_x[i], dy + dir_y[i])) {
                        if(!visited[dx + dir_x[i]][dy + dir_y[i]] 
                           && maps[dx + dir_x[i]][dy + dir_y[i]] == 1) {
                            visited[dx + dir_x[i]][dy + dir_y[i]] = true;
                            queue.add(new Point(dx + dir_x[i], dy + dir_y[i], sc+1));
                        }
                    }
                }
            }   
        }
        if(answer == Integer.MAX_VALUE)
            return -1;
        return answer;
    }
}
