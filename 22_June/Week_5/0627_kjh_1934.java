import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder result = new StringBuilder();
        
        int testCases = Integer.parseInt(br.readLine());
        while (testCases-- > 0) {
            String[] aAndB = br.readLine().split(" ");
            int a = Integer.parseInt(aAndB[0]);
            int b = Integer.parseInt(aAndB[1]);

            result.append(getLCM(a, b)).append('\n');
        }

        System.out.print(result);
        br.close();
    }
    //// 이렇게 함수 분리해두니까 훨씬 직관적이네여 굿굿
    public static int getLCM(int a, int b) {
        return a * b / getGCD(a, b);
    }

    private static int getGCD(int a, int b) {
        if (b == 0) return a;
        return getGCD(b, a % b);
    }
}
////굳굳
