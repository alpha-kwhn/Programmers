import java.util.*;
class Solution {
    boolean solution(String s) {
        int balance = 0;
        for(int i=0; i<s.length(); i++) {
            String target = String.valueOf(s.charAt(i));
            if(target.equals(")")) {
                if(i == 0)
                    return false;
                else {
                    if(balance > 0) 
                        balance--;
                    else
                        return false;
                }
            } else {
                if(i == s.length()-1)
                    return false;
                else {
                    if(balance >= 0) 
                        balance++;
                    else
                        return false;
                }
            }
        }
        if(balance != 0)
            return false;
        else
            return true;
    }
}
