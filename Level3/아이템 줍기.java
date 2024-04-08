import java.util.*;
class Solution {
    static int[][] maze = new int[102][102];
    static boolean[][] visited = new boolean[102][102]; // 점의 이동이므로 맵을 2배 늘려준다
    static int answer = 0;
    static int[] dir_y = {-1, 0, 1, 0}; // 상우하좌
    static int[] dir_x = {0, 1, 0, -1};
    static class Point {
        int x, y, cnt;
        Point(int x, int y, int cnt) { this.x = x; this.y = y; this.cnt = cnt; }
    }
    public static boolean isOK(int a, int b) {
        return (0<=a && a<102 && 0<=b && b<102);
    }
    public static void init(int[][] rectangle) {
        for(int i=0; i<rectangle.length; i++) {
            int left_x = rectangle[i][0]*2;
            int left_y = rectangle[i][1]*2;
            int right_x = rectangle[i][2]*2;
            int right_y = rectangle[i][3]*2;
            // 영역과 테두리 표시
            for(int j=left_x; j<=right_x; j++) {
                for(int p=left_y; p<=right_y; p++) {
                    if(maze[p][j] == 1) continue;
                    maze[p][j] = 1;
                    if(p==left_y||p==right_y||j==left_x||j==right_x)
                        maze[p][j] = 2;
                }
            }
        }
    }
    public static void BFS(int x1, int y1, int x2, int y2) {
        Queue<Point> queue = new LinkedList<>();
        queue.add(new Point(x1, y1, 0));
        visited[y1][x1] = true;
        while(!queue.isEmpty()) {
            Point pt = queue.poll();
            if(pt.x == x2 && pt.y == y2) {
                answer = pt.cnt;
                break;
            } else {
                for(int i=0; i<4; i++) {
                    int dx = pt.x + dir_x[i];
                    int dy = pt.y + dir_y[i];
                    if(isOK(dx, dy)) {
                        if(!visited[dy][dx] && maze[dy][dx] == 2) {
                            visited[dy][dx] = true;
                            queue.add(new Point(dx, dy, pt.cnt+1));
                        }
                    }
                }
            }
        }
    }
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        characterX *= 2;
        characterY *= 2;
        itemX *= 2;
        itemY *= 2;
        
        init(rectangle);
        BFS(characterX, characterY, itemX, itemY);
        return (int)(answer / 2);
    }
}
