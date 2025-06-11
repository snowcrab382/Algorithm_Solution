import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 여러 번 출력하는 경우 StringBuilder를 사용하는 것이 효율적입니다.
        StringBuilder sb = new StringBuilder(); 

        Stack<Integer> stack = new Stack<>();
        int n = Integer.parseInt(br.readLine().trim());

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            String command = line[0];

            // 이전 방식의 switch 문으로 수정
            switch (command) {
                case "1":
                    stack.add(Integer.parseInt(line[1]));
                    break; // break 추가
                case "2":
                    if (!stack.isEmpty()) {
                        sb.append(stack.pop()).append('\n');
                    } else {
                        sb.append(-1).append('\n');
                    }
                    break; // break 추가
                case "3":
                    sb.append(stack.size()).append('\n');
                    break; // break 추가
                case "4":
                    if (stack.isEmpty()) {
                        sb.append(1).append('\n');
                    } else {
                        sb.append(0).append('\n');
                    }
                    break; // break 추가
                case "5":
                    if (stack.isEmpty()) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(stack.peek()).append('\n');
                    }
                    break; // break 추가
            }
        }
        // 모아둔 출력을 한 번에 처리
        System.out.print(sb);
    }
}