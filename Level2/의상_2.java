import java.util.*;
import java.util.stream.*;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> info = new HashMap<>();
        
        for(String[] cloth : clothes) {
            String type = cloth[1];
            info.put(type, info.getOrDefault(type, 0) + 1);
        }
        
        ArrayList<Integer> arr = new ArrayList<>(info.values());
        int answer = 1;
        
        for(Integer val : arr) 
            answer *= (val+1);
        
        return answer-1;
    }
}
