import java.util.*;

class Solution {
    static int BinarySearch(ArrayList<Integer> deque, int num) {
        int left = 0;
        int right = deque.size();
        int mid;
        
        while(left<right) {
            mid = (left+right) / 2;
            if(deque.get(mid) < num) 
                left = mid+1;
            else if(deque.get(mid) > num)
                right = mid-1;
            else 
                return mid;
        }
        return left;
    }
    
    public int[] solution(String[] operations) {
        ArrayList<Integer> deque = new ArrayList<>();
        for(String opt: operations) {
            if(opt.charAt(0) == 'I') {
                if(deque.size() == 0) {
                    deque.add(Integer.parseInt(opt.substring(2)));
                } else {
                    int number = Integer.parseInt(opt.substring(2));
                    int idx = BinarySearch(deque, number);
                    deque.add(idx, number);
                }
            } else {
                if(deque.size() > 0) {
                    if(opt.charAt(2) == '-') 
                        deque.remove(0);
                    else
                        deque.remove(deque.size()-1);
                } else continue;
            }
        }
        
        int [] answer;
        if(deque.isEmpty())
            answer = new int[]{0, 0};
        else
            answer = new int[]{deque.get(deque.size()-1), deque.get(0)};
        return answer;
    }
}
