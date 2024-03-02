// 21억이 넘어가면 long 타입이어야 정수표현이 가능하다는 점을 정확히 숙지하자 (억 단위면 무작정 long으로 때려박기 금지)
// long 타입 값과 int 타입 값을 함께 계산하면 long 타입으로 취급됨
// ArrayList에 넣어서 값을 갱신해나가는 식으로 풀이한다면 메모리 초과 발생, Worst-Case를 정해두고 그 속에서 이분탐색을 해나가며 최적의 해를 구하는것이 바람직
// 접근법을 잘 기억해두자

import java.util.*;

// int * long = long, long * long = long, int는 21억까지, int * int = int
class Solution {
    public long solution(int n, int[] times) {  
        Arrays.sort(times);
        long answer = 1L;
        long left = 1L; 
        long right = (long)times[times.length-1] * n;
        long mid;
        long sum;
        
        while(left<=right) {
            mid = (left + right) / 2L;
            sum = 0L;
            
            for(int time: times)
                sum += (mid / time);
            
            if(sum < n) 
                left = mid + 1L;
            else if(sum >= n) {
                answer = mid;
                right = mid - 1L;
            }
        }
        return answer;
    }
}
