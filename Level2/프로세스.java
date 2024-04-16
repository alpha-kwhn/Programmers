import java.util.*;
class Solution {
    public class Point implements Comparable<Point> {
        int number;
        int priority;
        Point(int number, int priority) {
            this.number = number;
            this.priority = priority;
        }
        @Override
        public int compareTo(Point o) {
            return o.priority - this.priority;
        }
    }
    public int solution(int[] priorities, int location) {
        PriorityQueue<Point> queue = new PriorityQueue<>();
        ArrayList<Point> arr = new ArrayList<>();
        for(int i=0; i<priorities.length; i++) {
            queue.add(new Point(i, priorities[i]));
            arr.add(new Point(i, priorities[i]));
        }
        
        Queue<Point> alls = new LinkedList<>(arr);
        int answer = 0;
        while(!alls.isEmpty()) {
            Point pt = alls.poll();
            if(pt.priority == queue.peek().priority) {
                answer++;
                queue.poll();
                if(location == pt.number)
                    break;
            } else 
                alls.add(pt);
        }
        return answer;
    }
}
