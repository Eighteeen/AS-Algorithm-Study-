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
        //// => 솔찌 알고리즘 문제 풀이할때는 크게 의미없긴해요
        //// => 얘의 값은 더 이상 변하지 않는다! 선언함으로써 혹시나 실수로 값을 바꿀 경우를 예방하는 그런 기능임다
        final String input = br.readLine();
        
        StringTokenizer st = new StringTokenizer(input, " ");
        final int N = Integer.parseInt(st.nextToken());
        final int M = Integer.parseInt(st.nextToken());
        //// N * M 해서 -1해주는 게 더 간단하지 않나요??
        //// => N조각으로 일단 나누고 각각 M조각으로 또 나누는 풀이과정을 정리하면 N * M - 1 이라는 공식이 나오긴 하는데
        //// => 풀이과정을 표현해보고 싶어서 요렇게 했어요
        //// => 혹시 N*M-1 공식이 바로 나오는 풀이방법이 있나요?
        int cutIntoNPieces = N - 1;
        int cutIntoMPiecesForEachPiece = (M - 1) * N;
        // 풀이과정을 나타내주니까 어떤 작업을 하고있는지 알기 편리한거 같아여:)

        System.out.print(cutIntoNPieces + cutIntoMPiecesForEachPiece);

        br.close();
    }
}
