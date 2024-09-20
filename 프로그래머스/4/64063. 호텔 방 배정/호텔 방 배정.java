import java.util.*;

class Solution {
        public long[] solution(long k, long[] room_number) {
            Map<Long, Long> rooms = new HashMap<>();
            long[] answer = new long[room_number.length];
            for (int i = 0; i < room_number.length; i++) {
                answer[i] = findEmptyRoom(room_number[i], rooms);
            }
            return answer;
        }

        public long findEmptyRoom(long number, Map<Long, Long> rooms) {
            if (!rooms.containsKey(number)) {
                rooms.put(number, number + 1);
                return number;
            }

            long next = findEmptyRoom(rooms.get(number), rooms);
            rooms.replace(number, next + 1);
            return next;
        }

    }