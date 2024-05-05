import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int cnt = truck_weights.length;
        int bridge_weight = 0;
        int tmp = 0;

        LinkedList<Integer> bridge = new LinkedList<>();
        for (int i = 0; i < bridge_length; i++) {
            bridge.add(0);
        }

        while (cnt > 0) {
            answer++; //시간 증가

            int finish = bridge.poll(); //다리를 빠져나온 물체의 무게
            if (finish != 0) { //무게가 0이 아니면 트럭이므로 카운트
                cnt--;
            }
            bridge_weight -= finish; //다리 위 물체의 무게 총합

            if (tmp == truck_weights.length) { //대기 트럭이 없으면 하위 로직은 스킵
                continue;
            }

            if (bridge_weight + truck_weights[tmp] <= weight) { //다리에 추가 트럭이 진입가능하다면
                bridge.add(truck_weights[tmp]); //트럭 진입
                bridge_weight += truck_weights[tmp]; //트럭 무게만큼 증가
                tmp++; //다음 트럭 인덱스
            }
            else {
                bridge.add(0);
            }
        }
        
        return answer;
    }
}