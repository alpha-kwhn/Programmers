import java.util.*;

class Solution
{
    public int solution(String s)
    {
        char[] arr = s.toCharArray();
        Deque<Character> stack = new ArrayDeque<>();
        
        for(Character c : arr) {
            if(stack.isEmpty())
                stack.addLast(c);
            else {
                if(stack.peekLast() == c)
                    stack.removeLast();
                else
                    stack.addLast(c);
            }
        }
        
        if(stack.isEmpty())
            return 1;
        else 
            return 0;
    }
}
