class Solution {
    public String solution(String new_id) {
        new_id = new_id.toLowerCase();
        
        StringBuilder sb = new StringBuilder();
        for (char c : new_id.toCharArray()) {
            if (c >= 'a' && c <= 'z' || c >= '0' && c <= '9' || c == '-' || c == '_' || c == '.') {
                sb.append(c);
            }
        }
        new_id = sb.toString();
        
        sb = new StringBuilder();
        boolean flag = false;
        for (char c : new_id.toCharArray()) {
            if (c == '.') {
                if (!flag) {
                    sb.append(c);
                    flag = true;
                }
            } else {
            sb.append(c);
            flag = false;
            }
        }
        new_id = sb.toString();
        
        while (new_id.startsWith(".")) {
        new_id = new_id.substring(1);
        }
        while (new_id.endsWith(".")) {
            new_id = new_id.substring(0, new_id.length() - 1);
        }

        if (new_id.isEmpty()) {
            new_id = "a";
        }

        if (new_id.length() >= 16) {
            new_id = new_id.substring(0, 15);
            if (new_id.endsWith(".")) {
                new_id = new_id.substring(0, 14);
            }
        }

        while (new_id.length() <= 2) {
            new_id += new_id.charAt(new_id.length() - 1);
        }
        return new_id;
    }
}