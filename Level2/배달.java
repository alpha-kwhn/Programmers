import java.util.*;
import java.util.stream.*;

class Solution {
    public class Node implements Comparable<Node> {
        int num;
        int cost;
        Node(int num, int cost) {
            this.num = num;
            this.cost = cost;
        }
        @Override 
        public int compareTo(Node e) {
            return this.cost - e.cost;
        }
    }
    
    public int solution(int N, int[][] road, int K) {
        ArrayList<Node>[] arr = new ArrayList[N+1];
        for(int i=1; i<=N; i++)
            arr[i] = new ArrayList<>();
        
        int[] costs = new int[N+1];
        Arrays.fill(costs, Integer.MAX_VALUE);
        
        for(int[] r : road) {
            arr[r[0]].add(new Node(r[1], r[2]));
            arr[r[1]].add(new Node(r[0], r[2]));
        }
        
        PriorityQueue<Node> queue = new PriorityQueue<>();
        queue.add(new Node(1, 0));
        
        while(!queue.isEmpty()) {
            Node node = queue.poll();
            int dest = node.num;
            for(Node nd : arr[dest]) {
                int nwDest = nd.num;
                if(costs[nwDest] > node.cost + nd.cost) {
                    costs[nwDest] = node.cost + nd.cost;
                    queue.add(new Node(nwDest, costs[nwDest]));
                }
            }
        }
        
        int answer = 1;
        for(int i=2; i<=N; i++) 
            if(costs[i] <= K) 
                answer++;
        
        return answer;
    }
}
