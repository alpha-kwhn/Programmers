import java.util.*;
import java.util.stream.*;

class Solution {
    static int row;
    static int col;
    public class Node {
        int x;
        int y;
        int cost;
        int dir;
        
        Node(int x, int y, int cost, int dir) {
            this.x = x;
            this.y = y;
            this.cost = cost;
            this.dir = dir;
        }
    }
    
    public boolean isOK(int a, int b) {
        return (0<=a && a<row && 0<=b && b<col);
    }
    
    public int solution(int[][] board) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(0, 0, 0, -1));
        int answer = Integer.MAX_VALUE;
        
        row = board.length;
        col = board[0].length;
        
        int[] dir_x = {-1, 0, 1, 0};
        int[] dir_y = {0, 1, 0, -1};
        
        int[][][] visited = new int[board.length][board[0].length][4];
        
        while(!queue.isEmpty()) {
            Node node = queue.poll();
            for(int i=0; i<4; i++) {
                int dx = node.x + dir_x[i];
                int dy = node.y + dir_y[i];
                int cst = node.cost;
                
                if(!isOK(dx, dy))
                    continue;
                
                if(board[dx][dy] == 1)
                    continue;
                
                if(dx == 0 && dy == 0)
                    continue;
                
                if(node.dir == -1 || (node.dir - i) % 2 == 0)
                    cst += 100;
                else
                    cst += 600;
                
                if(dx == row-1 && dy == col-1)
                    answer = Math.min(answer, cst);
                else {
                    if(visited[dx][dy][i] == 0 || visited[dx][dy][i] > cst) {
                        visited[dx][dy][i] = cst;
                        queue.add(new Node(dx, dy, cst, i));
                    }
                }
            }
        }
        
        return answer;
    }
}
