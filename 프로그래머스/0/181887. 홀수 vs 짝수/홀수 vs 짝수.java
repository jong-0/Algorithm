class Solution {
    public int solution(int[] num_list) {
        int sum_e = 0;
        int sum_o = 0;
        
        for (int i = 0; i < num_list.length; i++) {
            if (i%2==0) {
                sum_e += num_list[i];
            } else sum_o += num_list[i];
        }
        
        if (sum_e > sum_o) {
            return sum_e;
        } else return sum_o;
    }
}