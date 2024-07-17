class Solution {
    public int solution(int[] arr, int idx) {
        int answer = -1;
        if (arr[idx] == 1) {
            answer = idx;
        } else {
            for (int i = idx+1; i < arr.length; i++) {
                if (arr[i] == 1) {
                    answer = i;
                    break;
                }
            }
        }
        return answer;
    }
}