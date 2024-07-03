class Solution {
    public int[] solution(int[] num_list) {
        int even = 0;
        int odd = 0;
        for (int i = 0; i<num_list.length; i++) {
            if (num_list[i]%2 ==0) {
                even += 1;
            } else {
                odd += 1;
            }
        }
        int[] answer = {even, odd};
        return answer;
    }
}