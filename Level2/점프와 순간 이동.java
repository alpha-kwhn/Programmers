import java.util.*;

// K칸 점프, 누적거리 * 2 칸으로 순간이동
// 점프한 칸 만큼 소모, 순간이동은 미소모
// 점프 횟수 최소화

public class Solution {
    public int solution(int n) {
        int energy = 0;
        while(n > 0) {
            if(n % 2 == 1) {
                energy++;
                n--;
            } else 
                n /= 2;
        }
        return energy;
    }
}
