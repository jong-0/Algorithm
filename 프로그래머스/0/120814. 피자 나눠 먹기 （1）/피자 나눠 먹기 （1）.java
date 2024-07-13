class Solution {
    public int solution(int num) {
        int answer = 0;
        int m = 0;
        int n = 0;
        
        m = num/7;
        n = num%7;
        
        if (n == 0) {
            answer = m;
        } else answer = m+1;
        
        
        return answer;
    }
}