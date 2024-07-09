import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            String s = sc.next();
            if (s.length() == 1) {
                System.out.println(s+s);
            } else if (s.length() == 2) {
                System.out.println(s);
            } else {
                System.out.print(s.charAt(0));
                System.out.println(s.charAt(s.length()-1));
            }
        }
    }
}
