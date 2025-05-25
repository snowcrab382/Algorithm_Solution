import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int i = sc.nextInt() - 1;
        System.out.println(s.charAt(i));
    }
}