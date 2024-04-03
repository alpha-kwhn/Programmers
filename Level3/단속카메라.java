import java.util.*;
class Solution {
    public int solution(int[][] routes) {
        Arrays.sort(routes, (e1, e2) -> {
            if(e1[0] < e2[0]) 
                return -1;
            else if(e1[0] > e2[0])
                return 1;
            return 0;
        });
        int tmp = routes[0][1];
        int idx = 0;
        ArrayList<ArrayList<Integer>> point = new ArrayList<>();
        point.add(new ArrayList<>(0));
        for(int i=1; i<routes.length; i++) {
            if(routes[i][0] <= tmp) {
                if(routes[i][1] >= tmp)
                	point.get(idx).add(i);
                else {
                    tmp = routes[i][1];
                    point.get(idx).add(i);
                }
            } else {
                idx++;
                point.add(new ArrayList<>(i));
                tmp = routes[i][1];
            }
        }
        int result = 0;
        return point.size();
    }
}
