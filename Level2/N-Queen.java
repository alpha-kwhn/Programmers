import java.util.*;
class Solution {
    static int count = 0;
    static boolean isOk(int a, int b, int n) {
        return (0 <= a && a < n && 0 <= b && b < n);
    }
    public void combination(int depth, int r, 
                            boolean[] checked, ArrayList<int[]>pass) {
        if(depth == r) {
            count++;
            return;
        }
        
        for(int i=0; i<r; i++) {
            if(!checked[i]) {
                boolean able = true;
                for(int j=0; j<pass.size(); j++) {
                    int [] target = pass.get(j);
                    if(Math.abs(target[0]-depth) == Math.abs(i-target[1])) {
                        able = false;
                        break;
                    }
                }
                if(able) {
                    int [] ars = new int[]{depth, i};
                    checked[i] = true;
                    pass.add(ars);
                    combination(depth+1, r, checked, pass);
                    pass.remove(ars);
                    checked[i] = false;
                }
            }
        }
    }
    
    public int solution(int n) {
        for(int i=0; i<n; i++) {
            boolean [] checked = new boolean[n];
            ArrayList<int[]> arr = new ArrayList<>();
            checked[i] = true;
            arr.add(new int[]{0, i});
            combination(1, n, checked, arr);
        }
        return count;
    }
}
