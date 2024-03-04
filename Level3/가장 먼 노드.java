import java.util.*;

class Solution {
    static class Node implements Comparable<Node> {
        int num;
        int cost;
        Node(int num, int cost) {
            this.num = num;
            this.cost = cost;
        }
        @Override
        public int compareTo(Node node) {
            return this.cost - node.cost;
        }
    }
    
    static ArrayList<Node>[] maze;
    static boolean[] visited;
    static PriorityQueue<Node> queue = new PriorityQueue<>();
    
    static int BFS(int[] costs, boolean[] visited) {
        while(!queue.isEmpty()) {
            Node target = queue.poll();
            if(visited[target.num]) continue;
            else {
                visited[target.num] = true;
                for(Node nde: maze[target.num]) {
                    if(costs[nde.num] > costs[target.num] + nde.cost) {
                        costs[nde.num] = costs[target.num] + nde.cost;
                        queue.add(new Node(nde.num, costs[nde.num]));
                    }
                }
            }
        }
        int maxi = 0;
        int answer = 0;
        for(int i=2; i<costs.length; i++) {
            if(costs[i] != Integer.MAX_VALUE) {
                maxi = Math.max(maxi, costs[i]);
            }
        }

        for(int i=2; i<costs.length; i++) {
            if(maxi == costs[i])
                answer += 1;
        }
        return answer;
    }
    // 방문 여부 체크는 pop한 후에 !!
    public int solution(int n, int[][] edge) {
        maze = new ArrayList[n+1];
        for(int i=0; i<n+1; i++)
            maze[i] = new ArrayList<>();
        for(int i=0; i<edge.length; i++) {
            maze[edge[i][0]].add(new Node(edge[i][1], 1));
            maze[edge[i][1]].add(new Node(edge[i][0], 1));
        }
        
        visited = new boolean[n+1];
        int [] cost = new int[n+1];
        Arrays.fill(cost, Integer.MAX_VALUE);
        
        queue.add(new Node(1, 0));
        cost[1] = 0;
        return BFS(cost, visited);
    }
}
