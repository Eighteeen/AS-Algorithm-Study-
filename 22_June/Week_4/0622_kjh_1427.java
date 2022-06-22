import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        final String INPUT = br.readLine();
        System.out.print(sortDigitsByDesc(INPUT));

        br.close();
    }

    public static String sortDigitsByDesc(String digits) {
        int[] digitCount = new int[10];

        for (int i = 0; i < digits.length(); i++) {
            int digit = Character.getNumericValue(digits.charAt(i));
            digitCount[digit]++;
        }

        StringBuilder sb = new StringBuilder();
        for (int digit = 9; digit >= 0; digit--) {
            for (int i = 0; i < digitCount[digit]; i++) {
                sb.append(digit);
            }
        }

        return sb.toString();
    }

    public static int toInt(char ch) {
        return ch - '0';
    }
}
