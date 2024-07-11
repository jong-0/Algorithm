import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] ans = new int[prices.length];
        Deque<Integer> dq = new ArrayDeque<>();
        
        for(int i = 0; i < prices.length; i++) {
            while (!dq.isEmpty()) {
                int j = dq.peek();
                if (prices[j] > prices[i]) {
                    ans[j] = i - j;
                    dq.pop();
                } else break;
            }
            dq.push(i);
        }
        
        while (!dq.isEmpty()) {
            int i = dq.pop();
            ans[i] = prices.length - i - 1;
        }
        return ans;
    }
}