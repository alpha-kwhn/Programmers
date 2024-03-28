import java.util.*;
class Solution {
    public int[] solution(int n, long k) {
        int count = 0;
        int [] answer = new int[n];
        ArrayList<Integer> arr = new ArrayList<>();
        long factorial = 1L;
        for(int i=1; i<=n; i++) {
            factorial *= i;
            arr.add(i);
        }
        k--;
        while(n > 0) {
            factorial /= n;
            int value = (int) (k / factorial);
            answer[count++] = arr.get(value);
            arr.remove(value);
            k %= factorial;
            n--;
        }
        
        return answer;
    }
}
