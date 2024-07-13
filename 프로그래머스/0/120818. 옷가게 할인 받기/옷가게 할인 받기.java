class Solution {
    public int solution(int price) {
        int ans;
        
        if (price < 100000) {
            ans = price;
        } else if (price < 300000) {
            ans = (int) (price*0.95);
        } else if (price < 500000) {
            ans = (int) (price*0.9);
        } else ans = (int) (price*0.8);
        
        return ans;
    }
}