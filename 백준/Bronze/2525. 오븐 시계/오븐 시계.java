import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int n = sc.nextInt();

        if (m + n >= 60) {
            if (((m+n)/60 + h) >= 24) {
                System.out.println(((m+n)/60 + h)%24 + " " + (m+n)%60);
            } else System.out.println(((m+n)/60 + h) + " " + (m+n)%60);
        } else System.out.println(h + " " + (m+n));
    }
}
