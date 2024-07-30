import java.util.*;

class Solution {
    public int solution(String s) {
        int size = s.length();
        int answer = 0;
        
        for(int i=0; i<size; i++) {
            Deque<Character> deque = new ArrayDeque<>();
            boolean able = true;
            
            for(int j=i; j<i+size; j++) {
                char tmp = s.charAt(j % size);
                if(deque.isEmpty()) {
                    if(tmp == ']' || tmp == ')' || tmp == '}') {
                        able = false;
                        break;
                } else
                        deque.addLast(tmp);
                } else {
                    if(deque.peekLast() == '(') {
                        if(tmp == ')')
                            deque.removeLast();
                        else 
                            deque.addLast(tmp);
                    } else if(deque.peekLast() == '{') {
                        if(tmp == '}')
                            deque.removeLast();
                        else 
                            deque.addLast(tmp);
                    } else if(deque.peekLast() == '[') {
                        if(tmp == ']')
                            deque.removeLast();
                        else 
                            deque.addLast(tmp);
                    } else 
                        deque.addLast(tmp);
                }
            }
            if(able && deque.isEmpty())
                answer++;
        }
        return answer;
    }
}
