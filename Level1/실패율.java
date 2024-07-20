import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] maps = new int[N+1];
        int people = stages.length;
    
        for(int j=0; j<people; j++) 
            if(stages[j] < N+1)
                maps[stages[j]]++;
        
        TreeMap<Double, ArrayList<Integer>> sets = new TreeMap<>(Collections.reverseOrder());
        
        for(int i=1; i<=N; i++) {
            if(people > 0) {
                double percent = ((double)maps[i] / (double)people);
                ArrayList<Integer> tmp = new ArrayList<>();

                if(sets.containsKey(percent)) 
                    tmp = sets.get(percent);

                tmp.add(i);
                sets.put(percent, tmp);
                people -= maps[i];
            } else {
                ArrayList<Integer> tmp = new ArrayList<>();
                if(sets.containsKey(0.0)) 
                    tmp = sets.get(0.0);
                tmp.add(i);
                sets.put(0.0, tmp);
            }
        }
        
        ArrayList<Double> keys = new ArrayList<>(sets.keySet()); 
        ArrayList<Integer> answer = new ArrayList<>();
        
        for(Double ke : keys)
            answer.addAll(sets.get(ke));
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}
