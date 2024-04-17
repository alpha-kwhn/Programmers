import java.util.*;
class Solution {
    public int solution(int[][] jobs) {
        // 작업 시작시간에 맞춤 오름차순 정렬
        PriorityQueue<int[]> queue = new PriorityQueue<>((e1, e2) -> {
            return e1[0] - e2[0];
        });
        // 작업 시간 짧은 순으로 오름차순 정렬
        PriorityQueue<int[]> work = new PriorityQueue<>((e1, e2) -> {
            return e1[1]-e2[1];
        });
        
        for(int i=0; i<jobs.length; i++)
            queue.add(jobs[i]);
        
        int time = 0;
        int answer = 0;
        int count = 0;
        while(count < jobs.length) {
            while(!queue.isEmpty() && queue.peek()[0] <= time) 
                work.add(queue.poll());
            if(work.isEmpty()) {
                time += (queue.peek()[0] - time);
            }else {
                int [] dis = work.poll();
                answer += (time - dis[0] + dis[1]);
                time += dis[1];
                count++;
            }
        }
        return (int)(answer / jobs.length);
    }
}
