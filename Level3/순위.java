import java.util.*;

class Solution {
    static ArrayList<Integer>[] win;
    static ArrayList<Integer>[] lose;
    static int answer = 0;
    
    static void DFS(int start, int n) {
        PriorityQueue<Integer> queue = new PriorityQueue<>();
        queue.add(start);
        boolean[] visited = new boolean[n+1];
        int count = 0;
        
        while(!queue.isEmpty()) {
            int target = queue.poll();
            for(int node: win[target]) {
                if(visited[node]) continue;
                else {
                    visited[node] = true;
                    count++;
                    queue.add(node);
                }
            }
        }
        
        Arrays.fill(visited, false);
        queue.add(start);
        while(!queue.isEmpty()) {
            int target = queue.poll();
            for(int node: lose[target]) {
                if(visited[node]) continue;
                else {
                    visited[node] = true;
                    count++;
                    queue.add(node);
                }
            }
        }
        
        if(count == n-1)
            answer++;
    }
    
    public int solution(int n, int[][] results) {
        win = new ArrayList[n+1];
        lose = new ArrayList[n+1];
        for(int i=0; i<n+1; i++) {
            win[i] = new ArrayList<>();
            lose[i] = new ArrayList<>();
        }
        
        for(int i=0; i<results.length; i++) {
            win[results[i][0]].add(results[i][1]);
            lose[results[i][1]].add(results[i][0]);
        }
        
        for(int i=1; i<=n; i++)
            DFS(i, n);
        
        return answer;
    }
}
