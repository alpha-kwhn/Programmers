import java.util.*;

class Solution {
    static int answer = 0;
    static int diff = Integer.MAX_VALUE;
    static List<List<Integer>> cases = new ArrayList<>();
    
    static void simulation(boolean[][] visited, int r, int start) {
        for(int i=1; i<=r; i++) {
            if(!visited[start][i]) {
                visited[start][i] = true;
                visited[i][start] = true;
                answer++;
                simulation(visited, r, i);
                visited[start][i] = false;
                visited[i][start] = false;
            }
        }
    } 
    
    public int solution(int n, int[][] wires) {
        // 경우의 수 모두 구하기
        for(int i=0; i<wires.length; i++) {
            List<Integer> selected = new ArrayList<>();
            for(int j=0; j<wires.length; j++) 
                if(i != j) 
                    selected.add(j);
            cases.add(selected);
        }
        
        for(int i=0; i<cases.size(); i++) {
            List<Integer> testing = cases.get(i);
            boolean [][] visited = new boolean[n+1][n+1];
            
            for(int j=0; j<n+1; j++) 
                Arrays.fill(visited[j], true);
            
            for(int idx : testing) {
                visited[wires[idx][1]][wires[idx][0]] = false;
                visited[wires[idx][0]][wires[idx][1]] = false;
            }
            int idx = testing.get(0);
            simulation(visited, n, wires[idx][0]);
            int a = answer + 1;
            int b = n - a;
            diff = Math.min(diff, Math.abs(a-b));
            answer = 0;
        }
        
        return diff;
    }
}
