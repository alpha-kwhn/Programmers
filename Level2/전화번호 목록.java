import java.util.*;
class Solution {
    public boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        for(int i=0; i<phone_book.length-1; i++) {
            if(phone_book[i+1].contains(phone_book[i]))
                if(phone_book[i+1].substring(0, phone_book[i].length()).equals(phone_book[i]))
                    return false;
        }
        return true;
    }
}
