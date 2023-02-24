
import java.util.Scanner;

/**
 * InnerMainTest
 */
public class MainTest {
    static void printFrom_c(String S, char[] c) {
        for (int i = 0; i < S.length; i++) {
            System.out.print(c[i]);
        }
        System.out.println();
    }

    static void restoreInto_c(String S, char[] c) {
        for (int i = 0; i < S.length; i++) {
            c[i] = S.split("");
        }
    }

    public static void main(String[] args) {
        Scanner I = new Scanner(System.in);
        String S = I.next();
        char[] c = new char[S.length()];
        restoreInto_c(S,c);
        printFrom_c();
        I.close();
    }
}