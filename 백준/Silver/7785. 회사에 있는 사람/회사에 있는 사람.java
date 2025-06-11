import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        Set<String> log = new HashSet<>();
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            String name = sc.next();
            String action = sc.next();

            if (action.equals("enter")) {
                log.add(name);
            } else {
                log.remove(name);
            }
        }

        String[] arr = log.toArray(String[]::new);
        Arrays.sort(arr, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for (String name : arr) {
            sb.append(name).append("\n");
        }
        System.out.print(sb.toString().trim());

    }
}
