import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        Stack<Integer> stack = new Stack<>();
        ArrayList<Integer> [] arr = new ArrayList[board.length];
        int[] size = new int[board.length];
        int answer = 0;
        
        for(int i=0; i<board.length; i++) {
            ArrayList<Integer> ars = new ArrayList<>();
            for(int j=0; j<board.length; j++)
                if(board[j][i] > 0)
                    ars.add(board[j][i]);
            Collections.reverse(ars);
            arr[i] = ars;
            size[i] = ars.size();
        }
        
        for(int i=0; i<moves.length; i++) {
            int num = moves[i] - 1;
            if(size[num] > 0){
                int target = arr[num].get(size[num]-1);
                arr[num].remove(size[num]-1);
                size[num]--;
                if(!stack.isEmpty() && stack.peek() == target) {
                    answer += 2;
                    stack.pop();
                } else 
                    stack.push(target);
            }
        }
        
        return answer;
    }
}
