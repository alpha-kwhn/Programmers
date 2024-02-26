import java.util.*;

class Solution {
    static int N;
    static int M;
    static int X;
    static int Y;
    
    static int zone1(int a, int b) {
        int new_a = a;
        int new_b = (2*N)-b;
        return (int)(Math.pow(X-new_a, 2) + Math.pow(Y-new_b, 2));
    }
    
    static int zone2(int a, int b) {
        int new_a = (2*M)-a;
        int new_b = b;
        return (int)(Math.pow(X-new_a, 2) + Math.pow(Y-new_b, 2));
    }
    
    static int zone3(int a, int b) {
        int new_a = a;
        int new_b = -b;
        return (int)(Math.pow(X-new_a, 2) + Math.pow(Y-new_b, 2));
    }
    
    static int zone4(int a, int b) {
        int new_a = -a;
        int new_b = b;
        return (int)(Math.pow(X-new_a, 2) + Math.pow(Y-new_b, 2));
    }
    
    static int corner1(int a, int b) {
        int new_a = -a;
        int new_b = (2*N)-b;
        return (int)(Math.pow(X-new_a, 2) + Math.pow(Y-new_b, 2));
    }
    
    static int corner2(int a, int b) {
        int new_a = (2*M)-a;
        int new_b = (2*N)-b;
        return (int)(Math.pow(X-new_a, 2) + Math.pow(Y-new_b, 2));
    }
    
    static int corner3(int a, int b) {
        int new_a = (2*M)-a;
        int new_b = -b;
        return (int)(Math.pow(X-new_a, 2) + Math.pow(Y-new_b, 2));
    }
    
    static int corner4(int a, int b) {
        int new_a = -a;
        int new_b = -b;
        return (int)(Math.pow(X-new_a, 2) + Math.pow(Y-new_b, 2));
    }
    
    public int[] solution(int m, int n, int startX, int startY, int[][] balls) {
        N = n;
        M = m;
        X = startX;
        Y = startY;
        
        int [] answer = new int[balls.length];
        
        for(int i=0; i<balls.length; i++) {
            int dx = balls[i][0];
            int dy = balls[i][1];
            PriorityQueue<Integer> result = new PriorityQueue<>();
            
            // 한쪽면 돌리기 불가능 (1, 3 중 하나 불가)
            if(X == dx) {
                if(Y < dy) {
                    result.add(zone2(dx, dy));
                    result.add(zone3(dx, dy));
                    result.add(zone4(dx, dy));
                } else {
                    result.add(zone1(dx, dy));
                    result.add(zone2(dx, dy));
                    result.add(zone4(dx, dy));
                }
            }
            
            // 한쪽면 돌리기 불가능 (2, 4 중 하나 불가)
            else if(Y == dy) {
                if(X < dx) {
                    result.add(zone1(dx, dy));
                    result.add(zone3(dx, dy));
                    result.add(zone4(dx, dy));
                } else {
                    result.add(zone1(dx, dy));
                    result.add(zone2(dx, dy));
                    result.add(zone3(dx, dy));
                }
            }
            
            // 코너로 돌리기 가능함 + 기울기가 양수
            else if(Y/X == dy/dx) {
                result.add(zone1(dx, dy));
                result.add(zone2(dx, dy));
                result.add(zone3(dx, dy));
                result.add(zone4(dx, dy));
                if(X < dx) 
                    result.add(corner4(dx, dy));
                else 
                    result.add(corner2(dx, dy));
            } 
            
            // 코너로 돌리기 가능함 + 기울기가 음수
            else if(Y-N/X == dy-N/dx) { 
                result.add(zone1(dx, dy));
                result.add(zone2(dx, dy));
                result.add(zone3(dx, dy));
                result.add(zone4(dx, dy));
                if(X < dx) 
                    result.add(corner1(dx, dy));
                else 
                    result.add(corner3(dx, dy));
            }
            
            // 코너로 못돌리고, 모든 면으로 돌리기 가능 
            else {
                result.add(zone1(dx, dy));
                result.add(zone2(dx, dy));
                result.add(zone3(dx, dy));
                result.add(zone4(dx, dy));               
            }
            
            answer[i] = result.peek();
        }
        
        return answer;
    }
}
