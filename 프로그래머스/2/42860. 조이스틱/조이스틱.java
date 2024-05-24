class Solution {
    public int solution(String name) {
        int answer = 0;
        int length = name.length();
        char A = 'A';
        char Z = 'Z';
        
        int idx = 0;
        int move = length - 1;
        for (int i=0; i<length; i++) {
            answer += Math.min(name.charAt(i) - A, Z - name.charAt(i) + 1);
            
            idx = i + 1;
            while (idx < length && name.charAt(idx) == A) {
                idx++;
            }
            move = Math.min(move, i * 2 + length - idx);
            move = Math.min(move, (length - idx)*2 + i);
        }
        System.out.println(answer);
        return answer + move;
    }
}
// A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z
// 0   1   2   3   4   5   6   7   8   9  10  11  12   13  12  11  10  9   8   7   6   5   4   3   2   1

// 0   1   2   3   4   5   6   7   8   9
// B   B   A   A   A   B   A   A   A   B

// tmp
// i - tmp vs len - i + tmp
