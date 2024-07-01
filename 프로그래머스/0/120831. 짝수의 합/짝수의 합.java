class Solution {
    public int solution(int n) {
        int start;
        int sum = 0;
        for (start = 1; start <= n; start++) {
            if (start%2 == 0) {
                sum += start;
            }
        }
        return sum;
    }
}