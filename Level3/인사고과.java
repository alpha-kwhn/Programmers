import java.util.*;

class Solution {
    public class Worker implements Comparable<Worker> {
        int a;
        int b;
        
        Worker(int a, int b) {
            this.a = a;
            this.b = b;
        }
        
        @Override
        public int compareTo(Worker worker) {
            if(this.a == worker.a) 
                return Integer.compare(this.b, worker.b);
            else 
                return Integer.compare(worker.a, this.a);
        }
    }
    
    public int solution(int[][] scores) {
        
        if(scores.length == 1) return 1;
        
        ArrayList<Worker> arr = new ArrayList<>();
        
        for(int i=0; i<scores.length; i++) 
            arr.add(new Worker(scores[i][0], scores[i][1]));
        
        Collections.sort(arr);
        
        int maxi = arr.get(0).b;
        
        for(int i=1; i<arr.size(); i++) {
            if(arr.get(i).b < maxi) {
                if(arr.get(i).a == scores[0][0] && arr.get(i).b == scores[0][1])
                    return -1;
                arr.set(i, new Worker(-1, -1));
            } else 
                maxi = arr.get(i).b;
        }
        
        Collections.sort(arr, (s1, s2) -> Integer.compare(s2.a+s2.b, s1.a+s1.b));
        
        int grade = 1;
        
        for(int i=0; i<arr.size(); i++) {
            if(arr.get(i).score == (scores[0][0] + scores[0][1]))
                break;
            else
                grade += 1;
        }
          
        return grade;
    }
}
