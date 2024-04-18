import java.util.*;
// 크루스칼 알고리즘을 적용한 MST 문제 (최소 신장으로 사이클 없는 순환 구하기)
class Solution {
    static int[] parent;
    // 시작 부모를 찾는 알고리즘
    public int find(int a) {
        if(parent[a] == a) return a;
        else return parent[a] = find(parent[a]);
    }
    // 그래프 관계 형성 알고리즘
    public void union(int a, int b) {
        a = find(a);
        b = find(b);
        if(a != b)
            parent[b] = a;
    }
    public int solution(int n, int[][] costs) {
        int answer = 0;
        parent = new int[n];
        for(int i=0; i<n; i++)
            parent[i] = i;
        // 비용 기준으로 오름차순 정렬
        Arrays.sort(costs, (e1, e2) -> e1[2]-e2[2]);
        // 크루스칼
        for(int i=0; i<costs.length; i++) {
            if(find(costs[i][0]) != find(costs[i][1])) {
                union(costs[i][0], costs[i][1]);
                answer += costs[i][2];
            }
        }
        return answer;
    }
}
