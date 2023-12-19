class Solution {
    public int solution(int a, int b) {

        String a_s = Integer.toString(a);
        String b_s = Integer.toString(b);

        String ab_s = a_s + b_s;

        int ab_i = Integer.parseInt(ab_s);
        
        if (ab_i >= a * b * 2) {
            return ab_i;   
        }
        else {
            return a * b * 2;
        }
    }
}