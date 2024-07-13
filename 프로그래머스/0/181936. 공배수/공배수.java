class Solution {
    public int solution(int num, int n, int m) {
        int ans = 0;
        if (num%n == 0 && num%m == 0) {
            ans = 1;
        }

        return ans;
    }
}