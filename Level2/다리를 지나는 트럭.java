import java.util.*;
class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int time = 0;
        int idx = 0;
        int now_weight = 0;
        Queue<Integer> done = new LinkedList<>();
        Queue<Integer> on = new LinkedList<>();
        
        while(idx < truck_weights.length) {
            if(on.size() < bridge_length) {
                if(now_weight + truck_weights[idx] <= weight) {
                    on.add(truck_weights[idx]);
                    now_weight += truck_weights[idx++];
                } else 
                    on.add(0);
                time++;
            } else {
                done.add(on.peek());
                now_weight -= on.poll();
            }
        }
        if(!on.isEmpty()) 
            time += bridge_length;
        return time;
    }
}
