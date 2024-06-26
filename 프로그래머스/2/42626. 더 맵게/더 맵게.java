import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int food : scoville) {
            heap.add(food);
        }

        while (heap.peek() < K) {
            if (heap.size() == 1) {
                answer = -1;
                break;
            }
            int x = heap.poll();
            int y = heap.poll();
            heap.add(x + (y * 2));
            answer++;
        }
        return answer;
    }
}