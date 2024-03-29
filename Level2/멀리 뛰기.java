import java.util.*;
class Solution {
    public long solution(int n) {
        long [] arr = new long[n+1];
        if(n==1)
            return 1;
        else if(n==2)
            return 2;
        else {
            arr[1] = 1;
            arr[2] = 2;
            int start = 3;
            while(start <= n) {
                arr[start] = (arr[start-2] + arr[start-1]) % 1234567;
                start++;
            }
            return arr[n];
        }
    }
}
