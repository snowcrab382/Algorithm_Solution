import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        int answer = Integer.MAX_VALUE;

        for (int idx = 0; idx < n-1; idx++) {
            List<List<Integer>> graph = new ArrayList<>();
            for (int i = 0; i < n+1; i++) {
                graph.add(new ArrayList<>());
            }
            
            for (int i = 0; i < n-1; i++) {
                if (i == idx) {
                    continue;
                }
                graph.get(wires[i][0]).add(wires[i][1]);
                graph.get(wires[i][1]).add(wires[i][0]);
            }

            int tmp = 0;
            for (int i = 1; i < n+1; i++) {
                if (!graph.get(i).isEmpty()) {
                    tmp = bfs(i, n, graph);
                    break;
                }
            }

            int difference = Math.abs((n - tmp) - tmp);
            answer = Math.min(answer, difference);
        }

        return answer;
    }
    
    public int bfs(int node, int n, List<List<Integer>> graph) {
        boolean[] visited = new boolean[n+1];
        Queue<Integer> queue = new ArrayDeque<>();
        visited[node] = true;
        queue.offer(node);
        int cnt = 1;

        while(!queue.isEmpty()) {
            int cur = queue.poll();
            for (int next : graph.get(cur)) {
                if (!visited[next]) {
                    queue.offer(next);
                    visited[next] = true;
                    cnt++;
                }
            }
        }
        return cnt;
    }
}