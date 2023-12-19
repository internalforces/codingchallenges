class Solution {
    public int solution(int a, int b) {
        
        String a_s = Integer.toString(a);
        String b_s = Integer.toString(b);
        
        String ab_s = a_s + b_s;
        String ba_s = b_s + a_s;
            
        int ab_i = Integer.parseInt(ab_s);
        int ba_i = Integer.parseInt(ba_s);
        
        if (ab_i >= ba_i) {
            return ab_i;
        }
        else {
            return ba_i;
        }
    }
}