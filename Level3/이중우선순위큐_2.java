import java.util.*;
class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> queue = new PriorityQueue<>(Collections.reverseOrder());
        for(int i=0; i<operations.length; i++) {
            char opt = operations[i].charAt(0);
            if(opt == 'I') 
                queue.add(Integer.valueOf(operations[i].substring(2)));
            else {
                if(queue.isEmpty())
                    continue;
                char opt2 = operations[i].charAt(2);
                if(opt2 == '1')
                    queue.poll();
                else {
                    PriorityQueue<Integer> tmp = new PriorityQueue<>();
                    tmp.addAll(queue);
                    tmp.poll();
                    queue = new PriorityQueue<>(Collections.reverseOrder());
                    queue.addAll(tmp);
                }  
            }
        }
        
        if(queue.isEmpty())
            return new int[]{0, 0};
        else {
            int [] answer = new int[2];
            if(queue.size() == 1)
                answer = new int[]{queue.peek(), queue.peek()};
            else {
                answer[0] = queue.poll();
                while(queue.size() > 1)
                    queue.poll();
                answer[1] = queue.poll();
            }
            return answer;
        }
    }
}
