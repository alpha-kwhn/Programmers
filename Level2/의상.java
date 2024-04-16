import java.util.*;
class Solution {
    static Map<String, Integer> wear = new HashMap<>();
    public int solution(String[][] clothes) {        
        for(String[] clo : clothes) {
            if(!wear.containsKey(clo[1]))
                wear.put(clo[1], 2);
            else {
                int tmp = wear.get(clo[1]);
                wear.put(clo[1], tmp+1);
            }
        }
        
        ArrayList<String> arr = new ArrayList<>(wear.keySet());
        
        int tmp = 1;
        int answer = 0;
        for(int i=0; i<arr.size(); i++) 
            tmp *= wear.get(arr.get(i));
        answer += tmp;
        
        return answer-1;
    }
}
