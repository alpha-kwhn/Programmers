import java.util.*;
class Solution {
    static int answer = 0;
    static int amount = 0;
    static int[][] maze;
    public int solution(int k, int[][] dungeons) {
        amount = dungeons.length;
        maze = dungeons.clone();
        
        permutation(0, new boolean[dungeons.length], k);
        
        return answer;
    }
    
    public void permutation(int cnt, boolean[] visited, int num) {
        for(int i=0; i<amount; i++) {
            if(!visited[i] && num >= maze[i][0]) {
                visited[i] = true;
                cnt++;
                permutation(cnt, visited.clone(), num-maze[i][1]);
                visited[i] = false;
                cnt--;
            }
        }
        answer = Math.max(answer, cnt);
    }
}
