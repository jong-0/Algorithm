class Solution {
    public int solution(String number) {
        int answer = 0;
        int sum = 0;
        String[] li = number.split("");
        for(int i = 0; i<li.length; i++){
            sum+=Integer.parseInt(li[i]);
        }
        answer = sum%9;
        return answer;
    }
}