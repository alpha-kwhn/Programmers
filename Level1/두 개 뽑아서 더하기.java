import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        TreeSet<Integer> sets = new TreeSet<>();
        
        for(int i=0; i<numbers.length; i++) 
            for(int j=0; j<numbers.length; j++) 
                if (i != j)
                    sets.add(numbers[i] + numbers[j]);
        
        int [] answer = new int[sets.size()];
        int idx = 0;
        
        for(Integer a : sets)
            answer[idx++] = a;
        
        return answer;
    }
}
