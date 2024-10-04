import java.util.*;

class Solution {
    public int solution(int[] topping) {
        Map<Integer, Integer> top1 = new HashMap<>();
        Map<Integer, Integer> top2 = new HashMap<>();
        int idx = 1;
        int answer = 0;
        
        int t1 = 1;
        int t2 = 0;
        
        top1.put(topping[0], 1);
        
        for(int i=1; i<topping.length; i++) {
            if(top2.getOrDefault(topping[i], 0) == 0)
                t2++;
            top2.put(topping[i], top2.getOrDefault(topping[i], 0) + 1);
        }
        
        while(idx < topping.length - 1) {
            if(t1 == t2)
                answer++;
            
            top2.put(topping[idx], top2.get(topping[idx]) - 1);
            
            if(top2.get(topping[idx]) == 0)
                t2--;
            
            if(top1.getOrDefault(topping[idx], 0) == 0) {
                t1++;
                top1.put(topping[idx], top1.getOrDefault(topping[idx], 0) + 1);
            }
            
            idx++;
        }
        
        return answer;
    }
}
