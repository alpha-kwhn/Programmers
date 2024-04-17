import java.util.*;
class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        for(int i=0; i<scoville.length; i++)
            queue.add(scoville[i]);
        while(!queue.isEmpty()) {
            int mildest = queue.poll();
            if(queue.isEmpty() && mildest < K)
                break;
            if(mildest >= K)
                return answer;
            else {
                int mild = queue.poll();
                queue.add(mildest + (mild * 2));
                answer++;
            }
        }
        return -1;
    }
}
