import java.util.*;
import java.util.stream.*;

class Solution {
    static boolean[] visited;
    static ArrayList<Integer>[] node;
    static int answer = 0;
    
    public static void dfs(int x) {
        for(Integer num : node[x]) {
            if(visited[num])
                continue;
            visited[num] = true;
            dfs(num);
        }
    }

    public int solution(int n, int[][] computers) {
        node = new ArrayList[n];
        visited = new boolean[n];
        for(int i=0; i<n; i++)
            node[i] = new ArrayList<>();
        
        for(int i=0; i<n; i++) {
            for(int j=0; j<computers[i].length; j++) {
                if(i == j)
                    continue;
                if(computers[i][j] == 1) 
                    node[i].add(j);
            }
        }
        
        for(int i=0; i<n; i++) {
            if(visited[i])
                continue;
            visited[i] = true;
            dfs(i);
            answer++;
        }
        
        return answer;
    }
    
    
}
