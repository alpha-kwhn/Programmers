import java.util.*;
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> time = new ArrayList<>();
        ArrayList<Integer> fin = new ArrayList<>();
        
        for(int i=0; i<progresses.length; i++) {
            int target = (int)(Math.ceil((100-progresses[i]) / speeds[i]));
            int left = (100-progresses[i]) % speeds[i];
            if(left > 0)
                target += 1;
            time.add(target);
        }
        
        Queue<Integer> queue = new LinkedList<>();
        queue.addAll(time);
        
        int answer = queue.poll();
        int cnt = 1;
        while(!queue.isEmpty()) {
            int tmp = queue.peek();
            if(answer >= tmp) {
                queue.poll();
                ++cnt;
            } else {
                fin.add(cnt);
                answer = queue.poll();
                cnt = 1;
            }
        }
        fin.add(cnt);

        int [] result = new int[fin.size()];
        for(int i=0; i<fin.size(); i++) 
            result[i] = fin.get(i);
        return result;
    }
}
