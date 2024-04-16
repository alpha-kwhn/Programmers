import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i=0; i<arr.length; i++) {
            if(i == 0)
                answer.add(arr[0]);
            else if(arr[i] != arr[i-1])
                answer.add(arr[i]);
        }
        int[] result = new int[answer.size()];
        for(int i=0; i<answer.size(); i++)
            result[i] = answer.get(i);
        return result;
    }
}
