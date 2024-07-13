class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int sum1 = 0;
        int sum2 = 0;
        int ans;
        
        if (arr1.length == arr2.length) {
            for (int i = 0; i < arr1.length; i++) {
                sum1 += arr1[i];
                sum2 += arr2[i];
            }
            if (sum1 == sum2) {
                ans = 0;
            } else if (sum1 > sum2) {
                ans = 1;
            } else ans = -1;
        } else {
            if (arr1.length > arr2.length) {
                ans = 1;
            } else ans = -1;
        }        
        return ans;
    }
}