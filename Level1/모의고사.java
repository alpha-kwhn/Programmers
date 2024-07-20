import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        
        int[] a = {1, 2, 3, 4, 5};
        int[] b = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] c = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        
        int score_a = 0;
        int score_b = 0;
        int score_c = 0;
        
        for(int i=0; i<answers.length; i++) {
            int ans = answers[i];
            
            if(ans == a[i%5])
                score_a++;
            
            if(ans == b[i%8])
                score_b++;
            
            if(ans == c[i%10])
                score_c++;
        }
        
        int maxi = Math.max(Math.max(score_a, score_b), score_c);
        
        HashMap<Integer, Integer> maps = new HashMap<>();
        maps.put(1, score_a);
        maps.put(2, score_b);
        maps.put(3, score_c);
        
        ArrayList<Integer> keys = new ArrayList<>(maps.keySet());
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(Integer ke : keys)
            if(maps.get(ke) == maxi)
                answer.add(ke);
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
