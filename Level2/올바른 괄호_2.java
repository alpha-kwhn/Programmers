import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<String> stack = new Stack<>();
        
        for(int i=0; i<s.length(); i++) {
            if(stack.isEmpty()) {
                if(Character.toString(s.charAt(i)).equals(")"))
                    return false;
                else
                    stack.push(Character.toString(s.charAt(i)));
            } else {
                if(stack.peek().equals("(")) {
                    if(Character.toString(s.charAt(i)).equals("("))
                        stack.push(Character.toString(s.charAt(i)));
                    else
                        stack.pop();
                } else 
                    stack.push(Character.toString(s.charAt(i)));
            }
        }
        
        if(stack.isEmpty())
            return true;
        else
            return false;
    }
}
