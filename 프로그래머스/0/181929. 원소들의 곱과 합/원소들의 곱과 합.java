class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int mul = 1;
        int power = 0;
        
        for (int i = 0; i < num_list.length; i++) {
            mul *= num_list[i];
            power += num_list[i];
        }
        
        if (mul > power*power) {
            answer = 0;
        } else answer = 1;
        return answer;
    }
}