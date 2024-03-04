import java.util.*;

class Solution {
    static class Music implements Comparable<Music> {
        int num;
        int idx;
        Music(int num, int idx) {
            this.num = num;
            this.idx = idx;
        }
        @Override
        public int compareTo(Music music) {
            if(this.num == music.num)
                return this.idx - music.idx;
            return music.num - this.num;
        }
    }
    
    static HashMap<String, Integer> played = new HashMap<>();
    static HashMap<String, PriorityQueue<Music>> lists = new HashMap<>();
    
    public int[] solution(String[] genres, int[] plays) {
        for(int i=0; i<genres.length; i++) {
            if(played.containsKey(genres[i]))
                played.put(genres[i], played.get(genres[i]) + plays[i]);
            else
                played.put(genres[i], plays[i]);
            
            if(lists.containsKey(genres[i])) 
                lists.get(genres[i]).add(new Music(plays[i], i));
            else {
                lists.put(genres[i], new PriorityQueue<>());
                lists.get(genres[i]).add(new Music(plays[i], i));
            }
        }
        
        TreeMap<Integer, String> maps = new TreeMap<>(Comparator.reverseOrder());
        for(String streamed: played.keySet()) 
            maps.put(played.get(streamed), streamed);
                
        ArrayList<Integer> answer = new ArrayList<>();
        for(int number: maps.keySet()) {
            answer.add(((lists.get(maps.get(number))).poll()).idx);
            if(!lists.get(maps.get(number)).isEmpty())
                answer.add(((lists.get(maps.get(number))).poll()).idx);
        }
        
        int [] result = new int[answer.size()];
        for(int i=0; i<result.length; i++)
            result[i] = answer.get(i);
        
        return result;
    }
}
