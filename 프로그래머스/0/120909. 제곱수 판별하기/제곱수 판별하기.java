class Solution {
    public int solution(int n) {
        double i = Math.sqrt(n);
        int answer = 2;
        int chk = (int) i;
        if (n == chk*chk) {
            answer = 1;
        }
        return answer;
    }
}