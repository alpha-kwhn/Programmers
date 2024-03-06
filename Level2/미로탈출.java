import java.util.*;

class Solution {
    static String[][] maze;
    static boolean[][] visited;
    static int start_x;
    static int start_y;
    static int labber_x;
    static int labber_y;
    static int end_x;
    static int end_y;
    static int[] dir_x = {0, 0, 1, -1};
    static int[] dir_y = {1, -1, 0, 0};
    static int answer;
    
    static boolean isOk(int a, int b, int max_a, int max_b) {
        return (0 <= a && a < max_a && 0 <= b && b < max_b);
    }
    
    static class Node {
        int x;
        int y;
        int cost;
        Node(int x, int y, int cost) {
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
    }
    
    static int BFS() {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(start_x, start_y, 0));
        boolean found = false;
        boolean exited = false;
        
        while(!queue.isEmpty()) {
            Node target = queue.poll();
            int cost = target.cost;
            for(int i=0; i<4; i++) {
                int dx = target.x + dir_x[i];
                int dy = target.y + dir_y[i];
                
                if(!isOk(dx, dy, maze.length, maze[0].length))
                    continue;
                
                if(visited[dx][dy])
                    continue;
                
                if(maze[dx][dy].equals("O") || maze[dx][dy].equals("E")) {
                    visited[dx][dy] = true;
                    queue.add(new Node(dx, dy, cost+1));
                    continue;
                }

                if(maze[dx][dy].equals("L")) {
                    queue.clear();
                    maze[start_x][start_y] = "O";
                    visited = new boolean[maze.length][maze[0].length];
                    visited[dx][dy] = true;
                    start_x = dx;
                    start_y = dy;
                    answer = cost+1;
                    found = true;
                    break;
                }
            }
        }
                
        if(!found)
            return -1;
        
        queue.add(new Node(start_x, start_y, answer));

        while(!queue.isEmpty()) {
            Node target = queue.poll();
            int cost = target.cost;
            for(int i=0; i<4; i++) {
                int dx = target.x + dir_x[i];
                int dy = target.y + dir_y[i];
                
                if(!isOk(dx, dy, maze.length, maze[0].length))
                    continue;
                
                if(visited[dx][dy])
                    continue;
                
                if(maze[dx][dy].equals("O")) {
                    visited[dx][dy] = true;
                    queue.add(new Node(dx, dy, cost+1));
                    continue;
                }
                
                if(maze[dx][dy].equals("E")) {
                    queue.clear();
                    answer = cost+1;
                    exited = true;
                    break;
                }
            }
        }
        
        if(!exited)
            return -1;
        
        return answer;
    }
    
    public int solution(String[] maps) {
        maze = new String[maps.length][maps[0].length()];
        visited = new boolean[maps.length][maps[0].length()];
        for(int i=0; i<maps.length; i++) {
            for(int j=0; j<maps[0].length(); j++) {
                char c = maps[i].charAt(j);
                maze[i][j] = String.valueOf(c);
                if(c == 'S') {
                    start_x = i;
                    start_y = j;
                } else if(c == 'L') {
                    labber_x = i;
                    labber_y = j;
                } else if(c == 'E') {
                    end_x = i;
                    end_y = j;
                }
            }
        }
        
        return BFS();
    }
}
