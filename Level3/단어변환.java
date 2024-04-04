import java.util.*;
class Solution {
    static boolean found = false;
    static boolean [] visited;
    static int answer = 0;
    class Node {
        String name; int count;
        Node(String name, int count) { this.name = name; this.count = count; }
    }
    public int solution(String begin, String target, String[] words) {
        visited = new boolean[words.length];
        for(int i=0; i<words.length; i++) {
            if(target.equals(words[i])) {
                found = true;
                break;
            }
        }
        if(!found) return 0;
        else {
            Queue<Node> queue = new LinkedList<>();
            queue.add(new Node(begin, 0));
            
            while(!queue.isEmpty()) {
                Node word = queue.poll();

                if(word.name.equals(target)) {
                    answer = word.count;
                    return answer;
                }
                    
                for(int i=0; i<words.length; i++) {
                    if(!visited[i]) {
                        int cnt = 0;
                        for(int j=0; j<words[i].length(); j++) {
                            if(word.name.charAt(j) != words[i].charAt(j)) {
                                if(cnt == 0) 
                                    cnt++;
                                else {
                                    cnt++;
                                    break;
                                }
                            }
                        }
                        if(cnt == 1) {
                            visited[i] = true;
                            queue.add(new Node(words[i], word.count + 1));
                        }
                    } else continue;
                }
            }
        }
        return 0;
    }
}
