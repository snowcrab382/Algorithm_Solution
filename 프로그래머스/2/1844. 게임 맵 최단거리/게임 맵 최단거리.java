import java.util.*;

class Solution {

    int[] dx = {1,-1,0,0};
    int[] dy = {0,0,1,-1};

    public int solution(int[][] maps) {
        int answer = 0;
        int n = maps.length;
        int m = maps[0].length;
        int[][] visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(visited[i], 0);
        }
        return bfs(maps, visited, 0, 0, n, m);
    }
    
    public int bfs(int[][] maps, int[][] visited, int x, int y, int n, int m) {
        visited[x][y] = 1;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{x, y});
        while (!queue.isEmpty()) {
            int nx, ny;
            int[] next = queue.poll();

            for (int i = 0; i < 4; i++) {
                nx = next[0] + dx[i];
                ny = next[1] + dy[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || maps[nx][ny] == 0) {
                    continue;
                }
                if (visited[nx][ny] == 1) {
                    continue;
                }
                maps[nx][ny] = maps[next[0]][next[1]] + 1;
                visited[nx][ny] = 1;
                queue.add(new int[]{nx, ny});
            }
        }
        
        if (maps[n-1][m-1] == 1) {
            return -1;
        }
        else {
            return maps[n-1][m-1];
        }
    }
}