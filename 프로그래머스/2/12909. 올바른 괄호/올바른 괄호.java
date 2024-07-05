import java.util.*;

class Solution {
    boolean solution(String s) {
        Deque<Character> dq = new ArrayDeque<>();
        boolean flag = true;
        
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                dq.push(c);
            } else if (c == ')') {
                if (!dq.isEmpty()) {
                    dq.pop();
                } else {
                    flag = false;
                    break;
                }
            }
        }
        if (!dq.isEmpty()) {
            flag = false;
        }
        return flag;
    }
}