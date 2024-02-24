import java.util.*;

class Solution {
    public int solution(int N, int number) {
        List<Set<Integer>> lis = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        int answer = -1;
        
        for(int i=0; i<=9; i++) {
            lis.add(new HashSet<>());
            if(i >= 1) {
                sb.append(N);
                lis.get(i).add(Integer.parseInt(sb.toString()));
            }
        }
        
        for(int i=2; i<=9; i++) {
            for(int j=1; j<i; j++) {
                for(int a: lis.get(i-j)) {
                    for(int b: lis.get(j)) {
                        lis.get(i).add(a+b);
                        lis.get(i).add(a-b);
                        lis.get(i).add(a*b);
                        if(b > 0)
                            lis.get(i).add((int)a/b);
                    }
                }
            }
        }
        
        for(int i=0; i<=9; i++) {
            if(lis.get(i).contains(number)) {
                answer = i;
                break;
            }
        }
        
        return answer;
    }
}
