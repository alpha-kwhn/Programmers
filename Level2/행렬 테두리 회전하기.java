import java.util.*;

class Solution {
    static int [][] maze;
    static int [] answer;
    
    static void simulation(int [] query, int [][] tmp, int idxe) {
        int direction = 1; // 1: 우, 2: 하, 3: 좌, 4: 상
        int row = query[0];
        int col = query[1];
        List<Integer> maxi = new ArrayList<>();
        
        while(direction < 5) {
            if(direction == 1) {
                if(col + 1 <= query[3]) {
                    col += 1;
                    tmp[row][col] = maze[row][col-1];
                } else {
                    row += 1;
                    tmp[row][col] = maze[row-1][col];
                    direction += 1;
                }
            } else if(direction == 2) {
                if(row + 1 <= query[2]) {
                    row += 1;
                    tmp[row][col] = maze[row-1][col];
                } else {
                    col -= 1;
                    tmp[row][col] = maze[row][col+1];
                    direction += 1;
                }
            } else if(direction == 3) {
                if(col - 1 >= query[1]) {
                    col -= 1;
                    tmp[row][col] = maze[row][col+1];
                } else {
                    row -= 1;
                    tmp[row][col] = maze[row+1][col];
                    direction += 1;
                }
            } else {
                if(row - 1 >= query[0]) {
                    row -= 1;
                    tmp[row][col] = maze[row+1][col];
                } else 
                    break;
            }
            maxi.add(tmp[row][col]);
        }
        
        for(int i=0; i<maze.length; i++) 
            maze[i] = Arrays.copyOf(tmp[i], tmp[0].length);
        
        Collections.sort(maxi);
        answer[idxe] = maxi.get(0);
    }
    
    public int[] solution(int rows, int columns, int[][] queries) {
        maze = new int[rows+1][columns+1];
        answer = new int[queries.length];
        
        int number = 1;
        for(int i=1; i<rows+1; i++) {
            for(int j=1; j<columns+1; j++) {
                maze[i][j] = number;
                number++;
            }
        }
        
        for(int i=0; i<queries.length; i++) {
            int [][] test = new int[rows+1][columns+1];
            for(int j=0; j<rows+1; j++)
                test[j] = Arrays.copyOf(maze[j], columns+1);
            simulation(queries[i], test, i);
        }
        
        return answer;
    }
}
