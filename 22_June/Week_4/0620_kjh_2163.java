import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// 변수명/함수명 등등으로 코드의 의도를 표현하는 식으로 
// 쉽게 읽히는 코드 지향하고 있음!

// 앞으로도 계속 이런 스타일로 코딩할텐데,
// 잘 안 읽히는 부분이 보인다면 => 어떻게 바꾸면 더 잘 읽힐 것 같다고 조언해준다면 매우 감사!
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        //// 조언은 아니고 궁금한건데 final을 쓰면 메모리나 이런게 더 좋은게 있는건가여?
        final String input = br.readLine();
        
        StringTokenizer st = new StringTokenizer(input, " ");
        final int N = Integer.parseInt(st.nextToken());
        final int M = Integer.parseInt(st.nextToken());
        //// N * M 해서 -1해주는 게 더 간단하지 않나요?? 
        int cutIntoNPieces = N - 1;
        int cutIntoMPiecesForEachPiece = (M - 1) * N;

        System.out.print(cutIntoNPieces + cutIntoMPiecesForEachPiece);

        br.close();
    }
}
