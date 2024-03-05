import java.util.*;

class Solution {    
    static ArrayList<String> total = new ArrayList<>();
    static void DFS(boolean[] visited, int depth, String[][] ticket, String start, String answer) {
        if (depth == ticket.length) {
            total.add(answer);
            return;
        } else {
            for (int i = 0; i < ticket.length; i++) {
                if (ticket[i][0].equals(start) && !visited[i]) {
                    visited[i] = true;
                    DFS(visited, depth + 1, ticket, ticket[i][1], answer + " " + ticket[i][1]);
                    visited[i] = false;
                }
            }
        }
    }

    public String[] solution(String[][] tickets) {
        ArrayList<String> answer = new ArrayList<>();
        answer.add("ICN");
        
        DFS(new boolean[tickets.length], 0, tickets, "ICN", "ICN");
        Collections.sort(total);
        String[] results = total.get(0).split(" ");
        return results;
    }
}
