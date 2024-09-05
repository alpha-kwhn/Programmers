import java.util.*;
import java.util.stream.*;

class Solution {
    static int x;
    static int y;
    static boolean open;
    static int row;
    static int col;
    static int[] dir_x = {-1, 1, 0, 0};
    static int[] dir_y = {0, 0, 1, -1};
    static boolean[][] visited;

    public static boolean isOK(int a, int b) {
        return (0<=a && a<row && 0<=b && b<col);
    }
    
    public static class Node {
        int x;
        int y;
        int cost;
        Node(int x, int y, int cost){
            this.x = x;
            this.y = y;
            this.cost = cost;
        }
    }
    
    public int solution(String[] maps) {
        row = maps.length;
        col = maps[0].length();
        
        for(int i=0; i<maps.length; i++) {
            for(int j=0; j<maps[i].length(); j++) {
                if(String.valueOf(maps[i].charAt(j)).equals("S")) {
                    x = i;
                    y = j;
                }
            }
        }
        
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(x, y, 0));
        
        visited = new boolean[row][col];
        
        while(!queue.isEmpty()) {
            Node node = queue.poll();
            if(visited[node.x][node.y])
                continue;
            
            visited[node.x][node.y] = true;
            for(int i=0; i<4; i++) {
                int dx = node.x + dir_x[i];
                int dy = node.y + dir_y[i]; 
                int cst = node.cost;
                if(isOK(dx, dy) && !String.valueOf(maps[dx].charAt(dy)).equals("X") && !visited[dx][dy]) {
                    if(String.valueOf(maps[dx].charAt(dy)).equals("L")) {
                        open = true;
                        StringBuilder sb = new StringBuilder(maps[dx]);
                        sb.setCharAt(dy, '0');
                        maps[dx] = sb.toString();
                        visited = new boolean[row][col];
                        queue.clear();
                        queue.add(new Node(dx, dy, cst+1));
                        break;
                    } else if(String.valueOf(maps[dx].charAt(dy)).equals("E")) {
                        if(!open) {
                            queue.add(new Node(dx, dy, cst+1));
                            continue;
                        }
                        return cst+1;
                    } else {
                        queue.add(new Node(dx, dy, cst+1));
                    }
                }
            }
        }
        return -1;
    }
}
