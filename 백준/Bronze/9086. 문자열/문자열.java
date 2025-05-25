import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            String s = sc.next();

            char start = s.charAt(0);
            char end = s.charAt(s.length() - 1);

            sb.append(start).append(end).append("\n");
        }
        System.out.println(sb);
    }
}