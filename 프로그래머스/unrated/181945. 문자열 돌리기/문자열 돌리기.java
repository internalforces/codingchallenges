import java.util.Scanner;
import java.util.Arrays;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        char[] arr = new char[a.length()];
        for(int i = 0; i < a.length(); i++){
            arr[i] = a.charAt(i);
            System.out.println(arr[i]);   
        }
    }
}