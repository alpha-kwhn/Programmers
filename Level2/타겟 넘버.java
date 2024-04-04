import java.util.*;
class Solution {
    static int answer = 0;
    static int N;
    static int[] arr;
    class Num {
        int num;
        int cnt;
        Num(int num, int cnt) { this.num = num; this.cnt = cnt; }
    }
    public int solution(int[] numbers, int target) {
        arr = Arrays.copyOf(numbers, numbers.length);
        N = numbers.length;
        Queue<Num> queue = new LinkedList<>();
        queue.add(new Num(numbers[0], 0));
        queue.add(new Num(numbers[0] * -1, 0));
        
        while(!queue.isEmpty()) {
            Num nums = queue.poll();
            if(nums.cnt == N-1) {
                if(nums.num == target)
                    answer++;
                continue;
            }
            
            queue.add(new Num(nums.num + numbers[nums.cnt+1], nums.cnt+1));
            queue.add(new Num(nums.num - numbers[nums.cnt+1], nums.cnt+1));
        }
        
        return answer;
    }
}
