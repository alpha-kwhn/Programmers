import java.util.*;
class Solution {
    public int solution(int N, int number) {
        Set<Integer> [] arr = new HashSet[10];
        
        for(int i=1; i<9; i++) {
            int num = Integer.parseInt(String.valueOf(N).repeat(i));
            arr[i] = new HashSet<>();
            arr[i].add(num);
        }
        
        int use = 2;
        while(use <= 8) {
            for(int j=1; j<use; j++) {
                ArrayList<Integer> first = new ArrayList<>(arr[j]);
                ArrayList<Integer> second = new ArrayList<>(arr[use-j]);
                for(int k=0; k<first.size(); k++) {
                    int a = first.get(k);
                    for(int p=0; p<second.size(); p++) {
                        int b = second.get(p);
                        arr[use].add(a+b);
                        arr[use].add(a-b);
                        arr[use].add(a*b);
                        if(b != 0)
                            arr[use].add((int)a/b);
                    }
                }
            }
            use++;
        }
        
        for(int i=1; i<=8; i++) {
            ArrayList<Integer> tmp = new ArrayList<>(arr[i]);
            for(int j=0; j<tmp.size(); j++) 
                if(tmp.get(j) == number)
                    return i;
        }
        
        return -1;
    }
}
