import java.util.*;
import java.util.stream.*;

class Solution
{
    public int solution(int n, int a, int b)
    {
        int A = n + (a-1);
        int B = n + (b-1);
        int answer = 0;
        
        while(A != B) {
            A = (A % 2 == 1) ? (A-1) / 2 : A / 2;
            B = (B % 2 == 1) ? (B-1) / 2 : B / 2;
            answer++;
        }
        
        return answer;
    }
}
