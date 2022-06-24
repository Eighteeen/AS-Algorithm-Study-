import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    private static final int MAX_DIGIT = 10;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        final String INPUT = br.readLine();
        System.out.print(sortDigitsByDesc(INPUT));

        br.close();
    }
    //// 정렬 직접 구현한거 구웃
    public static String sortDigitsByDesc(String digits) {
        ////10을 MAX_DIGIT이런식으로 따로 선언해주는거도 좋았을거 같아요! : 👍👍
        int[] digitCount = new int[MAX_DIGIT];
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
}
