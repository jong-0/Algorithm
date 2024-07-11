import java.util.*;

class Solution {
    public int solution(String s) {
        String ss = s + s;
        int ans = 0;
        
        for(int i = 0; i < s.length(); i++) {
            if(isValid(ss.substring(i,s.length()+i))) ans++;
        }
        return ans;
    }
    
    private boolean isValid(String s) {
        Deque<Character> dq = new ArrayDeque<>();
        
        for (char current : s.toCharArray()) {
            if (current == '(' || current == '{' || current == '[') {
                dq.push(current);
            } else {
                if (dq.isEmpty()) return false;
                
                char target = dq.pop();
                if ((target == '(' && current != ')') ||
                    (target == '[' && current != ']') ||
                    (target == '{' && current != '}')) {
                    return false;
                }
            }
        }
        return dq.isEmpty();
    }
}