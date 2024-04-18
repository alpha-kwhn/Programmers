import java.util.*;
class Solution {
    public String solution(String number, int k) {
        int tmp = k;
        Stack<Character> stack = new Stack<>();
        for(int i=0; i<number.length(); i++) {
            int now = number.charAt(i);
            while(!stack.isEmpty() && stack.peek() < now && k > 0) {
                stack.pop();
                k--;
            }
            stack.push(number.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<number.length()-tmp; i++)
            sb.append(stack.get(i));
        return sb.toString();
    }
}
